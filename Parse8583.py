import binascii
import datetime
import decimal
import logging
import re
import struct
import sys


from iso.bitarray import BitArray
from iso.IS08583parser import Iso8583DataError, panMask
from iso.isofield import ISOFieldManager


LOGGER= logging.getLogger(_name)
DEFAULT_ENCODING = 'cp500


class IS08583:


def _init_(self, iso_config, encoding-None) -> None:
self.iso_config = iso_config
if not encoding:
self.encoding = DEFAULT_ENCODING


else:


self.encoding = encoding


if not iso_config:

raise Exception('iso_config not provided')
def tolsgBytes(self, obj: dict) -> bytes:
return self.


dictToBytesMessage(obj)


def toMsgFields(self, bMsg: bytes) -> dict:
return self


bytesToDictMessage(bMsg)


def _bytesToDictMessage(self, message:bytes) -> dict:


bit_config - self.iso_config
encoding=self.encoding


LOGGER.debug("Processing message: len=%s contents:\n%s", len(message), message)
message_type_indicator = message[:2]
message - message[2:]
primaryBits = message[:8]
message = message[8:]
bitmap_list = self._get _bitmap_list(primaryBits)
secondayBits=b'
if bitmap_list[1]==True:
secondayBits = message[:8]
message - message[8:]
bitmap_listSec = self. _get_bitmap_list (secondayBits)
b=bitmap_listSec.pop(0)
bitmap_list[0]-bitmap_list[0]+b
bitmap_list.extend(bitmap_listSec)
LOGGER.debug("Bitmap: %s"


bitmap_list)


message_data-message


return_values = dict()


# add the message type
try:


