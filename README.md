# pir
A python script to monitor a PIR sensor on the Intel Galileo Gen 2

Usage: ./pir.py pinNumber

    root@galileo:~# ./pir.py 4
    Waiting for PIR to settle
    5
    4
    3
    2
    1
    Detecting movement
    Motion Detected 2016-02-25 00:08:46.188826
    Motion Detected 2016-02-25 00:08:54.199816
    Motion Detected 2016-02-25 00:08:56.202630

Help: 

    root@galileo:~# ./pir.py --help
    usage: pir.py [-h] [--version] pinNumber
    
    Script to monitor PIR sensor on Intel Galileo
    
    positional arguments:
      pinNumber   The pin number the PIR is attached to. i.e. 2-13
    
    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit

Example Wiring
![alt tag](https://raw.githubusercontent.com/joemcmanus/pir/master/GalileoGen2-PIR.png)
