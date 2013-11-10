import subprocess
import time
import threading
import Queue
from targets import targets

exploit = './railway/exploit.py'
keyfilepath = './keyfiles/railroad'
sleeptime = 45

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
