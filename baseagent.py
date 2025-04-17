from abc import ABC, abstractmethod
from iso.isomsgbearer import ISOMsgBearer 
from util.observe import Observable

class BaseAgent  (Observable, ABC):

def init(self) -> None:

super().init_()

#self.imb = imb

@abstractmethod

def processISOmessage(self, imb: ISOMsgBearer) -> ISOMsgBearer: pass
