

# Running the Launcher

- This launcher runs with CenOS 7.
- Make sure you run the same on a completely fresh machine (VM recommended)
- git clone mosip-platform from open source
- Modify  config_server/mosip_configs/kernel.properties to add your email SMTP credentials in the following fields:
    spring.mail.username=<user email id>
    spring.mail.password=<password>
   
- Inspect config.py for any changes. Esp following:
  COUNTRY_NAME 
- cd launcher
- First install environment, then run the services 

