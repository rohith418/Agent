import arena se
100 t sys
from cryptors manager import Algorithm, CryptoManager
name
mainly
parser = areparse ArgumentParser description Use this for encrypt/decrypt based on Algorithm "des", HOES/Des3:; "BLOWFISH',
Either -en/-de arguments alone with a and k requiredin
parser add argument( 6, below algorithm ("AS", BESIDES3"; "BLOWFISH"', required-True)
parser and argument( -K, help. Hash key supporting your Algorithm required-True)
parser add argument on, help- Encrypt plantext (-en "your text heresy')
parser, add argument de', help Decrypt your encrypted string fade "your encrypted hash here"")
arg5 = parser parse ares()
#print (a es)
of - Algorithm Unknown
try:
01 = Algorithmlares. a upper(). strip()]
except Exception as ..
print( Invalid Algorithm 1851. only accepted are RESIDES/DE53/BLOWFISH7 8 ames. 8)
If ares.K == None or 1enlarge.K) < so
print/"Invalid key, should be of man 8")
SYS exit
if (args.en == None or len(args.en) == 0) and (args.de ==None or len(args.de)--0)
print("Either encrypt or decrypt should be called using -en <plaintext> or -de <hash code here>"
sys.exit()


if args.en:
msg= CryptoManager.getCripto(al, args.k).encrypt(args.en)
print('Encrypted : %s to "%s"" % (args.en, msg))


if args.de:
msg= CryptoManager.getcripto(al, args.k).decrypt(args.de)
print('Decrypted : %s to "s"" % (args.de, msg))


print("Blowfish Test")
key -'ce0413c2c0840c5c5563fae7bad1d54a
bf- WFBlowfish(key)
plaintext - 'QHX_7szKVr8Nrdgt
en bf.encrypt(plaintext)
print("Encrypted: ", en)
msg = bf.decrypt(en)
print("Decrypted 1: %s to
%s." %
(en, msB))
en= 'D7FB6BA713C42505CC95C9D6B2457AD5129411ED2568B8E1
msg= bf.decrypt(en)
print("Decrypted 2: %s to %s." % (en, msg)
print("AES Test")
message
I


foobar2foobar2
AES_pkcs5_obj = WFAES(secret_key)
secret_key - "EB90524E2C60CA1412D54D75D52B4BEB"


print("Encripted: ", encrypted_message)
encrypted_message = AES_pkcs5_obj.encrypt(message)
#decrypted_message = AES_pkcs5_obj.decrypt(encrypted_message)
print("vf-pwd", len(decrypted_message), decrypted_message)
decrypted_message = AES_pkcs5_obj.decrypt("B6B56155979A2C00AA753E3B97AB2123")
print("mypwd", len(decrypted_message), decrypted message)
decrypted_message = AES_pkcs5_obj.decrypt(encrypted_message)
##

"""
print("DES3 Test")
key -"9b7fe98067769ddc25e316fb4c135e43f47f795b7370c86d
plaintext - '4808012956919618
bf= WFDES3(key)
en bf.encrypt(plaintext)
print("Encrypted: ", en)
msg= bf.decrypt(en)
print("Decrypted 1: %s to %s." % (en, msg))
en-'85F7862D7501DFD543F 210AE33DA0D7E06AECAACBF297B80
msg= bf.decrypt(en)
print("Decrypted 2: %s to %s." *[(en, msg))
"""
