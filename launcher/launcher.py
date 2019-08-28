#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  
# The script has been tried on CentOS 7
# Before running the launcher, install 'gcc' using
# sudo yum install gcc

import subprocess
import argparse
import time
import os
import glob
from logger import init_logger
from db import *
from config import *
from common import *
from ldap_utils import *
from hdfs import *
from clamav import *
from docker import *
from softhsm import *
from config_server import *

logger = logging.getLogger() # Root Logger 

def give_home_read_permissions():
    logger.info('Giving read persmissons to home directory')
    command('chmod 755 %s' % os.environ['HOME']) 

def install_tools():
    #TODO Install python 3.6
    logger.info('Installing  EPEL')
    command('sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
    logger.info('Installing Maven')
    command('sudo yum install -y maven')
    command('sudo yum install -y gcc')
    command('sudo yum install -y gcc-c++')
    command('sudo yum install -y postgresql-devel')
    command('sudo yum install -y python-devel')
    command('sudo pip3.6 install psutil')
    command('sudo pip3.6 install psycopg2')

def install_environ():
    logger.info('Installing environ')
    give_home_read_permissions() # For various access
    install_tools()
    install_docker()
    install_postgres()
    init_db(DB_SCRIPTS_PATH, SQL_SCRIPTS)
    run_hdfs()
    install_clamav()
    install_apacheds()
    load_ldap(COUNTRY_NAME)
    install_softhsm(SOFTHSM_INSTALL_DIR, SOFTHSM_CONFIG_DIR) 
    init_softhsm(SOFTHSM_PIN)
    install_config_repo(CONFIG_REPO)
    logger.info('Env install done')

def start_environ():
    restart_docker() 
    restart_postgres()
    restart_apacheds()
    restart_clamav()
    run_hdfs()

def clone_code(version, repos):
    # TODO: Check out all repos
    pass 

def build_code(code_dir):
    #TODO: Check out code
    logger.info('Building code')
    cwd = os.getcwd() 
    os.chdir(code_dir) 
    command('mvn -DskipTests install')
    os.chdir(cwd)
    logger.info('Building code done')

def init_and_cleanup():
    '''
    Before starting the services, perform cleanup for a fresh start.
    '''
    logger.info('Cleanup ..')
    clean_table('mosip_kernel', 'key_alias') 

def start_services(services, version):
    '''
    The location of the jar file is assumend to at $HOME/.m2/repository/io/mosip/module/service/version' 
    Args:
        services:  List of tuples [(module, service), (module, service) ..] 
        version: Assumed all services have same version specified in pom.xml.
    '''
    logger.info('Starting MOSIP services')    

    init_and_cleanup()

    logger.info('Running Config Server ..')
    err = run_config_server(CONFIG_REPO, LOGS_DIR)
    if err:
        logger.error('Could not run config server. Exiting..')
        return 1
    time.sleep(5)
    logger.info('Running all services..')
    for module, service in services:
        jar_dir = '%s/.m2/repository/io/mosip/%s/%s/%s' % (os.environ['HOME'], 
            module, service, version)
        jar_name = get_jar_name(service, version)
        run_jar(jar_dir, jar_name, LOGS_DIR, CONFIG_SERVER_PORT)

    logger.info('Starting MOSIP services - Done')    

    return 0

def stop_services(services, version):
    '''
    Stop all services given in the 'services' dict 
    Args:
        services:  Dict of form {service_name : service_dir}
    '''
    logger.info('Stopping MOSIP services')
    for module, service in services: 
        jar_name = get_jar_name(service, version)
        kill_process(jar_name)

    logger.info('Stopping Config Server')
    kill_process('spring.cloud.config.server.git.uri')

    logger.info('Stopping MOSIP services - done')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install-environ', action='store_true', help='Install  all the environment needed. The services are run autumatically.  The DB, LDAP etc are  initialized too')   
    parser.add_argument('--start-environ', action='store_true', help='Restart  all environment daemons. This assumes that environ has already been setup.')   
    parser.add_argument('--build-code', action='store_true', help='mvn builds all the jars')
    parser.add_argument('--start-services', action='store_true', help='Run all the services to bring up MOSIP')
    parser.add_argument('--stop-services', action='store_true', help='Stop all running services')

    return parser


def main():
    global logger
    init_logger(logger, 'logs/launcher.log', 10000000, 'info', 2)

    parser = parse_args()
    args = parser.parse_args()

    if args.install_environ:
        install_environ()
    if args.start_environ:
        start_environ()
    if args.build_code:
        build_code(CODE_DIR)
    if args.start_services:
        start_services(MOSIP_SERVICES, MOSIP_VERSION)
    if args.stop_services:
        stop_services(MOSIP_SERVICES, MOSIP_VERSION)
     
if __name__== '__main__':
    main()
       
