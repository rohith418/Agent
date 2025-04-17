from collections.abc import Callable
import multiprocessing
#import copy


from agents.agentmanager import AgentManager
from agents.baseagent import BaseAgent
from iso.isomsgbearer import ISOMsgBearer
from multiplex.basemux import BaseMux, TransBaseMux


class ReceivedMsgMux(multiprocessing.Process, BaseMlux):
def init_(self, imb:ISOMsgBearer, pQueue, pLock, name: str | None - None, daemon: bool | None - None) -> None: #parent:TransBaseMux,
super()._init_(name- name, daemon-daemon)
self.name- name


self.rxMessage:ISOMsgBearer = imb


self.pQueue:multiprocessing.Queue = pQueue
self.pLock - pLock


#self.txMessage:ISOMsgBearer = None#copy.deepcopy(imb)
self.terminated = False
#self.rxParent:TransBaseMux = parent
print(f"(_name>|(self.name)|initiated")


def terminate(self) -> None:
self.terminated = True
print(f"[name_>|(self.name)|terminated")
return super().terminate()
def run(self) -> None:
print(f"Run started (name): (self.name)")
#process mesaages using processors
if not self.terminated:
print(f"(name)|(self.name)|received msg:
mti:str = self.rxMessage.MTI
agent:BaseAgent= AgentManager().get(mti)


self.rxMessage.message)


txMessage:ISOMsgBearer= agent.processISOmessage(self.rxMessage)


# at the end call reply/reshond message back to parent
#self.rxParent.appendTxQueue(msg=txMessage)
with selfpLock:
self.pQueue.put(txMessage)


print(f"Run ended (_name): (self.name)")
