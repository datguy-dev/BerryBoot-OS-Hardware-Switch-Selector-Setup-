1. Install BerryBoot and add your desired images.
2. Install Raspbian Lite. (~300 mb)
3. Use `raspi-config` to setup networking if needed and auto-login of the user pi.
4. Install pip, sh, and pyftpdlib, for python
5. Adjust at least the FTP values of `boot_selector_config.py`.
6. Transfer the Python files to Raspbian Lite. (`Boot_selector.py` etc.)
7. Append the following to the end of `/home/pi/.bashrc`:
```
#Adjust the dirs accordingly.
sudo python /home/pi/ftp_server.py && sleep 2s &
sudo python /home/pi/boot_selector.py
```
8. Make sure the switch is not connected for the first run in order to generate the required filenames. Use the command: `source ~/.bashrc`. You should now have a working FTP server and a text file in the same directory named `images.log`.
9. Adjust boot_selector_config.py with the right filenames from `images.log` and the GPIO you wish to use for the switch. 


When everything is set up. Upon rebooting, the ftp server starts. The images.log file is produced. If the switch IS connected, the system will begin a countdown timer and reboot to the image that you have designated in the config file for the corresponding GPIO. If the switch is NOT connected, the system will not reboot, allowing you to connect via FTP to adjust the config file as needed.
