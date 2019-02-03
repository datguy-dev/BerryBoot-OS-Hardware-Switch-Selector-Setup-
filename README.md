1. Install BerryBoot and add your desired images.
2. Install Raspbian Lite. (~300 mb)
3. Use raspi-config to setup networking if needed and auto-login of the user pi.
4. Install pip, sh, and pyftpdlib, for python
5. Adjust the FTP sections of boot_selector_config.py
6. Transfer the Python files to Raspbian Lite. (Boot_selector.py etc.)
7. Edit and append to /home/pi/.bashrc to include:
...
sudo python /home/pi/ftp_server.py && sleep 2s &
sudo python /home/pi/boot_selector.py
...

Upon rebooting, the ftp server starts. If the switch IS connected, it will reboot to the image that you have designated in the config file for that GPIO. If the switch is NOT connected, the system will not reboot allowing you to connect and adjust the config file as needed. Additionally, when boot_selector.py is ran, even if it fails normally it'll generate an images.log file which can be used to adjust the filename's for the config file. 
