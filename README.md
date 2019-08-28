

# Running the Launcher

- This launcher runs with CenOS 7.
- Make sure you run the same on a completely fresh machine (VM recommended)
- git clone mosip-platform from open source
- Modify  config_server/mosip_configs/kernel.properties to add your email SMTP credentials in the following fields:
    spring.mail.username=<user email id>
    spring.mail.password=<password>
   
- Inspect launcher/config.py for any changes. Esp following:
  COUNTRY_NAME 
- cd launcher
- First install environment, then run the services 


Notes:

- Create a new VM with CentOS 7:  CentOS-7-x86_64-DVD-1810.iso 
- At least 8 GB RAM, 2 CPUs
- Make sure network is enabled on the VM using the option -NAT -> wifi adapter

- add current user to sudoers file 
- Install gcc, git
- Install python 3.5
Method 1:
--------
https://www.rosehosting.com/blog/how-to-install-python-3-6-4-on-centos-7/

Method2:
https://tecadmin.net/install-python-3-6-on-centos/
$ sudo ln -s /usr/local/bin/pip3.6 /bin/pip3.6

Tools:
Download and install Apache Studio DS
http://directory.apache.org/studio/download/download-linux.html

Accordingly change the path in launcher.py

- create 'mosip' directory in home
- clone mosip-launcher repo 
- git clone mosip-platform
  - checkout tag 0.9.0_phil
- Set google mail to receive messages from apps

- launcher --install-environ
from launcher directory
- launcher --start-environ - use only after reboot
- launcher build code
 - comment out others except kernel and prereg
- logs/
- After running all services.  Check logs for services to start up.  grep for "ERROR".

-- "mycountry" needs to be changed in all .ldif files as well.
-- config server runs on port 8888 by default.  It may conflict with some services.


