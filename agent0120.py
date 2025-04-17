import copy

from agents.baseagent import BaseAgent 
from iso.isomsgbearer import ISOMsgBearer

class Agent0120(BaseAgent):

definit _init_(self) -> None:

super().init()

def processISOmessage(self, imb: ISOMsgBearer)->150MsgBearer:

return self._ processISOmessage(imb)

def _processISOmessage(self, imb: ISOMsgBearer)->ISOMsgBearer:

#TODO Process the message

mti:str = imb.MTI

#logic to differenciate between two MITS 0128 and 0121

if mti == "0120":

pass

elif mti == "0121":

pass

imbOut: ISOMsgBearer copy.deepcopy(imb)

imbOut.setRespondMTI()

return imbOut
