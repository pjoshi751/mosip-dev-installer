import subprocess
import sys
import os
import glob
import shutil
import time
from common import *
from config import *

logger = logging.getLogger(__name__)

def install_config_repo(repo_path):
    logger.info('Creating config git repo for config server')
    if os.path.exists(repo_path):  # Assuming it is indeed a git repo
        return 
    os.makedirs(repo_path)
    cwd = os.getcwd() 
    os.chdir(repo_path)
    command('git init') 
    files = glob.glob(os.path.join(cwd, '../config_server/mosip_configs/*')) 
    for f in files:
        shutil.copy(f, '.')
    command('git add .')
    command('git commit -m "Added"')
    os.chdir(cwd)

def run_config_server(repo_path, logs_dir):
    logger.info('Running config server')
    cwd = os.getcwd() 
    os.chdir('../config_server/spring_config_server')  
    log_file = '%s/config_server.log' % logs_dir
    command('mvn -Dspring.cloud.config.server.git.uri=%s spring-boot:run >> %s 2>&1 &' % (repo_path, log_file))
    time.sleep(2) 
    f = open(log_file, 'rt')
    r = 0
    while 1:
        line = f.readline()
        if line.find('ERROR') != -1:
            logger.error('Could not start config server')
            r = 1
            break 
        if line.find('Started ConfigServiceApplication') != -1:
            logger.info('config server started')
            break  

    f.close()
    os.chdir(cwd)
    return r 

