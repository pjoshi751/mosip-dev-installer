# This file contains the config parameters of the launcher. Inspect the file
# carefully before running the launcher.  Esp. MOSIP_DIR.

import os

MOSIP_DIR = os.path.join(os.environ['HOME'], 'mosip')
DB_SCRIPTS_PATH = os.path.join(MOSIP_DIR, 'mosip-platform/db_scripts/')
POSTGRES_PORT = 5432
COUNTRY_NAME='morocco'  # For LDAP 
CONFIG_REPO= os.path.join(MOSIP_DIR, 'myconfig')  # git repo 
LOGS_DIR = os.path.join(MOSIP_DIR, 'mosip-test/deploy/launcher/logs')
