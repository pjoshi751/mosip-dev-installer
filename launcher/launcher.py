#!/usr/bin/python3.6
# Centos - Get the full DVD iso.  Custom select softwares - select GNU Desktop
# version while installing in VM.  
# The script has been tried on CentOS 7

import subprocess
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
from config_server import *

logger = logging.getLogger() # Root Logger 

def give_home_read_permissions():
    logger.info('Giving read persmissons to home directory')
    command('chmod 755 %s' % os.environ['HOME']) 

def install_docker():
    logger.info('Install Docker')
    command('sudo yum check-update')
    command('curl -fsSL https://get.docker.com/ | sh')
    command('sudo systemctl start docker')
    command('sudo systemctl enable docker')

def install_tools():
    logger.info('Installing  EPEL')
    command('sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
    logger.info('Installing Maven')
    command('sudo yum -y install maven')

def build_code(code_dir):
    cwd = os.getcwd() 
    os.chdir(code_dir) 
    command('mvn -DskiptTests install')
    os.chdir(cwd)

def run_jar(jar_dir, jar_name, logs_dir):
    cwd = os.getcwd() 
    os.chdir(jar_dir)
    command('java -Dspring.cloud.config.uri=http://localhost:%d -Dspring.cloud.config.label=master -jar %s >>%s/%s.log' % (CONFIG_SERVER_PORT, jar_name, logs_dir, jar_name))
    os.chdir(cwd)


def main():
    global logger
    init_logger(logger, 'logs/launcher.log', 10000000, 'info', 2)

    give_home_read_permissions() # For various access
    #install_tools()
    #install_docker()
    #install_postgres()
    #init_db()
    #install_clamav()
    #install_apacheds()
    #load_ldap(COUNTRY_NAME)
    #run_hdfs()
    #install_config_repo(CONFIG_REPO)
    #build_code() # TBD
    run_config_server(CONFIG_REPO, LOGS_DIR)
    logger.info('Install done')

if __name__== '__main__':
    main()
       
