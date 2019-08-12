#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  
# The script has been tried on CentOS 7

import subprocess
import argparse
import time
import os
import shutil
import glob
from logger import init_logger
from db import *
from config import *
from common import *
from ldap import *
from hdfs import *
from clamav import *
from docker import *
from config_server import *

logger = logging.getLogger() # Root Logger 

def give_home_read_permissions():
    logger.info('Giving read persmissons to home directory')
    command('chmod 755 %s' % os.environ['HOME']) 

def install_tools():
    logger.info('Installing  EPEL')
    command('sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
    logger.info('Installing Maven')
    command('sudo yum -y install maven')

def install_environ():
    '''
    Clone MOSIP code before installing environment
    '''
    install_tools()
    install_docker()
    install_postgres()
    run_hdfs()
    init_db()
    install_clamav()
    install_apacheds()
    load_ldap(COUNTRY_NAME)
    install_config_repo(CONFIG_REPO)

    #build_code() # TBD
    #run_config_server(CONFIG_REPO, LOGS_DIR)

def clone_code(version, repos):
    # TODO: Check out all repos
    pass 

def build_code(code_dir):
    #TODO: Check out code
    cwd = os.getcwd() 
    os.chdir(code_dir) 
    command('mvn -DskiptTests install')
    os.chdir(cwd)

def run_mosip_services(services, version):
    '''
    Run all services given in the 'services' dict.  The location of the jar
    file is assumend to at $HOME/.m2/repository/io/mosip/module/service/version' 
    Args:
        services:  List of tuples [(module, service), (module, service) ..] 
    '''
    
    for module, service in services:
        jar_dir = '%s/.m2/repository/io/mosip/%s/%s/%s' % (os.environ['HOME'], 
            module, service, version)
        jar_name = service + '-' + version + '.jar'
        run_jar(jar_dir, jar_name, LOGS_DIR, CONFIG_SERVER_PORT)

def stop_mosip_services(services):
    '''
    Stop all services given in the 'services' dict 
    Args:
        services:  Dict of form {service_name : service_dir}
    '''

    pass

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install-environ', action='store_true', help='Install  all the environment needed. The services are run autumatically.  The DB, LDAP etc are  initialized too')   
    parser.add_argument('--build-code', action='store_true', help='mvn builds all the jars')
    parser.add_argument('--run-services', action='store_true', help='Run all the services to bring up MOSIP')
    parser.add_argument('--stop-services', action='store_true', help='Stop all running services')

    return parser


def main():
    global logger
    init_logger(logger, 'logs/launcher.log', 10000000, 'info', 2)

    parser = parse_args()

    give_home_read_permissions() # For various access
    run_mosip_services(MOSIP_SERVICES, MOSIP_VERSION)
    logger.info('Install done')

if __name__== '__main__':
    main()
       
