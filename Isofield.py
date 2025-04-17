from abc import ABC, abstractmethod
impgrt logging


LOGGER = logging.getLogger(name)


class ISOField(ABC):
CHAR_ENCODING:str - 'cp500
BIN_ENCODING:str- 'cp500


def _init(self, endcoing=CHAR_ENCODING) -> None:
self.encoding = endcoing


def padRight(self, value:any, pad, maxLen:int)->any:


retVal
value


for i in range(maxLen - len(value)):
retVal+=pad


return retVal


def unpadRight(self, value:any, pad)->any:


retVal
value


for i in reversed(range(len(value))):
if retval[i] == pad:
retVal retVal[:i]
else:
break


return retVal


def decodelength(self, b:bytes, varLen:int) ->int:
##TODO - This below logic can be looped
1:int=0
if varLen=-1:
1=(b[0] & OxF)
elif varLen
2:


1=(b[0] & 0xF) * 10 + (b[1] & 0xF)
elif varLen -- 3:
1-(b[0] & 0xF) * 100 + (b[1] & 0xF) * 10 + (b[2] & 0XF)
elif varLen = 4:
1=(b[0] & 0xF) * 1000 + (b[1] & 0xF) * 100 + (b[2] & 0xF) * 10 + (b[3] & 0xF)


return l


def encodelength(self, l:int, varlen:int)->bytes:
##TODO- This below logic can be looped
b-bytes ()
if varLen=-1:
b-bytes([1])
elif varLen == 2:
b=bytes([int(1/10),(1%10)])
elif varLen = 3:
b=bytes([int(1/100),int(1%100/10),(1%10)])
elif varLen
== 4:


b-bytes([int(1/1000),int(1%1000/100),int(1%100/10),(1%10)])


return b


@abstractmethod


def pack(self, value: any, name:str, length:int, pad:any-None, varLength:int-0) "> bytes:


pass
@abstractmethod
def unpack(self, value: bytes, name:str, length:int, pad:any=None, varLength:int-0) -> tuple[dict, bytes]:
pass


@abstractmethod
def unpack(self, value: bytes, fldConfig:dict) -> tuple[dict, bytes]:


pass


