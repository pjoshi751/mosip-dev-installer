import subprocess
import logging

logger = logging.getLogger(__name__)

def command(cmd):
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0: 
        logger.error(r)
        
