import os
from cryptors.keystore import KeyStore
from cryptors.manager import Algorithm, CryptoManager, WFCrypto
from util.config import Config


Raw


Blame


class WFCryptoutil:
"""Crypto Utility class which will hold singleton object and required keystore and algorithoms ready for encrypt and decryptions


_shared_instance = None
_agents:dict= dict()


def new(cls):
"""virtual private constructor"""
if cls._shared_instance is None:
cls.shared_instance = super()._new_(cls)


return cls._shared_instance


def initialize(self, ksConfig:Config):
file - ksConfig.get ("Cryptors", "KeystoreFile")
keyFilestorePwd = ksConfig.get("Cryptors", "KeyFileEncryptedPassword")
keyFileAlgorithm = ksConfig.get("Cryptors", "KeyFileAlgorithm")
enwariable = ksConfig.get("Cryptors", "KeyFileEncryptionKeyAvaiableInEnv")
ksFikeKey = os.environ.get(str(enwariable), "")
if ksFikeKey
""


raise EnvironmentError(f"Please configure environment variable for Keystore read Key: (envVariable)")
al = Algorithm[keyFileAlgorithm.upper().strip()]
keyFilestorePwd - CryptoManager.getCripto(al, ksFikeKey).decrypt(keyFilestorePwd)


k=KeyStore(file, keyFilestorePwd)
self._ks:keyStore = k


dbpasswordkey = ksConfig.get("Cryptors", "DBPasswordKey", "dbpasswordkey")
alg = ksConfig-get("Cryptors", "DBPasswordAlgorithm", "Blowfish")
dbpasswordkey = k.getKey(dbpasswordkey)
al= Algorithm[alg.upper(.strip()]
self._dbCryptor:WFCrypto = CryptoManager.getCripto(al, dbpasswordkey)


dataEnKey = ksConfig.get("Cryptors", "DataEncryptionKey", "desedekey")
alg= ksConfig.get("Cryptors", "DataEncryptAlgorithm", "DES")
dataEnKey = k.getKey(dataEnKey)
al - Algorithm[alg.upper().strip()]
self._dataCrydar:WFCrypto = CryptoManager getCripto(al, dataEnkey)
self.initDone:bool - True


eproperty
def Keystore(self):
if isinstance(self._ks, KeyStore):
return self._ks
else:


raise NotImplementedError("KeyStore not set, please call initialize(dict<key-config>) from main program first.")


@property
def DBPasswordCryptor (self) -> WFCrypto:
if not self.initDone:
raise NotImplementedError("KeyStore not set, please call initialize(dict<key-config>) from main program first.">
return self._dbCryptor


eproperty
def DataCryptor(self) -> WFCrypto:
if not self.initDone:
raise NotImplementedErnor("KeyStore not set, please call initialize(dict<key-config>) from main program first.")
return self._dataCryptor