class ISOFieldFix(ISOField):
def _init_(self, endcoing=ISOField.CHAR_ENCODING) -> None:
super(.init(endcoing=endcoing)


def pack(self, value: any, name:str, length:int, pad:any=None, varLength:int=0) -> bytes:


if len(value) > length :
raise Exception(f"Field ((name)) data is longer than max length((length))")


if pad is not None:
value- self.padRight(value, pad, length)


return bytearray(value, self.encoding)
def unpack(self, value: bytes, name str Length.int, pad:any-None, vorlength Into )-, tuple dick, bytes].
retVal = {}
If len(value) < length;
raise Exception field (name)) data is shorter than expected length(lengthy, '
D= velvet: Length?
If pad Is not None:
V = self unpackagh.(v, pads
Vs, V decode(self encoding)
retro1[name] = v
return (reval, valvelength:])
def unpack(self, valve: bytes, Floconfig diet) > tuple diet, bytes]:
name strafedconfig get name's
length.int .int(f10confident( Length:))
Strip = ftdconfig get It')
god - 4ldconfig get ('pod')
reeva1 = ft
If len(value) < length.
raise Exceptionif field ((name) data is shorter than expected length((lengthy)")
V = Value[: Length]
If pad is not None
v = self unpaidRight (v, pod)
v-v. decode(self encoding)
retail DE' - StrID] =
return (retro1, valve[length:])
Class 1508Infield41×( ISOFieldFax):
- that (SELF) -> None:
super).. init (endearing. ISOField. BIN ENCODING)
Class ISOFieldvar (ISOField):
def init (self, endearing. ISOfield CHAR ENCODING)
super(). Init (ending endcoins)
def pack self, valve: am, name st.. Length.int, had any-one, varlength Into)
If (Jen(value) + varLength), Length
raise Exception( Field ((name) data is longer than max Length((Lengthy))
by bytco no) (Valve, self encoding)
I ten(by)
bestIf encodelength(1, vorlengths
do not by
def unpack(self, valve: bytes, name str, length Int, pad any-more, vorlength Into8) I tuple diet, bytes)
retval ={}
if len(value) < varLength:
raise Exception(f"Field ([name)) data is shorter than min expected length((varLength))")


l= self.decodeLength(value, varlength)
value = value[varLength:]
if len(value) < I or I > length:
raise Exception(f"Field ((name)) data is shorter than min expected length(tl))")


value[:1]
remainvalue-value[l:]


v=v.decode(self.encoding)
retVal[name] = remainValue


return (retVal,value)


def unpack(self, value: bytes, fldConfig:dict) -> tuple[dict, bytes]:
name:str = fldConfig.get('name')
length:int = int(fldConfig.get("length'))
fldType:str = fidConfig.get('type')
fldProcessor = fldConfig.get('processor')
strID = fldConfig.get(id")
fldParser, varLength= ISOFieldManager.getParser(fldType)
retVal ={}
if len(value) < varLength:
raise Exception(f"Field ((name)) data is shorter than min expected length((varLength))")


l= self.decodeLength(value, varLength)


value = value[varLength:]
if len(value)
< 1 or  1 >

length:
raise Exception(f"Field (fname)) data is shorter than min expected length((l))")


field_data = value[:1]
remainValue-value[l:]


if a PDS field, break it down again and
#
add to results
if fldProcessor == 'PDS':
retVal.update(["PDS_'+ strID : ISOFieldManager.Pds


to_dict(field_data)))


v-field_ data.decode(self.encoding)
retVal[ 'DE + strID]
EV


return (retVal,remainValue)


class ISOCharFieldVar(ISOFieldVar):
def init_(self) -> None:
super().init_(endcoing= ISOField.CHAR_ENCODING)


pass

class ISOBinFieldVar(ISOFieldVar):
def init(self) -> None:
super(._init(endcoing= ISOField.BIN_ENCODING)


pass


class PDSField(ISOField);
def _init(self) -> None:


super(.init_(endcoing- ISOField.BIN_ENCODING)


pass


class ISOFieldManager:
binVarParser = ISOBinFieldVan(
binFixParser = ISOBinFieldFix(
chrVarParser= IS0CharFieldVar()
chrFixParser = ISOCharFieldFix()


@staticmethod
def getParser (fldType:str)-> tuple[ISOField, int]:
match fldType:
case "LLL_EBC_CHART
return (ISOFieldManager.__chrVarParser, 3)
case 'LL_EBC_CHAR"
..


return (ISOFieldManager. _chrVarParser,
2)
case "CHAR_FIXED".
return (ISOFielanager chrFixParser.
0)
case "LL_CHAR":
return (ISOFieldManager.__chrVarParser.
2)
case "EBC_CHR_FIXED";
return (ISOFieldManager._chrFixParser,
case "LLL_BINARY":
0)
return (ISOFieldManager.__binVarParser.
3)
case "LL_BINARY"
return (ISOFieldManager._binVarParser.
case "BIN_FIXED"
2)
return (ISOFieldManager.__binFixParser,
0)
case _:
return (ISOFieldManager


binFixParser, 0)


@staticmethod


def unpack(bit, value: bytes, fldConfig:dict) -> tuple[dict, bytes]:
fldConfig['id']= bit
# name:str = fldConfig.get("name")
#length:int = int(fldConfig.get("length'))
fldType:str- fldConfig.get("type")
# pad = fldConfig.get("pad')


fldParser, varLength= ISOFieldManager.getParser(fldType)
return fldParser .unpack(value
fldConfig


estaticmethod


def pack(bit, value: any, fldConfig:dict) -> bytes:
fldConfig["id']= bit
name:str - fldConfig.get("name
length:int = int(fldConfig.get("length"))
fldType:str= fldConfig.get("type")
pad = fldConfig.get("pad')


fldParser, varLength = ISOFieldManager .getParser (fldType)
return fldParser.unpack(value, name, length, pad=pad, varLength=varLength)


@staticmethod


def pds_to_de(dict_values)


takes all the pds fields values in dict (PDSxxxx) and creates list of DE strings


:param dict_values: dict containing "PDSxxxx" elements
:return: list of byte strings containing pds data, or None if no fields


get the PDS field keys in order
#
LOGGER.debug(f"dict_values=(dict_values)')
keys- sorted([key for key in dict_values if key.startswith("PDS')])
LOGGER.debug(f'keys-(keys>')
output = ' '
outputs
Il
[]


for key in keys:
tag = int(key[3:])
LOGGER debug(f'tag=(tag)')
length - len(dict_values[key])
add_output = f'ftag:04)flength:03)(dict_values[key]]
if len(output + add_output) > 999:
outputs.append(output)
output
II


output += add_output
if output:
outputs. append (output)
LOGGER.debug(f">pds2de: (outputs)')


return outputs


estaticmethod
def pds_to_dict(field_data):
field_pointer
0


return_values = ()


while field_pointer < len(field_data):
# get the pds tag id
pds_field_tag = field_data[field_pointer:field_pointer+4]
fieldNo = (pds_field_tag[0] & 0xF) * 1000 + (pds_field_tag[1] & OxF)
LOGGER.debug("pds_field_tag-[%s]", fieldNo)


100 + (pds_field_tag[2] & OxF) * 10 + (pds_field_tag[3] & 0xF)


# get the pds length
pds_field_length - field_data[field_pointer+4:field_pointer+7]
pdsLen - (pds_field_length[0] & 0xF) * 100 * (pds_field_length[1] & 0xF) * 10 + (pds_field_length[2] & 0xF)
LOGGER.debug("pds_field_length=[%i]", pdsLen)


# get the pds data
pds_field_data - field_data[field_pointer+7:field_pointer+7+pdsLen]
LOGGER.debug("pds_field_data=[%s]", str(pds_field_data))
return_values["PDS" + str(fieldNo)] - pds_field_data.decode(ISOField.BIN_ENCODING)


# increment the fielaPointer
field_pointer +- 7+pdsLen


return return_values
