from pathlib import Path
import sys


#print("rest", str(Path(file_).resolve().parent.parent))
sys.path.append(str(Path(file).resolve().parent.parent))
from iso.IS08583parser import pack, unpack
from iso.spec import WFISOConfigSpec as wfISOspec
# from iso.parse8583 import IS08583
#from iso.wf_tsys_spec import AuthSPEC
import pprint
import binascii
import logging
LOG = logging.getLogger(_name_)
logging.getlogger().setlevel(logging.DEBUG)
logging.getLogger(.addHandler(logging.StreamHandler(sys.stdout))


pu = 3
bB - b'Ix01\x00\xf25tlx811t\xe@\x8@lx00lx001x001x001x001x0@1x001x001x04\x10EVMAVt!Hilx@0\x00\x00lx001x0glx00lx00\x99 \x001x08 \x06\x12\x00\x00lx00 \x08 \x12#1x067B\x08&lx08


if pu & 1 == 1:
isoMsg ('MTI': "0100", 'DE2": "4576224109214869", 'DE3': "000000", "DE4": "000000009900", "DE7':


"0806129000 ", 'DE11 ": "000812"
DE14': "2306', "DE18': "3742', "DE19': '0826', "DE20": "0840', "DE22": '0120', 'DE25": "08', "DE32": "493488", "DE37": "224300021957
DE40': '101', 'DE41": '98123456", 'DE42": "99999999999999 ", "DE43": 'Test DE42 Arizona
DE49": '0840", 'DE126": '0040000000000000f1f040f6f7f5", 'DE126_SUBFLDS': ("DE10": "10 675')
}
bB= pack(isoMsg, iso_config-wfISOspec, hex_bitmap=True)
bh AXx16\ X01 \X02 \ X00 \X00 \ X00 1 X01\X00 \x00 1X00\XA@ \x0O1XO\X06\x0@\x0@1x@\.x06\x0@1xØØ1x@Ə\x00"
print(f"packed data in hex: len=(len(bB)):", bB)
bB - binascii.unhexlify(bB)
print(f"packed data bytes:len=(len(bB)):", bB)
tL=len(bB)+22
print(f"Sending data of length ftL)", type(tL))
if pu & 2--2:
hexArray = binascii.hexlify(bB)
hexArray100-b'0100f224748109e0800000000000000000041045762241092148690000000000000099000806120000000812230637420826084001200806493488f2f2f4f3f0føf0f2f1f9f5f7f1
#isoMsg = unpack(hexArray100,iso_config=wfISOspec, hex_bitmap=True)
1exArrya400-b .0400722464810cc08010105532546938642194000000000000000200071609502600000117033743025001205906493488f2f2f4f3f0fefef2f1f9#5f7f0foførererorererefefe
rexArrya120=b'0120F22474810F E0800000000000040000001055325469386421940000000000000000000806120000000001170337420826084001200806493488F2F2F4F3FOFOFOF2F1F9F5F7F1M


'es110-b ' 0110F22474810BF0800000000000040000001056000033315612340000000000000005000808110000000812080130010826084001200806493488F2F2F4F3F0FOF0F2F1F9F5F7FOF0F1F0
rea100-b '0100F224748109E0800000000000000000041056900099998777890000000000000005000808110000000812080830010826084001200806493488F2F2F4F3F0F0F0F2F1F9F5F7F1FOF1F9F
reqMsg = unpack(req100,iso_config=wfISOspec, hex_bitmap=True)
resMsg unpack(res110,iso_config=wfIS0spec, hex_bitmap=True)
pprint.pprint(reqMsg, indent=4, depth=2)
pprint.pprint(resMsg, indent=4, depth=2)





F1f0f1f9f8f1f2f3f4f5f6f9f9f9f9f9f9f9f9f9f9f9f9f9f940e385a2a340c4c5f4f240404040404040404040404040404040c19989a9969581404040404040e4e208401c0040000000000000f1f040f6f7f5


If0f0f0f7f9f9f9f9f9f9f9f9f9f9f9f9f9f9400554055100000005
F1F 2F 3F4F5F 6F0F5F1F0F 1F0F0F0F8F 1F14040F9F9F9F9F9F9F9F9F9F9F9F9F9F940D781A8D7819340404040404040404040404040404040404040C19989A9969581404040404040E4E2000010FSFSF3F2F5F4F6F9F3F8F6F4F2F1F


LF 0F 1F9F 8F1F2F 3F 4F5F6F9F 9F 9F9F9F9F9F 9F9F9F9F9F9F940D781A8D7819340404040404040404040404040404040404040C19989A9969581404040404040E4E20BF5404040404040404040D4097810F5F6F0F0F0F0F9F9F9F9F8H
1F9F 8F1F 2F 3F4F5F6F9F9F9F9F9F9F9F9F9F9F9F9F9F940D781A8D7819340404040404040404040404040404040404040C19989A9969581404040404040E4E209780E0040000000000000F1F040F2F1F3
