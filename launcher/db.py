import subprocess
import os
import logging
from common import *
from config import *

logger = logging.getLogger(__name__)

PG_CONF_DIR = '/var/lib/pgsql/10/data'
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

    'mosip_pmp/mosip_role_common.sql',
    'mosip_pmp/mosip_role_pmpuser.sql',
    'mosip_pmp/mosip_pmp_db.sql',
    'mosip_pmp/mosip_pmp_grants.sql',
    'mosip_pmp/mosip_pmp_ddl_deploy.sql',

    'mosip_prereg/mosip_role_common.sql',
    'mosip_prereg/mosip_role_prereguser.sql',
    'mosip_prereg/mosip_prereg_db.sql',
    'mosip_prereg/mosip_prereg_grants.sql',
    'mosip_prereg/mosip_prereg_ddl_deploy.sql',
    'mosip_prereg/mosip_prereg_dml_deploy.sql',

    #'mosip_reg/mosip_reg_db.sql',
    #'mosip_reg/mosip_reg_ddl_deploy.sql',
    #'mosip_reg/mosip_reg_dml_deploy.sql',

    'mosip_regprc/mosip_role_common.sql',
    'mosip_regprc/mosip_role_regprcuser.sql',
    'mosip_regprc/mosip_regprc_db.sql',
    'mosip_regprc/mosip_regprc_grants.sql',
    'mosip_regprc/mosip_regprc_ddl_deploy.sql',
    'mosip_regprc/mosip_regprc_dml_deploy.sql'
]
def install_postgres():
    logger.info('Installing postgres')
    command('sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm')
    command('sudo yum -y install postgresql10')
    command('sudo yum -y install postgresql10-server')
    command('sudo /usr/pgsql-10/bin/postgresql-10-setup initdb')
    command('sudo systemctl enable postgresql-10')
    command('sudo systemctl start postgresql-10')

def configure_postgres():
    logger.info('Modify the pg_hba.conf file for "trust" access')
    command('sudo -u postgres mv %s/pg_hba.conf %s/pg_hba.conf.bak' % (PG_CONF_DIR, PG_CONF_DIR))
    command('sudo -u postgres cp resources/pg_hba.conf %s/pg_hba.conf' % PG_CONF_DIR)
    command('sudo systemctl restart postgresql-10') 

def init_db():
    configure_postgres()
    pwd = os.getcwd()    
    os.chdir(DB_SCRIPTS_PATH)
    for sql_path in SQL_SCRIPTS:
        sql_dir = os.path.join(DB_SCRIPTS_PATH, os.path.dirname(sql_path)) 
        sql_file = os.path.basename(sql_path)
        os.chdir(sql_dir)
        command('sudo -u postgres psql -f %s' % sql_file)

    os.chdir(pwd) # Return back to where we started 
