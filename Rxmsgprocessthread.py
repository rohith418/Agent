from abc import abstractmethod
import threading
import queue
import time
from iso.isomsgbearer import ISOMsgBearer
from multiplex.basemux import TransBaseMux
from multiplex.mulprocs.receivedmsgmux import ReceivedMsgMux
from util.observe import Observable
from multiprocessing import Queue as PQueue, Lock as PLock


class RxMsgProcessThread(threading.Thread, TransBaseMux, Observable):


def _init(self, rxQueue:queue.Queue, rxLock:threading.Lock, txQueue:queue.Queue, txLock:threading.Lock, name: str | None - None, daemon: bool | None - None) -> None:
super()._init_(None, None, name= name, daemon=daemon)
self.name = name
self.rxQueue:queue.Queue = rxQueue
self.rxlock:threading.Lock= rxLock
self.txQueue:queue.Queue = txQueue
self.txLock:threading.lock = txLock
self.terminated = False
self.pQueue:PQueue = PQueue()
self.pLock
PLock()
#self.attach()
print(f"(_name)|(self.name)|Initiated")
def terminate(self) -> None:
self.terminated = True
print(f"(name_>|(self.name)|terminated")


def run(self) -> None:
print(f"Run started f_name__): (self. name)")
try:
while not self.terminated:
msg:ISOMsgBearer- None
with self.rxLock:
if self.rxQueue.empty():
print(f"(name |iself.name>|rxQueue is emty")
time.sleep(1)
else:


msg - self.rxQueue.get()
if not (msg is None):


print(f"/name)|tself.name)|message_found and sending it to mux receiver")
P ReceivedMsgMux(msg, self.pQueue, self.pLock, self.name+":RxMUX")
p.start()


if not self.pQueue.empty():
with self.pLock:
selfappendTxQueue(self.pQueue.get())


#--While loop end
except KeyboardInterrupt as e:
print(f"(_name):(self.name)--Keyboard interrupt")
self.terminate(
return
print(f"Run ended [_name): (self.name)")
return super()run()


def appendTxQueue(self, msg:ISOMsgBearer).
with self.txlock:
self.txQueue.put(msg)
