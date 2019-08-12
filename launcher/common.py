import subprocess
import logging
import os
from config import *

logger = logging.getLogger(__name__)

def command(cmd):
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0: 
        logger.error(r)
        
def get_jar_name(service, version):
    return service + '-' + version + '.jar'

def run_jar(jar_dir, jar_name, logs_dir, config_port, 
            max_heap_size=JAVA_HEAP_SIZE):
    cwd = os.getcwd() 
    os.chdir(jar_dir)
    options = [
        '-Dspring.cloud.config.uri=http://localhost:%d' % config_port, 
        '-Dspring.cloud.config.label=master',
        '-Dspring.profiles.active=dev',
        '-Xmx%s' % max_heap_size 
    ]
    command('java %s -jar %s >>%s/%s.log 2>&1 &' % (' '.join(options), 
                                                    jar_name, logs_dir, 
                                                    jar_name))
    logger.info('%s run in background' % jar_name)
    os.chdir(cwd)
