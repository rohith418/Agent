"""
Parsers for Wf 1508583 messages.

The iso8583 module is extension and customization to py cartutil.1506583 message parsing functions.
"""

import binascii

import datetime

import decimal

import logging

import re

import struct

import sys

from iso.bitarray import BitArray

from iso.1508583parser import Iso8583DataError, panMask

from iso.isofield import ISOFieldManager

LOGGER logging.getLogger(name)

DEFAULT ENCODING cp500'

def pack(obj: dict, encoding-None, iso_config-None, hex_bitmap-True):

if not encoding:

encoding DEFAULT_ENCODING

if not iso_config:

raise Exception("iso_config not provided')

output_dict_to_Iso8583(obj, iso config, encoding, hex bitmap)

return output

def unpack(b: bytes, encoding-None, iso config-None, hex bitmap-True):

if not encoding:

encoding DEFAULT ENCODING

if not iso config:

raise Exception("iso config not provided')

return iso8583_to_dict(b, iso_config, encoding, hex bitmap)
def_iso8583_to_dict(message, bit_config, encoding-DEFAULT ENCODING, hex bitmap-True):

LOGGER.debug("Processing message: len-ks contents: \nks", len(message), message)

message type_indicator message[:4]

message message[4:]

primaryßits message[:8]

message message[8:]

bitmap list get_bitmap_list(primaryBits)

secondayBits-b

if bitmap list[1]--True:

secondayBits message[18]

message message[8:]

bitmap listsec get bitmap_list(secondaybits)

bobitmap listSec.pop(0)

bitmap_list[@]-bitmap_list[0]+b

bitmap list.extend(bitmap_listsec)

message data-message

return_values dict()

add the message type

try:

return values["HTI"]

except UnicodeError as ex

message_type_indicator.decode(encoding)

raise Iso85830atafrror("Failed decoding MTI field, binary_context_data-message, original exception-ex)

message pointer o

no_of bits-len(bitmap list)-1

#LOGGER.debug(f'bitmaplist: (bitmap list)")

for bit in range(2, no_of_bits): if bitmap list[bit]:

LOGGER.debug("processing bit %s", bit)

fld_config-bit_config[str(bit)]

return message, message data ISOFieldManager.unpack(str(bit), message data, fld_config)

return_values.update(return_message)

return return_values
def _dict to_iso8583(message, bit config, encoding-DEFAULT ENCODING, hex bitmap-True):

output datab

bitmap values (False) 128

bitmap values (0) True set bit 1 on for presence of secondary bitmap

#get the pds fields from config

de pds fields sorted(

[Int(key) for key in bit config if bit config[key].get("processor") 'POS"), reverse-True)

LOOGER.debug(de_pds_fields)

for de field value in pds to de(message):

de field key de pds fields.pop()

LOGGER.debug(f de defield_key]-[de_field_value}")

message[f'DE (de field_key) de field_value

lastbit-e

for bit in range(2, 128):

if message.get("DE" + str(bit)) or message.get('DE' + str(bit)):a e evals to false, allow zero values

lastbit bit

LOGGER.debug(f'processing bit (bit)")

bitmap values[bit 1] True

LOGGER.debug(message.get('DE' + str(bit)))

fld_config-bit_config[str(bit)]

isSubfieldPack True if fld config.get('class')=="SUBFIELD PACK" else False

If isSubFieldPack:

#DE126 SUBFLDS

sublessage message.get('DE+ str(bit)+ SUBFLDS)

sub_fld_config fid config.get('fields')

fldValdict Subfield_iso8583(subitessage, sub_fld_config, encoding, hex bitmap-hex bitmap)

bobytearray(1)

b[0]-len(fldVal)

output data binascii.hexlify(b) fldval else:

message.get("DE' str(bit)),

output data field_to_iso8583(

fld_config,

encoding-encoding)

if lastbit 65:

-bitmap values[:64] bitmap values

bitmap values[0]-False

bitarray BitArray()

bitarray.fromlist(bitmap_values) binary bitmap bitarray.tobytes()

bitmap binascii.hexlify(binary bitmap)

ti message 'HTI"].encode(encoding) if message.get('HII") else b'"

output stringati bitmap output data

return output_string
def _field_to_iso8583(bit_config, field value, encoding-DEFAULT_ENCODING):

output

LOGGER.debug(f'bit_config-(bit_config), field_value-(field_value), encoding-(encoding)")

field value pytype_to_string(field_value, bit_config)

field length bit config.get('length')

field type bit_config['type']

length size get field_length(bit config) # size of length for livar and 11lvar fields

if length size > a:

field length len(field_value)

b-bytearray(1)

b[0]-field_length

If 'LLHBINARY in field type:

iint(field_length/2).

b[0]-1

LOGGER.debug(f"field_length=(field_length), blen-(b), hexlen (binascii.hexlify(b))")

output binascii.hexlify(b)

#else:

# output + format(field length, a+ str(length_size)).encode(encoding)

if isinstance(field value, bytes): output + field_value[:field_length]

else:

If 'IsHex' in bit config:

b-bytearray (field_value,bit_config['Istfex']) output +-binascii.hexlify(b)

else: output + format(field_value[:field length],<+ str(field_length)).encode(encoding)

return output

def pan prefix(field_data):

Get prefix of PAN

return field data[:9]
def

string to pytype(field data, bit config):

Field conversion to native python type

param field data: Data to be converted

param bit config: Configuration for bit

return: data in required type

field python type bit config.get('field_python_type')

field date format bit config.get('field date_format", "SyXeld")

if field python type in ("int", "long"):

field data int(field data) if

field python type "decimal":

field data decimal Decimal(field_data)

if field python type "datetime":

field data datetime.datetime.strptime(field data, field_date_format)

return field data

def _pytype to string(field data, bit config):

convert py type to string for message

param field data: Data to be converted

param bit config: Configuration for bit

return: data in required type

field_python_type bit_config.get("field_python_type')

field date format bit config.get('field_date_format", "XyXaid")

return string field data

if field python_type in ('int", "long"):

return string format(int(field data), "0" + str(bit config.get("length", 0))+'d")

if field python type "decimal":

return string format(decimal.Decimal(field data), 'e'+str(bit_config.get('length', 03) 'f')

if field python type "datetime":

if not isinstance(field data, datetime.datetime):

field data_get_date_from_string(field data)

return string format(field data, field_date_format)

return return_string

def get date from_string(field_data: str) -> datetime:

Parse string dates to python datetime object

Use dateutils library if it is installed, otherwise revert to simple parser

param field data: string containing date

treturn; datetime object

try:

import dateutil.parser as parser

debug('Using dateutil parser") LOGGER

return parser.parse(field data) except ImportError:

pass
if sys.version_info >= (3, 7):

LOGGER.debug("Using fromisoformat") return datetime.datetime.fromisoformat(field_data)

fallback parser tries a few different formats until one works LOGGER.debug('Using built in date parser')

date_formats ("XY-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d")

output date None

for date format in date_formats:

output date datetime.datetime.strptime(field_data, date format)

try:

break

except ValueError:

continue

if not output_date:

raise ValueError("Unrecognised date string format{}".format(field_data))

return output_date

def _get_field_length(bit_config):

Determine length of iso8583 style field

param bit_config: dictionary of bit config data :return: length of field

length size 0

fType bit_config["type"]

if fType == "LLVAR" or fType=="LLHNUM":

length size 1

elif fType "LLHEXVAR" or fType="LLHECHAR":

length size1

elif fType="LLHCHAR":

length size 1

elif fType "LLLVAR":

length size 1

elif fType "LLHBINARY": length size1

return length size

def get bitmap_list(binary_bitmap, endian='big'):

Get list of bits from binary bitmap

param binary bitmap: the binary bitmap to be returned

creturn: the list containing bit values. Bit e contains original binary bitmap

working bitmap_list BitArray(endian)

working bitmap list.frombytes (binary_bitmap)

#Add bit e original binary bitmap bitmap list [binary_bitmap]
add bits from bitmap

bitmap_list.extend(working_bitmap_list.tolist())

return bitmap list

def_pds_to_de(dict_values):

takes all the pds fields values in dict (PDSxxxx) and creates list of DE strings

param dict values: dict containing "PD5xxxxx" elements :return: list of byte strings containing pds data, or None if no fields

#get the PDS field keys in order

LOGGER.debug(f'dict_values=(dict_values)')

keys sorted([key for key in dict values if key.startswith("PDS")])

LOGGER.debug(f'keys (keys)')

output

outputs []

for key in keys:

tag int(key[3:])

LOGGER.debug(f'tag-(tag)")

length len(dict_values[key])

add_output f"[tag:04)(length:03)(dict_values[key])'

if len(output add_output) > 999: outputs.append(output)

output -

output + add_output if output:

outputs.append(output)

LOGGER.debug(f>pds2de: (outputs)")

return outputs

def _pds to dict(field_data):

Get MasterCard pds fields from iso field

param field_data: the 1508583 field containing pds fields

return: dictionary of pds key values. Key in the fore PDSxxxxx where x is zero filled number of pds

field pointer return values()

while field pointer < len(field_data): #get the pds tag id

pds field tag field_data[field_pointer:field_pointer+4] LOGGER.debug("pds_field_tag=[%s]", pds_field_tag)
#get the pds length

pds field length int(field data[field_pointer+4:field_pointer+7]) LOGGER.debug("pds_field_length [Xi]", pds_field_length)

#get the pds data

pds_field data field_data[field_pointer+7: field_pointer+7+pds_field_length] LOGGER.debug("pds_field_data=[%s]", str(pds_field_data))

return_values["POS" + pds_field_tag] pds_field_data

#increment the fieldPainter. field pointer+ 7+pds_field_length

return return_values

deficc_to_dict(field_data):

Get de55 fields from message

param field_data: the field containing de55 :return: dictionary of de55 key values

key is tagstagid

TWO_BYTE_TAG_PREFIXES [b'\x9f", b'\x5f"]

field pointer

return_values ("ICC_DATA": binascii.b2a_hex(field_data).decode())

while field pointer < len(field_data):

#get the tag id (one byte)

field tag field data[field_pointer;field_pointer+1]

# set to 2 bytes if 2 byte tag if field tag in TWO_BYTE TAG PREFIXES:

field_tagfield_data[field_pointer:field_pointer+2]

field pointer + 2

else: field pointer +1

field_tag_display binascii.b2a_hex(field_tag) LOGGER.debug("field_tag_display-ks", field tag_display)

#stop processing de55 if low values tag found

if field tag display b'ee':

break
field_length_raw field_data(field_pointer;field_pointer+1] field length struct.unpack("B", field length_raw)[0]

LOGGER.debug("%s", format(field_tag display)) LOGGER.debug(field_length)

get the tag data

de field data field_data[field_pointer+1:field_pointer+field_length+1]

de_field_data_display binascii.b2a_hex(de_field_data).decode()

LOGGER.debug("%s", de_field data display)

return_values["TAG" field tag display.upper().decode()] de field_data_display

#increment the fieldPointer

field pointer+1+field_length

return return values

def get de43 fields(de43_field, processor_config-None):

get pds 43 field breakdown

param de43 field: data of pds 43 :return: dictionary of pds 43 sub elements

LOGGER.debug(fde43_field-(de43_field), processor: (processor_config)")

#Udaya code

field dict dict()

field dict["DE43.1"]-de43_field[:25]

field dict["DE43.2"]-de43 field [25:38]

field dict["DE43.3"]-de43_field[38:40]

return field dict

No field config provided, just exit

if not processor_config:

return dict()

#perform regex field matching

de43 regex processor_config

field match re.match(de43 regex, de43 field)

if not field watch:

return dict()

#get the dict

field dictfield match.groupdict()

if field dict.get("DE43 POSTCODE):

field dict 'DE43 POSTCODE']field dict['DE43 POSTCODE').rstrip()

return field_dict
def iso8583 Subfield dict(perenthit,message, bit config, encoding-DEFAULT ENCODING, maxSubfields-19)

LOGGER.debug("\n\nSubfields(s) Processing message: len-ks contents:\nks", perentfit, len(message), message)

try:

message length len(message) 16

binary bitmap, message data struct.unpack( "166" str(message length), message)

except struct.error as exi

raise Iso85830atafrror("Subfields Falled unpacking bitmap values", binary_context data-message, original exception-ех) dict()

return values

message pointer

#bitmap list get bitmap list (binary hitmap, endians little")

stris"f(estr(binary_bitmap)(2:18]+10)646)

stri 'seval (str1)

LOGGER.debug("Subfields hitmaplist: (str1))

far bit in range(0, maxiubfields): If stri[bit]

LOGGER.debug("Subfields processing bit is", bit) return message, message increment 150fieldManager.unpackt bit,

message data[message pointers),

bit config[str(bit)])

Increment the message pointer and process next field

message pointer message Increment return values.update(return message)

# check that all of message has been consumed, otherwise raise exception

If message pointer len(message data) raise Iso8583DataError

Subfields Message data not correct length.

Bitmap indicates len(message pointer), message is len(len(message data),

binary_context data-message
)
return return values

def_dict Subfield iso0583(message, bit config, encoding-DEFAULT ENCODING, maxSubfields-19, hex bitmap-False):

output datab

bitmap values [False] 64

get the pds fields from config

de pds fields sorted(

(int(key) for key in bit config if bit config[key].get("processor") 'PDS), reverse-True)

LOGGER.debug(de_pds_fields)

for de field_value in_pds_to_de(message):

de field key de_pds fields.pop()

LOGGER.debug(f'de(de_field_key)-(de_field_value)")

message['DE(de field_key]] de_field value

for bit in range(1, maxSubFields):

If message.get('DE" + str(bit)) or message.get('DE+ str(bit)) 0: evals to false, allow zero values

LOGGER.debug(f'processing sub bit (bit)")

bitmap values[bit 1] True

LOGGER.debug(message.get("DE+ str(bit)))

output data_field_to_iso8583(

bit_config[str(bit )]. message.get('DE' + str(bit)).

encoding-encoding)

bitarray BitArray()

bitarray.fromlist(bitmap values)

binary bitmap bitarray.tobytes()

if hex bitmaps bitmap binascii.hexlify(binary bitmap)

else:

bitmap binary bitmap

output string bitmap output data

return output string

if name == '_main':

import doctest

doctest.testmod()
