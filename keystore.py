import jks


class KeyStore:


def _init(self, storeFile:str, storePassword:str) -> None:
self.ks = jks.KeyStore.load(storeFile, storePassword)
self._certs:dict = dict(
self._seckeys:dict = dict()
self._load(


def __load(self):
self._certs.clear()
for alias, pk in self.ks.private_keys.items():
key = pk.pkey if pk.algorithm_oid == jks.util.RSA_ENCRYPTION_OID else pk.pkey_pkcs8
self._certs[pk.alias]
t


"privateKey": key.hex()
"cert_chain": []

}
certList=list()
for c in pk.cert_chain:
certList.append(t
"keyMan" : c[0],


"pubkey" : c[1] hex()


})


self._certs[pk.alias]["cert_chain"]=certList
self._seckeys.clear()


for alias, sk in self.ks.secret_keys.items():
self._secKeys[sk.alias]- f
"key": sk.key.hex(), #"".join("€:02x)".format (b) for b in bytearray(sk.key)"
"algorithm": sk.algorithm
"size": sk.key_size


#print(self._certs, self._seckeys)


def getkey(self, keyAlias:str) -> str:
""" Return key from available secure keys in the keystore
['keyalias': ("key': '1234567867769ddc25e316fb4c135e43f47f791234567890


jalgorithm.


E


DESede


"size ': 192}}


v=self._seckeys.get(keyAlias)
if v:

return v["key"]
else:
return None


def getCert(self, certAlias:str) -> any:
""" Return certificate as below format

{
'privateKey': '308202.
cert_chain': [("keyMan': "X.509", 'pubKey':
'3082024a308.....'}]
}
" " "
v=self._certs.get(certAlias)
if v:


return v
else:


return None


if _name_ == 
'main_':


file="C:\\Users\\u692495\NSourceCode\NOrbiscom\\KeyTest\\wells-fargo.keystore"
k=KeyStore(file,"foobar")


print("cert:",k.getCert("kSakey"))
print("getKey", k.getkey("dbpasswordkey"))
