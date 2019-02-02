#!/usr/bin/env python

import os, sh
from time import sleep
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
import boot_selector_config

try:
	print('\032[1;32;40m mounting /dev/mmcblk0p2')
	sh.mount('/dev/mmcblk0p2','/mnt')
except sh.ErrorReturnCode_32:
	print('\033[1;33;40m \t/dev/mmcblk0p2 is already mounted')
	pass
except sh.ErrorReturnCode_1:
	print('\031[1;31;40m Run as root!')
	quit(1)
except Exception as e:
	print('\031[1;31;40m {0}\n{1} -> {1}'.format(e, type(e).__name__, e.args))
	quit(2)

if not os.path.isfile('./images.log'):
	print('\032[1;33;40m creating images.log file')
	sh.touch('./images.log')
else:
	print('\032[1;32;40m images.log file exists')

if not os.path.isfile('/mnt/data/runonce'):
	print('\032[1;33;40m creating runonce file')
	sh.touch('/mnt/data/runonce')
	runonce_file = open('/mnt/data/runonce', 'w')
else:
	print('\033[1;32;40m runonce file exists')
	runonce_file = open('/mnt/data/runonce', 'w')

berry_images = sh.ls('/mnt/images')
print('\033[1;32;40m found images:')
print('\033[1;36;40m {0}'.format(berry_images))
log_file = open('./images.log', 'w')
log_file.writelines(berry_images)
log_file.close()
print('\033[1;32;40m images written to images.log file')

print('\033[1;32;40m checking gpio for boot selection')
for gpio_pin, image in boot_selector_config.gpio_image.items():
	gpio.setup(gpio_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
	gpio_state = gpio.input(gpio_pin)
	print('\033[1;36;40m \tgpio {0} = {1}'.format(gpio_pin, not bool(gpio_state)))
	if not gpio_state:
		#looking for a LOW signal
		try:
			print('\033[1;32;40m writing {0} to /mnt/data/runonce'.format(image))
			sh.echo(image, _out=runonce_file)
			runonce_file.close()
			print('\033[1;33;40m rebooting in:')
			for t in reversed(range(boot_selector_config.countdown)):
				print('\033[1;31;40m \t{0}'.format(t))
				sleep(1)
			gpio.cleanup()
			sh.reboot()
		except Exception as e:
			print('\033[1;31;40m {0}\n{1} -> {1}'.format(e, type(e).__name__, e.args))
			quit(2)
gpio.cleanup()
runonce_file.close()
print('\033[1;31;40m error: check the switch connections or config')
quit(2)
