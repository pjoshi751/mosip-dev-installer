import logging
from common import *
from config import *

logger = logging.getLogger(__name__)

def install_docker():
    logger.info('Install Docker')
    command('sudo yum check-update')
    #command('curl -fsSL https://get.docker.com/ | sh')
    #command('sudo usermod -a -G docker $USER') # Give access to current user
    #command('exec su -l $USER') # Don't need to logout with this
    command('sudo yum install -y docker-ce')
    command('sudo systemctl start docker')
    command('sudo systemctl enable docker')

def restart_docker():
    logger.info('Restarting Docker')
    command('sudo systemctl restart docker')
    command('exec su -l $USER') # TODO: permission problem without this. 
