import binascii
import datetime
import decimal
import logging
import re
import struct
import sys


from iso.bitarray import BitArray
from iso.util import panMask


LOGGER logging.getlogger(name_)
DEFAULT_ENCODING = 'latin_1


class IS08583BaseError (Exception):


binary_context_data = None
record_number = None
ex = None
def _init_(self, *args, **kwargs):
super(I508583BaseError, self).init_(*args)
if kwargs.get("record_number'):
self.record_number = kwargs['record_number']
if kwargs.get("binary_context_data'):
self.binary_context_data = kwargs['binary_context_data']
if kwargs.get("original_exception'):
self.ex kwargs['original_exception']


class Iso8583DataError (IS08583BaseError):
pass


def pack(obj: dict, encoding=None, iso_config=None, hex_bitmap=True)


if not encoding:
encoding
DEFAULT_ENCOD G
"


if not iso_config:
raise Iso8583DataError("Config iso spec is missing. Provide as iso_config parameter')


output - _dict_to_iso8583(obj, iso_config, encoding, hex_bitmap)
return output
def unpack(b: bytes, encoding=None, iso_config=None, hex_bitmap=True):


if not encoding:
encoding - DEFAULT_ENCODING
if not iso_config:
raise Iso8583DataError('Config iso spec is missing. Provide as iso_config parameter')


return _iso8583_to_dict(b, iso_config, encoding, hex_bitmap)


def _iso8583_to_dict (message, bit_config, encoding-DEFAULT_ENCODING, hex_bitmap=True):


LOGGER.debug("Processing message: len-%s contents:\n%s", len(message), message)
# split raw message into components MessageType(4B), Bitmap(16B)
# Message(l=*)


message_type_indicator = message[:4]
message = message[4:]
primaryBits - message[:16]
message = message[16:]
bitmap_list _get_bitmap_list(binascii.unhexlify(primaryBits))
secondayBits-b'
if bitmap_list[1]==True:
secondayBits = message[:16]
message=
message[16:]
bitmap_listSec _get_bitmap_list(binascii.unhexlify(secondayBits))
b=bitmap_listSec.pop(0)
bitmap_list[0]-bitmap_list[0]+b
bitmap_list.extend(bitmap_listSec)


message_data=message
# try:
# if hex_bitmap:
#


message_length = len(message)-36
message_type_indicator, bitmap, message_data struct.unpack(
"4532s" + str(message_length)
binary_bitmap = binascii.unhexlify(bitmap)
"s", message)


#


#


#


else:


#


message_length = len(message)-20
message_type_indicator, binary_bitmap, message_data = struct.unpack(
"4s16s" + str(message_length) + "s", message)
except struct.error as ex:
raise Iso8583DataError ("Failed unpacking bitmap values", binary context_data-message, original_exception=ex.
return_values dict ()
# add the message type
try:


return_values["MTI"] = message_type_indicator.decode(encoding)
except UnicodeError as ex:


raise I5o8583DataError('Failed decoding MTI field", binary_context_data-message, oniginal_exception=ex)


message_pointer = 0
#bitmap_list = _get_bitmap_list(binary_bitmap)
no_of_bits=len(bitmap_list)-1
LOGGER.debug(f'bitmaplist: (bitmap_list)")
for bit in range(2, no_of_bits):
if bitmap_list [bit]:
LOGGER. debug("processing bit %", bit)
return_message, message_increment = _iso8583_to_field(
bit,
bit_config[str(bit)],
message_data[message_pointer:],
encoding)


# Increment the message pointer and process next field
message_pointer += message_increment
return_values.update(return_message)
check that all of message has been consumed, otherwise raise exception
# if message_pointer != len(message_data)
#
raise Iso8583DataError (
#
f'Message data not correct length.
#
f'Bitmap indicates len=(message_pointer), message is len=flen(message_data))
#
binary_context_data=message


return return_values


def _dict_to_iso8583(message, bit_config, encoding-DEFAULT_ENCODING, hex_bitmap=True):


output data - b'


bitmap_values = [False] * 128
bitmap_values[0] True # set bit 1 on for presence of secondary bitmap


get the Pds fields from config
#
de_pds_fields - sorted(
[int(key) for key in bit_config if bit_config[key].get("field_processor') == "PDS"], reverse-True)
LOGGER. debug(de_pds_fields)
for de_field_value in _pds_to_de(message):
de_field_key - de_pds_fields.pop(
LOGGER.debug(f"de[de_field_key)=(de_field_value)')
message[f'DE[de_field_key)'] de_field_value


lastbit=0


for bit in range(2, 128):
if message.get('DE' + str(bit)) or message.get("DE' + str(bit)) =- 0: # 0 evals to false, allow zero values
lastbit = bit
LOGGER.debug(f"processing bit (bit)')
bitmap_values[bit - 1] = True
LOGGER.debug(message.get(DE"+ str(bit)))
fld_config-bit_config[str(bit)]
isSubFieldPack = True if fld_config.get(class')=="SUBFIELD_PACK" else False
if isSubFieldPack:
#DE126_SUBFLDS
subMessage= message.get("DE" + str(bit) +"_SUBFLDS")
sub_fld_config = fld_config.get ("fields"
fldVal - dict SubField_iso8583(subMessage, sub_fld_config, encoding, hex_bitmap-hex_bitmap)
b=bytearray(1)
b[0]-1en(fldVal)
output_data += binascii.hexlify(b)


x


fldVal


else:
output_data +- _field_to_iso8583(
fld_config,
message.get("DE"
str(bit)),encoding = encoding)
if lastbit < 65:
bitmap_values = bitmap_values[:64]
bitmap_values[0]=False


egeneratedata.com


bitarray = BitArray()
bitarray.fromlist(bitmap_values)
binary_bitmap = bitarray.tobytes()
bitmap = binascii.hexlify(binary_bitmap)


mti =,message['MTI"].encode(encoding) if message.get(MTI') else b"
output_string mti t bitmap + output_data
return output_string


def _field_to_iso8583(bit_config, field_value, encoding=DEFAULT_ENCODING)


output = b'
LOGGER.debug(f'bit_config=(bit_config), field_value=(field_value?, encoding=fencoding)


field_value =_pytype_to_string(field_value, bit_config)
field_length - bit_config.get("field_length')


field_type - bit_config["field_type']
length_size - _get_field_length(bit_config)


# size of length for llvar and lllvar fields
I Length sizes 0:
field Length - len(field valves
6 bytes ray (1)
0101-71010 length
IF 'LLHBINARY In field type:
1 = Int (field length /2)
6103 i
LARGER debug( field length-field Lengthy, bien-101, hexten-tofnasty nextifyou')
output to binascii heredity (6)
output to format field length, 01 + strength side)) encode (encoding)
It IsInstance (rte10 value, bytes)
output to field value field length
It IsHex In bat con 10.
-bytearray field valve, bit Comfier Istex:))
Output +-Dinas021 he 11107
else
output to format (field valve field length),'<' + str(field length)). encode(encoding)
return output
def _iso8583_to_field(bit, bit_config, message_data, encoding-DEFAULT_ENCODING)


field_length - bit_config["field_length]
field_type = bit_config['field_type']


length_size = _get_field_length(bit_config)


if length_size > 0:
field_length_string = message_data[:length_size]
try:


field_length_string = field_length_string.decode(encoding)
except UnicodeDecodeError as ex:
raise Iso8583DataError(f'Unable to decode DE(bit) field length'
binary_context_data=message_data, original lexception=ex)


try:
b=binascii.unhexlify(field_length_string)
field_length-int.from_bytes(b,'little")
#field_length - int(field_length_string)
except ValueError as ex:
raise Iso8583DataError(f"Invalid field length DE(bit)'
binary_context _data-message_data, original_exception-ex)


if 'IsHex' in bit_config or field_type== "BINARY" or field_type=="LLHBINARY"
field_length = field_length× 2
LOGGER.debug(f'_iso8583_to_field: bit_config-(bit_config), field_value=(message_data), field_length-(field_length)")


field_data = message_data[length_size: length_size + field_length]
#if 'IsHex' in bit_config:
#
b-binascii.unhexlify(field_data)
#
field_data = b.decode(cp500")


LOGGER. debug(f'field_data=[field_data)')
field_processor - bit_config.get("field_processor')


forSubFld_data = field_data
# do ascii conversion except for ICC field
if field_processor != "ICC:
try:
if 'IsHex' not in bit_config:
field_data = field_data.decode(encoding)
else:


b-binascii.unhexlify(field_data)
field_data - b.decode(bit_config['IsHex'])


except UnicodeDecodeError as ex:
raise Iso8583DataError(f'Unable to decode DE(bit) field value
binary_context_data-message_data, original_exception=ex)
# if field is PAN type, mask the card value
if field_processor -= 'PAN'
field_data panMask(field_data)


if field is PAN type, mask the card value
if field_ processor == PAN-PREFIX':
field_data -_pan_prefix(field_data)


# do field conversion to native python type
try:


field_data - _string_to_pytype(field_data, bit_config)
except ValueError as ex:
raise Iso8583DataError(f'Unable to convert DE(bit) field to python type
binary_context_data=message_data, original_exception-ex)
return_values = dict()


# add value to return dictionary
return_values["DE" + str(bit)] = field_data


# if a PDS field, break it down again and add to results
if field_processor == 'PDS':
return_values.update(_pds_to_dict(field_data))


# if a DE43 field, break in down again and add to results
if field_processor == 'DE43':
processor_config - bit_config.get("field_processor_config')
return_values.update(_get_de43_fields(field_data, processor_config))
# if ICC field, break into tags
if field_processor == "ICC":
return_values.update(_icc_to_dict(field_data))


if 'FIXED_SUBFIELD" =- bit_config['class']:
if 'IsHex' in bit_config:
b-binascii.unhexlify(forSubFld_data)
forSubFld_data = b.decode(bit_config['IsHex"])
subfls "
#return_values["DE" +str(bit) + "SUBFLDS"] = _iso8583_SubField_dict (bit, forSubFld data, bit_config-bit_config["fields"]
for key, fld in bit_config["fields"].items():
1= fld['field_length']
v=forSubFld_data[:1]
forSubFld_data = forSubFld_data[l:]
subfls['DE'+key]=v


return_values["DE" +str(bit) + "_SUBFLDS"] - subfls


elif 'SUBFIELD_PACK' == bit_config["class']:
return_values["DE" +str(bit) + "_SUBFLDS"] - _iso8583_SubField_dict (bit, forSubFld_data, bit_config-bit_config["fields"])


return return_values, field_length + length_size


def _pan_prefix(field_data):


Get prefix of PAN


return field_data[:9]
def _string_to_pytype(field_data, bit_config):


Field conversion to native python type


:param field_data: Data to be converted
:param bit_config: Configuration for bit
:return: data in required type


field_python_type - bit_config.get("field_python_type')
field_date_format bit_config.get("field_date_format', "%y%m%d")


if field_python_type in ("int", "long"):
field_data = int(field_data)
if field_python_type == "decimal":
field_data - decimal.Decimal(field_data)
if field_python_type "datetime":
field_data datetime.datetime.strptime(field_data, field_date_format)
return field_data


def _pytype_to_string(field_data, bit_config)

"""
convert py type to string for message
:param field_data: Data to be converted
:param bit_config: Configuration for bit
:return: data in required type


field_python_type = bit_config.get('field_python_type")
field_date_format - bit_config.get(field_date_format', "%yXm%d"


return_string - field_data
if field_python_type in ("int', "long'):
return_string - format(int(field_data), "0 + str(bit_config.get("field_length", 0))+ 'd'
if field_python_type == "decimal":
return_string = format(decimal.Decimal(field_data), '0' +str(bit_config.get(field_length' 0))+ 'f")

if field_python_type == "datetime":
if not isinstance(field_data, datetime.datetime):
field_data = _get_date_from_string(field_data)
return_string = format(field_data, field_date_format)
return return_string
def _get_date_from_string(field_data: str) -> datetime:


Parse string dates to python datetime object


Use dateutils library if it is installed, otherwise revert to simple parser
:param field_data: string containing date
: return: datetime object


try:
import dateutil.parser as parser
LOGGER.debug('Using dateutil parser')
return parser.parse(field_data)
except ImportError:
pass


if sys.version_info >= (3, 7):
LOGGER.debug('Using fromisoformat')
return datetime.datetime.fromisoformat(field_data)


# fallback parser -- tries a few different formats until one works
LOGGER.debug("Using built in date parser')
date_formats = ("%Y-%m-%d %H:%M1:%5", "%Y-%m-%d xH:XM", "%Y-%m-*d")
output_date = None
for date_format in date_formats:
try:

output_date = datetime.datetime.strptime(field_data, date_format)
break
except ValueError:
continue
if not output_date:
raise ValueError ("Unrecognised date string format - ()". format (field data))
return output_date


def _get_field_length(bit_config):


Determine length of iso8583 style field


:param bit_config: dictionary of bit config data
:return: length of field


nun


length_size


fType - bit_config['field_type"]


if fType -- "LLVAR" or fType--"LLHNUM"
length_size
2
elif fType == "LLHEXVAR" or" fType=="LLHECHAR":
length_size
2


4


elif fType=="LLHCHAR":
length_size F P
elif fType == "LLLVAR":
length_size = B
elif fType -- "LLHBINARY":
length_size
C


return length_size


def _get_bitmap_list(binary_bitmap, endian='big'):
working_bitmap_list = BitArray(endian)
working_bitmap_list.frombytes(binary_bitmap)


# Add bit 0 -> original binary bitmap
bitmap_list = [binary_bitmap]


# add bits from bitmap


bitmap_list.extend(working_bitmap_list.tolist())


return bitmap_list


def _pds_to_de(dict_values):
# get the PDS field keys in order
LOGGER.debug(f'dict_values=(dict_values)')
keys sorted([key for key in dict_values if key.startswith("PDS')])
LOGGER.debug(f'keys=(keys)")
output
outputs = []
for key in keys:
tag = int(key[3:])
LOGGER.debug(f'tag=(tag)')
length len(dict_values [key])
add_output
x ftag:04)flength:03)(dict_ values[key]]
if len(output + add_output) > 999:
outputs. append(output)
output =
output += add_output
if output:
outputs.append(output)
LOGGER.debug(f'>pds2de: foutputs)')


return outputs
def _pds_to_dict(field_data):


Get MasterCard pds fields from iso field


:param field_data: the IS08583 field containing pds fields
:return: dictionary of pds key values. Key in the form PDSxxxx where x is zero filled number of pds


field_pointer
= E
return_values =


while field_pointer < len(field_data):
# get the pds tag id
pds_field_tag - field_data[field_pointer:field_pointer+4]
LOGGER.debug("pds_field_tag=[%s]", pds_field_tag)
# get the pds length
pds_field_length = int(field_data[field_pointer+4:field_pointer+7])
LOGGER.debug("pds_field_length=[%i]", pds_field_length)
get the pds data
pds_field_data = field_data[field_pointer+7:field_pointer+7+pds_field_length]
LOGGER.debug("pds_field_data-[%s]", str(pds_field_data))
return_values["PDS"
pds_fiel tag]=
pds_field_data
# increment the fieldPointer
field_pointer +- 7+pds_field_length


return return_values


def _icc_to_dict(field_data):


Get de55 fields from message


:param field_data: the field containing de55
:return: dictionary of de55 key values
key is tag+tagid


TWO_BYTE_TAG_PREFIXES = [b'Ix9f"


b'Ix5f"]


field_pointer


IE


return_values ("ICC_DATA": binascii.b2a_hex(field_data).decode())


while field_pointer < len(field_data):
# get the tag id (one byte)
field_tag field_data[field_pointer:field_pointer+1]
# set to 2 bytes if 2 byte tag
if field_tag in TWO_BYTE_TAG_PREFIXES:
field_tag field_data[field_pointer:field_pointer+2]
field_pointer += 2
else
field pointer to 1
field the display = binascii. 62a her field top)
LOGGER debug( field toe display=rs", field top display)
I stop processing debs if low valves top found
If 71010 to display =- blog..
break
field length roll - field dotalfie1a pointer field pointer+19
field length = struct unpack 'SB", field Length row) 10)
LOGGER debug("85", format (field toe display))
LOGGER debelfield zeroth)
I get the tae date
de field data - field data field pointer+1 field pointer-field length+11
at 11010 data Display - inascii. 028 neale field data) decoded)
LOGGER GROVES As, de field data display)
return valves The - field top display upper() Decoder)) - be Field Data alsoplay
#Increment the fieldpointer
field pointer += 1+field_ length
return return_values


def _get_de43_fields(de43_field, processor_config=None):
LOGGER.debug(f"de43_field=(de43_field) , processor: [processor_config)")


#Udaya code
field_dict - dict()
field_dict["DE43.1"]-de43_field[:25]
field_dict["DE43.2"]-de43_field[25:38]
field_dict["DE43.3"]-de43_field[38:40]
return field_dict


# No field config provided, just exit
if not processor_config:
return dict()


# perform regex field matching
de43_regex= processor_config
field_match = re.match(de43_regex, de43_field)
if not field_match:
return dict()


# get the dict


field_dict = field_match.groupdict()
if field_dict.get("DE43_POSTCODE"):
field_dict["DE43_POSTCODE'] = field_dict["DE43_POSTCODE'].rstrip()
return field_dict


def iso8583 SubField dict(perentBit, message. bit config, enading-DEFAULT ENCODING maxSubFields-19):
LOGGER.debug("In\nSubfields(%s) Processing message: len-%s contents:\n%s",perentBit, len(message), message)
try:
message_length = len(message)-16
binary _bitmap, message_data = struct.unpack(
"16s" + str(message_length) + "s", message)
except struct.error as ex:


ing mes sage: len-%s contents:\n%s",perentBit, len(message), message)


return_values = dict ()
raise Iso8583DataError ("Subfields Failed unpacking bitmap values', binary_context_data-message, original_exception=ex


message_pointer


e


#bitmap_list = _get_bitmap_list(binary_bitmap, endian='little')


str1"f'(0x"+str(binary_bitmap)[2:18]+":0>64b)""
str1= '0'+eval(str1)


LOGGER. debug(f'Subfields bitmaplist: (str1]')
for bit in range(0, maxSubFields):
if strl[bit]--"1":
LOGGER.debug("Subfields processing bit %s", bit)
return_message, message_increment = _iso8583_to_field(
bit,
bit_config[str(bit)],
message_data[message_pointer:],
encoding)


#
Increment the message pointer and process next field


message_pointer += message_increment
return_values.update(return_message)
# check that all of message has been consumed, otherwise raise exception
if message_pointer != len(message_data):
raise Iso8583DataError(
f'Subfields Message data not correct length. "
f'Bitmap indicates len-(message_pointer), message is len-(len (message_data))
binary_context_data=message
Y


return return_values


def _dict_SubField_iso8583(message, bit_config, encoding=DEFAULT_ENCODING, maxSubfields-i9, hex_bitmap-false):


output_data
=b''


bitmap_values = [False] * 64


# get the pds fields from config
de_pds_fields - sorted(
[int(key) for key in bit_config if bit_config[key].get ("field_processor') -- "PDS "], reverse-True)
LOGGER.debug(de_pds_fields)


for de_field_value in _pds_to_de(message):
de_field_key = de_pds_fields.pop()
LOGGER.debug(f'de(de_field_key)=(de_field_value)")
message[f'DE(de_field_key)'] = de_field_value


for bit in range(1, maxSubFields):
if message.get("DE" + str(bit)) or message.get ('DE' + str(bit)) -- 0: # 0 evals to false, allow zero values
LOGGER .debug(f'processing sub bit (bit)")
bitmap_values[bit - 1] = True
LOGGER.debug(message.get("DE"+ str(bit)))
output_data +- _field_to_iso8583(
bit_config[str(bit)]
message.get('DE' + str(bit))
encoding=encoding)


n


bitarray
BitArray()
=
bitarray.fromlist(bitmap_values)
binary_bitmap = bitarray.tobytes()
if hex_bitmap:
bitmap - binascii.hexlify(binary_bitmap)
else:
bitmap
binary_bitmap
H
output _string - bitmap + output_data
return output_string

if _name_=='main':

Import doctest

doctest testmod()
