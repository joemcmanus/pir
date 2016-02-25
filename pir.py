#!/usr/bin/env python
# File    : pir.py  An example script of reading a Parallax PIR sensor
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  02/24/2016
# Copyright (C) 2016 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import time             
import mraa    
import datetime

parser = argparse.ArgumentParser(description='Script to monitor PIR sensor on Intel Galileo')
parser.add_argument('pinNumber', help="The pin number the PIR is attached to. i.e. 2-13", type=int)
parser.add_argument('--version', action='version',version='%(prog)s 0.1')
args=parser.parse_args()

pin = mraa.Gpio(args.pinNumber)
pin.dir(mraa.DIR_IN)


print("Waiting for PIR to settle")
i=5
while i > 0:
	print i
	time.sleep(1)
	i=i-1

print("Detecting movement")
try:
	while True: 
		if pin.read(): 
			print("Motion Detected " + str(datetime.datetime.now()))
		time.sleep(2)
except:
	quit()