return_values["MTI"] = message_type_indicator.decode(encoding)
except UnicodeError as ex:
raise Iso8583DataError("Failed decoding MTI field', binary_context_data-message, original_exception=ex)


message. pointer
◦


no_of_bits=len(bitmap_list)-1


for bit in range(2, no_of_bits):
if bitmap_list[bit]:
LOGGER.debug("processing bit %s: %s", bit, message_data)


fld_config-bit_config[str(bit)]
return_message, message_data = ISOFieldManager.unpack(str(bit), message_data, fld_config)
LOGGER.debug("bit % value: %s", bit, return_message
return_values.update(return_message)


return return_values


def


dictToBytesMessage(self, message) -> bytes:


bit_config - self.iso_config
encoding=self.encoding


output_data - b''
bitmap_values
[False] * 128
bitmap_values[0] = True
get the pds fields from config
#
de_pds_fields = sorted(
[int(key) for key in bit_config if bit_config[key].get("processor") -- "PDS"], reverse-True)
LOGGER. debug(de_pds_fields)
for de_field_value in self._pds_to_de(message):
de_field_key - de_pds_fields.pop()
LOGGER. debug(f'de(de_field_key)=[de_field_value)')
message[f"DE(de_field_key)'] - de_field_value
lastbit-0
for bit in range(2, 128):
if message.get('DE' + str(bit)) or message.get('DE' + str(bit)) =-0: # 0 evals to false, allow zero values
lastbit = bit
LOGGER.debug(f'processing bit (bit)")
bitmap_values[bit - 1] = True
LOGGER.debug(message.get('DE' + str(bit)))
fld_config=bit_config[str(bit)]
isSubFieldPack = True if fld_config.get("class')--"SUBFIELD_PACK" else False
if isSubfieldPack:
#DE126_SUBFLDS
subMessage = message.get(DE' + str(bit) + "_SUBFLDS')
sub_fld_config = fld_config.get('fields")
fldVal = self._dict_SubField_iso8583(subMessage, sub_fld_config, encoding)
b=bytearray(1)
b[0]=1en(fldVal)


output_data +- binascii.hexlify(b) + fldVal
else:
output_data += self._field_to_iso8583(
fld_config,
message.get('DE' + str(bit)).
encoding-encoding)


if lastbit < 65:


bitmap_values = bitmap_values[:64]


bitmap_values[0]=False


bitarray - BitArray()
bitarray.fromlist(bitmap_values)
binary_bitmap = bitarray.tobytes()
bitmap = binascii.hexlify(binary_bitmap)


mti = message['MTI"].encode(encoding) if message.get("MTI') else b'
output_string mti + bitmap + output_data
return output_string
def _field_to_iso8583(self, bit_config, field_value, encoding-DEFAULT_ENCODING):


output
b'.
LOGGER.debug(f"bit_config-(bit_config), field_value=(field_value), encoding-(encoding)')


field_value = self._pytype_to_string(field_value, bit_config)
field_length bit_config.get("length')


field_type
bit_config['type"]


length_size = self._get_field_length(bit_config) # size of length for llvar and 11lvar fields


if length_size > 0:
field_length = len(field_value)
b=bytearray(1)
b[0]=field_length
if "LLHBINARY' in field_type:
i- int(field_length / 2)
b[e]=i
LOGGER.debug(f"field_length=(field_length), blen-(b), hexlen-(binascii.hexlify(b))")
output +- binascii.hexlify(b)
#else:
tt
output
+E
format(field length, '0"
str(length_size))


encode (encoding)


if isinstance(field_value, bytes):
output += field_value[:field_length]
else:
if 'IsHex' in bit_config:
b=bytearray(field_value,bit_config['IsHex'])
output +-binascii.hexlify(b)
else:
output
"


format (field value[:field length].
+ str(field_length)).encode(encoding)


return output
def


_iso8583_to_field(self, bit, bit_config, message_data, encoding-DEFAULT_ENCODING):


field_length bit_config['length']


ISOFieldManager.unpack(message_data, bit_config)


LOGGER.debug(f"_iso8583_to_field: bit_config=(bit_config), field_value-(message_data), field_length=(field_length)")


field_data
message_data[length_size:length_size


field_length]


LOGGER.debug(f`field_data=(field_data)')
field_processor
bit_config.get("processor")


forSubFld_data = field_data
#do ascii conversion except for ICC field
if field_processor != "ICC':
try:


if 'IsHex' not in bit_config:
field_data
field_data.decode(encoding)
else:
b=binascii.unhexlify(field_data)
field_data
b.decode(bit_config["IsHex"])


except UnicodeDecodeError as ex:
raise Iso8583DataError(f'Unable to decode DEfbit) field value'
binary_context_data-message_data, original exception=ex)


# if field is PAN type, panMask the card value
if field_processor == 'PAN':
field_data
panMask(field_data)


#do field conversion to native python type
try:
field_data
self._string_to_pytype(field_data, bit_config)
except ValueError as ex:
raise Iso8583DataError(f'Unable to convert DE(bit) field to python type
binary_context_data=message_data, original exception=ex)
return_values
dict()
#add value to return dictionary
return_values["DE" + str(bit)] = field_data


# if a PDS field, break it down again and add to results
if field_processor -= 'PDS':
return_values.update(self._pds_to_dict(field_data))


#if a DE43 field, break in down again and add to results
if, field_processor 'DE43":
processor_config - bit_config.get("field_processor_config")
return_values.update(self._get_de43_fields(field_data, processor_config))


if .SUBFIELD_PACK" == bit_config[ 'class' ]:
return_values["DE" +str(bit) + "_SUBFLDS"] - self._iso8583 SubField_dict(bit, forSubFld_data, bit_config-bit_config["fields"].


return return_values, field_length + length_size


def _pan_prefix(self, field_data):


BR


Get prefix of PAN


return field_data[:9]


def_get_field_length(self, bit_config):


Determine length of iso8583 style field


:param bit_config: dictionary of bit config data
:return: length of field


length_size=0


fType
bit_config['type']
if fType == "LLVAR" or fType=="LLHNUM":
length_size
= 1


elif fType == "LLHEXVAR" or fType=="LLHECHAR":
length_size 1
elif fType=="LLHCHAR":
length_size
1


elif fType == "LLLVAR":
Jength_size
= 1


elif fType == "LLHBINARY"
length_size
1


return length_size


def _get_bitmap_list(self,binary_bitmap, endian='big'):


Get list of bits from binary bitmap


:param binary_bitmap: the binary bitmap to be returned
:return: the list containing bit values. Bit 0 contains original binary bitmap


working_bitmap_list BitArray(endian)
working_bitmap_list.frombytes(binary_bitmap)


original binary bitmap
#
Add bit
->
bitmap_list [binary_bitmap]


add bits from bitmap


bitmap_1ist.extend(working_bitmap_list.tolist())


return bitmap_list


def _pds_to de(self, dict_values):


"""
takes all the pds fields values in dict (PDSxxxx) and creates list of DE strings

:param dict_values: dict containing "PDSxxxx" elements
:return: list of byte strings containing pds data, or None if no fields
"""
LOGGER.debug(f"dict_values=(dict_values)')
keys- sorted([key for key in dict_values if key.startswith("PDS')])
LOGGER.debug(f"keys=fkeys)')
output
outputs = []
for key in keys:
tag = int(key[3:])
LOGGER. debug(f"tag-(tag)')
length - len(dict_values[key])
add_output = f'(tag:04)/length:03)(dict_values[key])
if len(output + add_output) > 999:
outputs.append(output)
output
=


output += add_output
if output:
outputs.append(output)
LOGGER.debug(f">pds2de: foutputs)')


return outputs


def _pds_to_dict(self, field_data):
field_pointer ⁃
return_values = )


while field_pointer < len(field_data):
# get the pds tag id


pds_field_tag = field_data[field_pointer:field_pointer+4]
LOGGER.debug("pds_field_tag=[%s]", pds_field_tag)


# get the pds length
pds_field_length = int(field_data[field_pointer+4:field_pointer+7])
LOGGER.debug("pds_field_length-[%i]", pds_field_length)


# get the pds data
pds_field_data = field_data[field_pointer+7:field_pointer+7+pds_field_length]
LOGGER.debug("pds_field_data=[%s]", str(pds_field_data))
return_values["PDS" + pds_field_tag] = pds_field_data


# increment the fieldPointer
field_pointer += 7+pds_field_length


return return_values


def_get_de43_fields(self, de43_field, processor_config-None):

"""
get pds 43 field breakdown


:param de43_field: data of pds 43
:return: dictionary of pds 43 sub elements
"""

LOGGER.debug(f"de43_field=(de43_field)
processor: (processor_config)")
field_dict = dict()
field_dict["DE43.1"]=de43_field[:25]
field_dict["DE43.2"]-de43_fie1d[25:38]
field_dict["DE43.3"]-de43_field[38:40]
return field_dict
ief _iso8583_SubField_dict(self, perentBit,message, bit_config, encoding=DEFAULT_ENCODING, maxSubFields-19):


LOGGER.debug("In\nSubfields(%s) Processing message: len-%s contents:\n%s",perentBit, len(message), message)


try:


message_length = len(message)-16
binary _bitmap, message_data = struct.unpack(
"16s" + str (message_length)
"s", message)
+
except struct.error as ex:


raise Iso8583DataError('Subfields Failed unpacking bitmap values', binary_context_data-message, original_exception=ex)
return_values = dict()


message_pointer =
#bitmap_list - _get_bitmap_list(binary_bitmap, endian="little')


str1="f'(0x"+str(binary_bitmap)[2:18]+":0>64b)'"
str1= '0'+eval(str1)


LOGGER.debug(f'Subfields bitmaplist: [stri)")
for bit in range(0, maxSubFields):
if strl[bit]=='1":
LOGGER.debug("Subfields processing bit %s", bit)
return message, messageincrement
self._iso8583_to_field(
bit,
bit_config[str(bit)],
message_data[message_pointer:].
encoding)


#
Increment the message pointer and process next field
message_pointer += message_increment
return_values.update(return_message)
if message_pointer != len(message_data):
raise Iso8583DataError(
f'Subfields Message data not correct length.
f'Bitmap indicates len-(message_pointer), message is len=flen(message_data))"
binary_context_data=message


return return_values


def _dict_SubField_iso8583(self,
encoding-self.encoding
output_data = b',
bitmap_values = [False] * 64


message, bit_config, maxSubFields-19):


# get the pds fields from config
de_pds, fields
sorted(


[int(key) for key in bit_config if bit config[key] get("processor"
LOGER. debug(de_Pds_fields)


"


"PDS'], reverse=True)


for de_field_value in self._pds_to_de(message):
de_field_key = de_pds_fields.pop()
LOGGER.debug(f'defde_field_key)=fde_field_value)')
message[f'DE(de_field_key)'] = de_field_value
for bit in range(1, maxSubFields):
if message.get('DE' + str(bit)) or message.get("DE' + str(bit)) =- 0: # 0 evals to false, allow zero values
LOGGER.debug(f'processing sub bit (bit)')
bitmap_values[bit - 1] = True
LOGGER.debug(message.get("DE' + str(bit)))
output_data + self._field_to_iso8583(
bit_config[str(bit)],
message.get('DE" + str(bit))
encoding=encoding)


bitarray = BitArray()
bitarray.fromlist(bitmap_values)
binary_bitmap = bitarray.tobytes()
if hex_bitmap:
bitmap = binascii.hexlify(binary_bitmap)
else:
bitmap = binary_bitmap


output_string - bitmap + output_data
return output_string
