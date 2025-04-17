class AuthManager:

def _init_(self, msg):

self.msg = msg

def processAuth(self) -> any:

#clone msg

retMsg = self.msg

--> select status from real card where pan-?

--> if status is 'A' then authroriseMessage(response code "00")

--> if not then declineMessage(response code="14")

#set Field(39, respCode); #

return retMsg

def setResponseCode(self, respCode:str): self.msg["39"] = respCode
