# This file contains the config parameters of the launcher. Inspect the file
# carefully before running the launcher.  Esp. MOSIP_DIR.

import os

MOSIP_DIR = os.path.join(os.environ['HOME'], 'mosip')
DB_SCRIPTS_PATH = os.path.join(MOSIP_DIR, 'mosip-platform/db_scripts/')
CODE_DIR = os.path.join(MOSIP_DIR, 'mosip-platform')
POSTGRES_PORT = 5432
CONFIG_SERVER_PORT = 8888 # Should be same as in application.properties of 
                          # config-server
COUNTRY_NAME='morocco'  # For LDAP 
CONFIG_REPO= os.path.join(MOSIP_DIR, 'myconfig')  # git repo 
LOGS_DIR = os.path.join(MOSIP_DIR, 'mosip-launcher/launcher/logs')
