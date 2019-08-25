# This file contains the config parameters of the launcher. Inspect the file
# carefully before running the launcher.  Esp. MOSIP_DIR.

import os

MOSIP_DIR = os.path.join(os.environ['HOME'], 'mosip')
MOSIP_VERSION = '0.9.0'  # Such a tag should exist on the repo
MOSIP_REPO = 'https://github.com/mosip/mosip-platform'

CODE_DIR = os.path.join(MOSIP_DIR, 'mosip-platform')

POSTGRES_PORT = 5432
PG_CONF_DIR = '/var/lib/pgsql/10/data'  # Postgres

CONFIG_SERVER_PORT = 8888 # Should be same as in application.properties of 
                          # config-server
COUNTRY_NAME='morocco'  # For LDAP 

# Local repo where all config files of MOSIP will be fetched by config server.
CONFIG_REPO= os.path.join(MOSIP_DIR, 'myconfig')  # git repo 
LOGS_DIR = os.path.join(MOSIP_DIR, 'mosip-launcher/launcher/logs')

JAVA_HEAP_SIZE = '256m' 

DB_SCRIPTS_PATH = os.path.join(MOSIP_DIR, 'mosip-platform/db_scripts/')
SQL_SCRIPTS = [  # These are in a paritcular sequence
    'mosip_kernel/mosip_role_common.sql',
    'mosip_kernel/mosip_role_kerneluser.sql',
    'mosip_kernel/mosip_kernel_db.sql',
    'mosip_kernel/mosip_kernel_grants.sql',
    'mosip_kernel/mosip_kernel_ddl_deploy.sql',
    'mosip_kernel/mosip_kernel_dml_deploy.sql',

    'mosip_audit/mosip_role_common.sql',
    'mosip_audit/mosip_role_audituser.sql',
    'mosip_audit/mosip_audit_db.sql',
    'mosip_audit/mosip_audit_grants.sql',
    'mosip_audit/mosip_audit_ddl_deploy.sql',

    'mosip_iam/mosip_role_common.sql',
    'mosip_iam/mosip_role_iamuser.sql',
    'mosip_iam/mosip_iam_db.sql',
    'mosip_iam/mosip_iam_grants.sql',
    'mosip_iam/mosip_iam_ddl_deploy.sql',
    'mosip_iam/mosip_iam_dml_deploy.sql',

    'mosip_ida/mosip_role_common.sql',
    'mosip_ida/mosip_role_idauser.sql',
    'mosip_ida/mosip_ida_db.sql',
    'mosip_ida/mosip_ida_grants.sql',
    'mosip_ida/mosip_ida_ddl_deploy.sql',

    'mosip_idmap/mosip_role_common.sql',
    'mosip_idmap/mosip_role_idmapuser.sql',
    'mosip_idmap/mosip_idmap_db.sql',
    'mosip_idmap/mosip_idmap_grants.sql',
    'mosip_idmap/mosip_idmap_ddl_deploy.sql',

    'mosip_idrepo/mosip_role_common.sql',
    'mosip_idrepo/mosip_role_idrepouser.sql',
    'mosip_idrepo/mosip_idrepo_db.sql',
    'mosip_idrepo/mosip_idrepo_grants.sql',
    'mosip_idrepo/mosip_idrepo_ddl_deploy.sql',

    'mosip_master/mosip_role_common.sql',
    'mosip_master/mosip_role_masteruser.sql',
    'mosip_master/mosip_master_db.sql',
    'mosip_master/mosip_master_grants.sql',
    'mosip_master/mosip_master_ddl_deploy.sql',
    'mosip_master/mosip_master_dml_deploy.sql',
  
    # TODO: Not in version 0.9.0
    #'mosip_pmp/mosip_role_common.sql',
    #'mosip_pmp/mosip_role_pmpuser.sql',
    #'mosip_pmp/mosip_pmp_db.sql',
    #'mosip_pmp/mosip_pmp_grants.sql',
    #'mosip_pmp/mosip_pmp_ddl_deploy.sql',

    'mosip_prereg/mosip_role_common.sql',
    'mosip_prereg/mosip_role_prereguser.sql',
    'mosip_prereg/mosip_prereg_db.sql',
    'mosip_prereg/mosip_prereg_grants.sql',
    'mosip_prereg/mosip_prereg_ddl_deploy.sql',
    'mosip_prereg/mosip_prereg_dml_deploy.sql',

    # TODO: Some problem running these
    #'mosip_reg/mosip_reg_db.sql', 
    #'mosip_reg/mosip_reg_ddl_deploy.sql',
    #'mosip_reg/mosip_reg_dml_deploy.sql',

    'mosip_regprc/mosip_role_common.sql',
    'mosip_regprc/mosip_role_regprcuser.sql',
    'mosip_regprc/mosip_regprc_db.sql',
    'mosip_regprc/mosip_regprc_grants.sql',
    'mosip_regprc/mosip_regprc_ddl_deploy.sql',
    #'mosip_regprc/mosip_regprc_dml_deploy.sql' # TODO: not in 0.9.0 
]

MOSIP_SERVICES = [ 
    ('kernel', 'kernel-auth-service'),
    ('kernel', 'kernel-keymanager-service'),
    ('kernel', 'kernel-otpmanager-service'),
    ('kernel', 'kernel-emailnotification-service'),
    ('kernel', 'kernel-masterdata-service'),
    ('preregistration', 'pre-registration-login-service'),
    ('preregistration', 'pre-registration-notification-service'),
    ('preregistration', 'pre-registration-demographic-service')
]
