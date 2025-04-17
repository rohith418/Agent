import copy

from agents.baseagent import BaseAgent 
from iso.isomsgbearer import ISOMsgBearer

class Agent0400 (BaseAgent):

def _init_(self) -> None:

super().init_()

def processISOmessage(self, imb: ISOMsgBearer)->ISOMsgBearer:

return self. process ISOmessage(imb)

def_processISOmessage(self, imb: ISOMsgBearer)->ISOMsgBearer:

#TODO Process the message

mti:str = imb.MTI

#logic to differenciate between two MITS 0120 and 0121

if mti == "0400":

pass

elif mti == "0401":

pass

elif mti == "0420":

pass

elif mti == "0421":

pass

imbOut: ISOMsgBearer = copy.deepcopy(imb)

imbOut.setRespondMTI()

return imbOut
