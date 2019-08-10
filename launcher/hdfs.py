import subprocess
import sys
import time 
from common import *
from config import *

logger = logging.getLogger(__name__)

def run_hdfs():
    logger.info('Running HDFS docker container')
    proc = subprocess.Popen('docker run -d sequenceiq/hadoop-docker:2.7.0', shell=True, stdout=subprocess.PIPE)
    container_id = proc.stdout.readline().strip()
    container_id = container_id.decode() # bytes -> str
    proc = subprocess.Popen('docker attach %s' % container_id, stdout=subprocess.PIPE, shell=True)
    while 1: 
        s = proc.stdout.readline().decode() # bytes -> str
        logger.info(s)
        if s.find('starting nodemanager') != -1: 
            break
        time.sleep(1) 
    logger.info('HDFS started')
    return container_id

def stop_hdfs(container_id):
    logger.info('Stopping HDFS docker container')
    command('docker container stop %s' % container_id)

