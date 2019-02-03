1. Install BerryBoot and add your desired images.
2. Install Raspbian Lite. (~300 mb)
3. Use raspi-config to setup networking if needed and auto-login of the user pi.
4. Install pip, sh, and pyftpdlib, for python
5. Adjust at least the FTP values of boot_selector_config.py
6. Transfer the Python files to Raspbian Lite. (Boot_selector.py etc.)
7. Append the following to the end of /home/pi/.bashrc:
```
sudo python /home/pi/ftp_server.py && sleep 2s &
sudo python /home/pi/boot_selector.py
```
8. Do not connect the switch for the first run in order to generate the required filename information. 
9. Adjust boot_selector_config.py with the right filenames and GPIO for the switch and reboot. 

The image designation works in the config file by assigning a GPIO number (BCM scheme) to an OS image filename. Your switch will connect to those GPIO. You don't know the image filenames yet so your first run won't be successful. However, the images.log file will provide you with those names to make proper adjustments. You may also use the terminal output if needed.

When everything is set up. Upon rebooting, the ftp server starts. The images.log file is produced. If the switch IS connected, the system will countdown and reboot to the image that you have designated in the config file for the corresponding GPIO. If the switch is NOT connected, the system will not reboot allowing you to connect via FTP to adjust the config file as needed.
