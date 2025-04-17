import binascii


from iso.IS08583parser import pack, unpack
from iso.spec import WFISOConfigSpec as wfISOspec


class ISOMsgBearer:
HEADER_LENGTH:int = 22
def _init(self) ->None:
self.header:bytes = None
self.message:dict = dict()
def init(self, header: bytes, message:bytes) -> None:
self.header:bytes = header
self.message:dict = dict()
self.unpack(message)


@property
def MTI(self) -> str:
return self.message.get("MTI")


@MTI.setter
def MTI(self, mti:str):
self.message["MTI"]=mti
def setRespondMTI(self) -> str:
mti = self.MTI
mti = mti[0:2] + str(int(mti[2])+1) + "0"
self.message["MTI"]=mti
return mti

def isInMessage(self) -> bool:
return int(self.MTI[2])%2==0
def isRetransMessage(self) -> bool:
return self.MTI[3] == "1'
@property
def IspMessage(self) -> dict:
return self.message


@property
def Header(self) ->bytes:
return self.header


@Header.setter
def Header(self, header:bytes):
self.header = header


def pack(self) -> bytes:


returns ISO message body in bytes format


return pack(self.message, iso_config=wfISOspec, hex_bitmap-True)


def unpack(self, msgBytes: bytes) -> dict:
isoMsg = unpack(binascii.hexlify(msgBytes), iso_config=wfISOspec, hex_bitmap=True)
self.message = isoMsg
~eturn isoMsg


#TODO set field 39
# r.set(39, cfg.get("rc", "00"));
