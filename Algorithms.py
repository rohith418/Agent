from abc import ABC, abstractmethod
from Crypto.Cipher import Blowfish, AES, DES3
import binascii


class


WFA1gorithm(ABC):
def_init__(self,key:str, mode:Blowfish.MODE_ECB-Blowfish.MODE_ECB,block_size:int=16):
self.key = self.setkey(key)
self.mode = mode
self.block_size block_size
self.cipher None
self.padChar:int - 10
self. .minSize:int
1E
P
self


.init(


@abstractmethod
def init(self):
pass


def setKey(self,key:str):
# convert bytes
key = key.encode('utf-8")
return binascii.unhexlify(key)


def encrypt(self,message:str)->str:
#padding as per block size
bs- self.block_size
if self.minSize != 0 and len(message) < self.minSize:
bs = self.minSize
pad - lambda s: s + ( bs- len(s) % bs) * chr(self. padChar)
message=pad(message)
# convert to bytes
byte_array = message.encode("UTF-8")


# now encrypt the padded bytes
encrypted - self.cipher.encrypt(byte_array)
base64 encode and convert back to string
return encrypted.hex().upper()


def decrypt(self,message:str)->str:
# convert the message to bytes
byte_array = message.encode("utf-8")
message - binascii.unhexlify(byte_array)
# decrypt and decode
de=self.cipher.decrypt(message)
#print(f'key=(self.key)---de:[de)')
decrypted = de.decode()
#strip all new line chars which are added as part of padding
return decrypted.strip("In").strip(chr(8))


class WFBlowfish(WFAlgorithm):
def init(self,key:str, mode:Blowfish.MODE_ECB-Blowfish.MODE_ECB,block_size:int=Blowfish.block_size):
super().init(key, mode, Blowfish.block_size)
def init(self):
# new instance of AES with encoded key
self.cipher = Blowfish.new(self.key, self.mode)


class WFAES(WFAlgorithm):
def _init_(self,key:str, mode:AES.MODE_ECB=AES.MODE_ECB,block_size:int=16):
super().init_(key, mode, block_size)


def init(self):
# new instance of AES with encoded key
self.cipher = AES.new(self.key, self.mode)


class WFDES3(WFAlgorithm):
def _ini _(self, key:str, mode:DES3. MODE_ECB=DES3. MODE ECB, block- size: int-DES3. block_size):

super().init(key, mode, block_size)


def init(self):
# new instance of AES with encoded key
self.cipher = DES3.new(self.key, self.mode)
self. padChar = 
8


self.minSize = 24
