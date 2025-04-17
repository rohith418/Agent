import copy

from agents.baseagent import BaseAgent
 from iso.isomsgbearer import ISOMsgBearer

class Agent0100(BaseAgent): definit (self) -> None:

super().init()

def processISOmessage(self, imb: ISOMsgBearer)->ISOMsgBearer: return self._ processISOmessage(imb)

def _processISOmessage(self, imb: ISOMsgBearer)->ISOMsgBearer:

#TODO Process the message

mti:str = imb.MTI

#logic to differenciate between two MITs 0100 and 0101
 if mti == "0100":
pass 
elif mti == "0101":
pass



imbOut: ISOMsgBearer =  copy.deepcopy(imb)

imbOut.setRespondMTI()

return imbOut
