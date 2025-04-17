import threading


import queue
import socket
import time


from iso.isomsgbearer import ISOMsgBearer
from multiplex.basemux import BaseMux


class MsgReceiverThread(threading.Thread, BaseMux):
def init(self, client:socket.socket, rxQueue:queue.Queue, rxLock:threading.Lock, name: str | None = None, daemon: bool | None = None) -> None:
super(._init(None, None, name= name, daemon-daemon)
self.name = name
self.terminated = False
self.rxQueue: queue.Queue = rxQueue
self.rxlock:threading.lock= rxLock
self.socketReadLock:threading.Lock = threading.Lock()
self.client:socket.socket = client
print(f"Init í_name_ ]: fself.name]")


def terminate(self) -> None:
self.terminated = True
try:
self.client.close(
except:
pass


print(f"(_name)|(self.name)|terminated")


def run(self) -> None:
print(f"Run started [_name_): (self.name)")
while not self.terminated:
header, msg self.receive()
imb - ISOMsgBearer (header, msg)
print(f"ISOMsgBearer (imb.IsoMessage): (self.name) queued for proecssing")
with self.rxLock:
self.rxQueue.put(imb)
time.sleep(0.2) #TODO -- Check if sleep required if required how much time it should be..
print(f"Run ended name): (self.name)")


#return super().run()


def receive(self) -> tuple:
"""receive() -> (header:bytes, message:bytes)"""
with self.socketReadLock:


print(f"(name)|íself.name)|client socket waiting to receive")
lenBytes=self.client.recv(2)
#Belogic is to find lenght of message
totalMessageLen = (lenBytes[0] & 0xFF) << 8 | lenBytes[1] & 0xFF
#LOG. debug(f'MessageLength: [totalMessageLen)')


headerBytes = self.client.recv(ISOMsgBearer.HEADER_LENGTH)
messageBytes = self.client.recv(totalMessageLen-ISOMsgBearen.HEADER_LENGTH)
print(f"received (name_): (self.name)", messageBytes, headerBytes)
#LOG. debug(f"Header: (headerBytes) Body Bytes: (messageBytes) Body Hex: (messageBytes.hex())")
return (headerBytes, messageBytes)
