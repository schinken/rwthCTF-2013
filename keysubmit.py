import asyncore
import socket
import datetime
import threading
import sys
import time
from Queue import Queue

q = Queue()

HOST = '10.23.0.1'    # The remote host
PORT = 1              # The same port as used by the server

class IncomingHandler(asyncore.dispatcher_with_send):

    def set_addr(self, addr):
        self.addr = addr

    def handle_read(self):

        key = ""
        while True:
          data = self.recv(1)
          if data == "\n":
              break;
          else:
              key += data
        
        q.put((key, self.addr))

    def handle_close(self):
        print repr(self.addr), "disconnected"
        self.close()

class SubmitServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = IncomingHandler(sock)
            handler.set_addr(addr)


class SubmitKeyToKeyserver(threading.Thread):

    def __init__(self, queue):
        self.keys = {}
        self.kill_received = False
        self.queue = queue

        self.open_sock()
        self.score = 0


        super(SubmitKeyToKeyserver, self).__init__()

    def open_sock(self):

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
        except:

            print "Reconnect failed!!! Waiting 2 sec"
            time.sleep(2)
            self.open_sock()

    def kill(self):
        self.kill_received = True
        self.queue.put("foo")

    def run(self):

        while True:

          if self.kill_received:
              print "Killing thread"
              return

          tmp = self.queue.get()
          key, addr = tmp[0], tmp[1]
          if key in self.keys:
              #print datetime.datetime.now(), "Skipping ("+key+")"
              self.queue.task_done()
              continue
 
          try:
              self.sock.sendall(key+"\n")
              result = self.sock.recv(1024)
          except:
              # handle disconnect
              self.sock.close()
              self.open_sock()

              self.sock.sendall("INIT\n")
              result = self.sock.recv(1024)

              self.sock.sendall(key+"\n")
              
              result = self.sock.recv(1024)

          if 'Congratulations' in result:
                self.score += 1
                print datetime.datetime.now(), "Successful: ", self.score

          print datetime.datetime.now(), "Submitted key ("+key+") from "+repr(addr)+" :: ["+result.strip()+"]"

          self.keys[key] = True
          self.queue.task_done()


try:
    tmp = SubmitKeyToKeyserver(q)
    tmp.start()

    q.put("INITAL")

    server = SubmitServer('localhost', 8080)
    asyncore.loop()
except KeyboardInterrupt:
    print "Ctrl-c received! Sending kill to threads..."
    tmp.kill()
    sys.exit(1)
