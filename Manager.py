from cryptors.algorithms import WFAES, WFAlgorithm, WFBlowfish, HFDES3
from enum import Enum
import threading


class Algorithm(Enum):
AES = 1
DES = २
BLOWFISH
m
=
DES3 = 4
Unknown- 99


class WFCrypto:
def _init(self, algtm: Algorithm, key:str) -> None:
self.Algtm:Algorithm = algtm
self.key
key
self.crypto:WFAlgorithm = None


if self.Algtm == Algorithm.AES:
self.crypto = WFAES(self.key)
elif self.Algtm == Algorithm.BLOWFISH:
self.crypto = WFBlowfish(self.key)
elif self.Algtm == Algorithm.DES or self.Algtm == Algorithm.DES3:
self.crypto = WFDES3(self.key)
else:
raise NotImplementedError("Algorithm not implemented")
def encrypt(self, message:str):


return self.crypto.encrypt(message)


def decrypt(self, message:str):


return self.crypto.decrypt(message)
class CryptoManager:
__dictCryptos:dict = dict()
__lock = threading.Lock ()


@staticmethod


def getCripto(algtm:Algorithm, key:str):
dKey = str(algtm)+":"+key
cpt= CryptoManager.__dict@ryptos.get(dKey)
if cpt:


return cpt


CryptoManager.__lock.acquire()
try:
cpt = WFCrypto(algtm, key)
CryptoManager._dictCryptos[dKey]=cpt
finally:
CryptoManager.__lock.release()
return cpt
