import logging
from common import *
from config import *

logger = logging.getLogger(__name__)

def install_docker():
    logger.info('Install Docker')
    command('sudo yum check-update')
    command('curl -fsSL https://get.docker.com/ | sh')
    command('sudo systemctl start docker')
    command('sudo systemctl enable docker')
