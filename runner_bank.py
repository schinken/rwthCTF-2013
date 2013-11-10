import subprocess
import time
import threading
import Queue
from targets import targets

exploit = './bank/exploit.py'
keyfilepath = './keyfiles/bank'
sleeptime = 45

#keyfile = open(keyfilepath, 'a+')

roundctr = 1
while True:
  plist = []
  fc = 0
  sc = 0                        
  ec = 0
  print "Spawning exploits ...."
  for target in targets:
    args = exploit + " " +  target
    import os
    os.system(args + " >>  " + keyfilepath+ "&")

  time.sleep(sleeptime)
