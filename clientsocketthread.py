import socket
import threading
import queue
import time
from multiplex.basemux import BaseMux
import util
import util.observe


from multiplex.threads.msgreceiverthread import MsgReceiverThread
from multiplex.threads.msgresponderthread import MsgResponderThread
from multiplex.threads.rxmsgprocessthread import RxMsgProcessThread


class ClientSocketHandler(threading.Thread, util.observe.Observable, BaseMux):
def init_(self, serverHost:str, serverPort: int, name:str = "client") -> None:
super()._init(None, None, name= name)
self.name:str= f"(name)@[serverHost):(serverPort)"
self.serverHost = serverHost
self.serverPort - serverPort
self. txQueue:queue Queue
IE
None


self.rxQueue:queue.Queue= None
self.txlock:threading.Lock= None
self.rxlock:threading.Lock=None
self.client:socket.socket = None
self.reInit(
self.stateChanged - False
self.listThreads:list - []
self.terminated:bool = False
def run(self) -> None:
try:
self,


delegateListeners()


while not self.terminated:
self.monitorThreads()


except KeyboardInterrupt as e:
print(f"(_name_):(self.name)--Keyboard interrupt")
self.terminate()
return


#return super().run()


def reInit(self):
self.txQueue:queue.Queue= queue.Queue()
self.rxQueue:queue.Queue -queue.Queue()
self.txLock:threading.Lock= threading.Lock(
self.rxLock:threading.Lock threading.Lock()
self.client:socket.socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self.client.connect((self.serverHost, self.serverPort))
#TODO Handle ConnectionRefusedError
def __delegateListeners(self):
if self.client:


print(f"delegatelistners: (self.name)")
t1 = MsgReceiverThread(self.client, self.rxQueue, self.rxLock, name= self.name+"receiver"
t2 = MsgResponderThread(self.client, self.txQueue, self.txLock, name=self.name+"responder")
t3 = RxMsgProcessThread(self.rxQueue, self.rxLock, self.txQueue, self.txLock, name=self.name+"rxprocess")
#t4 = threading.Thread(target=self.monitorThreads, args=())
self.listThreads.extend([t1,t2,t3])
t1.start()
t2.start()
t3.start()
#t4.start()
#t1.join()
# t2.join()
# t3.join()
print("delegateListners end")
def monitorThreads(self):


time.sleep(3)
for t in self. listThreads:
if self.terminated: break
if isinstance(t, threading.Thread):
tc:threading. Thread
II
t
if not tc.is_alive():
print(tc.getName(), "not alive")
else:
print(tc getName
"is alive")


def terminate(self) -> bool:
self.terminated = True


for t in self listThreads:
if isinstance(t, BaseMux):
tc: BaseMux
t
tc.terminate()


return self.terminated
