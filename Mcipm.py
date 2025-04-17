"""
Mastercard reg IPM clearing file readers and writers

VBS file readers and writers

IPM file readers and writers

IPM parameter extract reader

Support for 1014 blocked format

Read an IPM file::

from cardutil import mciipm

with open('ipm in.bin', 'rb') as ipm_in:

reader mciipm.IpmReader(ipm_in)

for record in reader:

print(record)

Create an IPM file::

from cardutil import mciipm

with open('ipm_out.bin', 'wb') as ipm_out: writer mciipm.IpmWriter(ipm_out)

writer.write({'MTI': '1111', 'DEZ': '9999111122221111'))

writer.close()

MasterCard file formats

VBS file format

This format is a basic variable record format.

There are no carriage returns or line feeds in the file.

A file consists of records. Each record is prefixed with a 4 byte binary length.

Say you had a file with the following 2 records:

code-block:: text

"This is first record 1234567" < length 28

"This is second record AAAABBBBB123" < length 34

Add 4 byte binary length to the start of each record. (x'1C 28, x^2234) with the file finishing with a zero length record length

code-block:: hexdump
00000000:

00

00 00

10

54 68 69 73

00000010: 00000020:

74

20

72

65 22

63 54

6F 68

72 69

64

00

00

00

73

00000030:

68

64 42

20 42

72 65 63 6F 31 32 33 00

72 00

00000040: 42

1014 blocked file format

20 20

69 73 20 66 69 72 31

73

32 73

33 20

34 35

36

37

20 69

73 65

63

6F

64 20 41

41

41

41

42

42

This is the same as VBS format with 1014 blocking applied.

The VBS data is blocked into lengths of 1012, and an additional 2 x 40 characters are appended at each block.

.... This is firs

t record 1234567

... "This is seco

nd record AAAABB

888123....

Finally, the total file length is made a multiple of 1014 with the final incomplete record being filled with the x'40' character

Taking the above VBS example

code-block:: hexdump

00000000:

00 00 00 10 74 20 72 65

54 68 69 63 6F 72

73 64

00000010: 00000020: 00 00 00 22 54 68 69 73

00000030: 65 64 20 72 65 63 6F 72

00000040: 42 42 42 31 32 33 00 00

20 69 73 20 66 69 72 73 20 31 32 33 34 35 36 37 20 69 73 20 73 65 63 6F

64 20 41 41 41 41 42 42

.... This is firs

t record 1234567

... "This is seco

nd record AAAABB

888123....

Block to 1014 by adding 2 x 40' characters every 1812 characters in the data.

Finally fill with x'40' characters to next 1014 increment.

In this case, there is only one increment

code-block:: hexdump

00000000: 00 00 00 10 54 68 69 73

00000018: 74 20 72 65 63 6F 72 64

00000020: 00 00 00 22 54 68 69 73

00000030: 6E 64 20 72 65 63 6F 72

00000040: 42 42 42 31 32 33 00 00

20 69 73 20 66 69 72 73

20 31 32 33 34 35 36 37

20 69 73 20 73 65 63 6F

64 28 41 41 41 41 42 42

00 00 40 40 40 40 40 40

....This is firs

t record 1234567

nd record AAAABB

..."This is seco

888123....00000

00000050: 40 40 40 40 40 40 40 40

000003E0: 40 40 40 40 40 40 40 40 000003F0: 40 40 40 40 40 40

40 40 40 40 40 40 40 40

40 40 40 40 40 40 40 40

2000000000000000

Import io

import logging

import struct

import typing

from clearinglib.iso.wfcardutiliso8583 import pack, unpack from clearinglib.iso.spec import IPMSpec as WFISOConfigSpec

from iso.1508583parser Import 1508583BaseError

LOGGER logging.getLogger(name)

class Acilpabatafrror (1508583Basefrror): pass
class Block1014(object):

1014 Blocker for file objects.

Wrap around a file object. Return 1014 blocked data

PAD CHAR b\x40

definit(self, file_obj):

self.file obj file obj

self.remaining chars 1012

def getattr (self, name: str):

Attribute proxy for wrapped file object

try:

return self. dict_[name]

except KeyError:

if hasattr(self.file_obj, name):

return getattr(self.file_obj, name)

return None

def write(self, bytes_to_write: bytes) None:

Write requested bytes to the output file object.

# not enough bytes to complete a block, just write and subtract from remaining

LOGGER.debug(f'bytes_to_write=(bytes_to_write)')

if len(bytes_to_write) < self.remaining_chars:

LOGGER.debug(f'len->(len(bytes_to_write))<{self.remaining_chars}") )')

LOGGER.debug(f'write (bytes_to_write self.file_obj.write(bytes_to_write)

self.remaining_chars len(bytes_to_write)

return

#complete the first record

LOGGER.debug(f'write first: (bytes_to_write[:self.remaining_chars]}')

self.file_obj.write(bytes_to_write[:self.remaining_chars])

self.file_obj.write(self.PAD_CHAR 2)

bytes_to_write bytes_to_write [self.remaining_chars:]

#now write complete blocks

LOGGER.debug(f'write while: (bytes_to_write[:1012]}')

while len(bytes_to_write) 1012:

self.file_obj.write(bytes_to_write[:1012]) self.file_obj.write(self.PAD CHAR 2)

bytes_to_write bytes_to_write [1012:]

#write whatever is left

LOGGER.debug(f'urite last: (bytes_to_write)') self.file_obj.write(bytes_to_write)

self.remaining chars 1012-len(bytes_to_write)

LOGGER.debug(fremaining chars-(self.remaining chars)')

def seek(self, pos: int) None:

Finalise then seek file object to requested position
note:: Method only partially implemented. Only use to seek start of file (zero)

self.finalise()

self.file_obj.seek(pos)

def close(self) -> None:

Finalise then close the file object

self.finalise()

self.file_obj.close()

def finalise(self) -> None:

Complete the blocking operation by creating final 1014 block. Called by close and seek methods to ensure completion.

self.file_obj.write(self.PAD_CHAR (self.remaining chars + 2))

self.remaining_chars 1012

class Unblock1014(object):

Unblocks 1014 blocked file objects.

Wrap around a 1014 blocked file object. Return file like object providing only unblocked data

definit (self, file obj: typing.Binary10):

self.file_obj file obj

self.buffer b"

def getattr (self, name: str) -> any:

Attribute proxy for wrapped file object

try:

return self. dict_[name]

except KeyError:

if hasattr(self.file_obj, name):

return getattr(self.file_obj, name)

return None

def read(self, bytes to read: int0):
Read requested bytes from the file object. Returned data will be unblocked

read all True if not bytes to_read else False while read_all or len(self.buffer) < bytes to_read: block self.file_obj.read(1014) if not block: # eof self.buffer + block[:1012] output self.buffer[:bytes_to_read] self.buffer return output self.buffer[bytes_to_read:].

break

class VbsReader (object):

The VbsReader class can be used to iterate through a VBS formatted file object record by record.

from cardutil.mciipm import VbsReader with open('vbs_file.bin', 'rb') as vbs_file: vbs_reader VbsReader(vbs_file) for vbs_record in vbs_reader: print(vbs_record)

record number = 1

last record None

definit (self, vbs file: typing. Binary10, blocked: bool False):

Create a VbsReader -object

param vbs_file: File object with VBS formatted data

self.vbs_data vbs_file

if blocked:

self.vbs data Unblock1014(vbs_file)
def getattr (self, name)-> any:

Attribute proxy for wrapped file object

try:

return self. dict_[name]

except KeyError:

if hasattr(self.vbs_data, name):

return getattr(self.vbs_data, name)

return None

def _iter (self):

return self

def _next(self) -> bytes:

Unpacks a variable blocked object into records

record_length_raw self.vbs_data.read(4)

if len(record_length_raw) != 4:

this can happen if the VBS does not have a zero length record at end.

You can recreate using Vbswriter and not calling close method.

The reader will just accept we are at end if this happens.

LOGGER.warning(f'Unable to read next record length requested 4 bytes,' f' got (len(record_length_raw)) assuming end of data")

raise StopIteration

record length = struct.unpack(">i", record_length_raw) [0]

LOGGER.debug("record_length=%s", record_length)

#throw scipe data error if length is negative or excessively large (indicates bad input)

if record length < or record_length > 3000:

raise McilpmDataError(f"Invalid record length value read was (record_length)",

record_number-self.record_number, binary_context_data=self.last_record)

#exit if last record (length-0)

if record length - 8:

raise StopIteration

record self.vbs_data.read(record_length)

if len(record) ! record length:

raise McilpmDataError(f"Unable to read complete record record length: (record_length), f"data read: (len(record))", record_number-self.record_number,

binary_context_data-record_length_raw + record)

self. last record record_length_raw record #save last record read

self.record_number+1 # increment recurd counter

return record get the full record including the record length
class IpmReader(VbsReader):

IPM reader can be used to iterate through an IPM file

The file object must be in VBS format.

from cardutil.mclips import IpmReader with open('vbs_in.bin', 'rb') as vbs in: reader IpeReader(vbs_in) for record in reader: print(record)

If the file required 1014 block format, then set the "blocked parameter to True.

from cardutil.mciipm import IpmReader with open('blocked_in.bin', 'rb') as blocked_in: reader Ip Reader (blocked_in, blocked=True) for record in reader: print(record)

def_init_(self, ipm files typing.Binary 10, encoding: str None, iso config: dict None, **kwargs):

Create a new IpmReader

param ipm file: the file object to read sparam encoding: the file encoding param config: config dict with key bit_config

self.encoding encoding self.iso_config

WFISOConfigSpec#iso_config super(IpmReader, self).init (ipm file, **kwargs)

def next (self) -> dicti

vbs_record (IpmReader, self). next() LOGGER.debug(f(len(vbs_record)): (vbs_record))

try: output unpack(vbs_record, encoding-self.encoding, iso config-self.iso_config, hex bitmap=True) except 1508583BaseError as ex: raise HcilpmDataError(

"Error while loading 1508583 record', binary_context data-self, last_record,

record_number-self.record_number,
original exception ex
)
return output 
class Vbswriter(object):

Writes VBS formatted files.

The writer can be used as follows::

>>> with lo.BytesIO() as vbs out:

writer VbsWriter(vis_out)

writer.write(b'This is the record')

writer.close()

The close method must be issued to finalise the file by adding the zero length record which indicated the end of the file.

The message is a byte string containing the data.

Alternatively, you can use as a context manager which will take care of the writer closure.

>>>>> with io.Bytes10() as vbs_out:

with Vbswriter(vbs_out, blocked-True) as writer:

writer.write(b'This is the record")

definit (self, out file: typing. BinaryI0, blocked: bool False):

self.out file out file

if blocked:

self.out file Block1014(out file)

def getattr (self, name) -> any:

Attribute proxy for wrapped. file object

try: return self. dict_[name]

except KeyError:

if hasattr(self.out_file, name):

return getattr(self.out file, name)

return None

def write(self, record: bytes) -> None:

Add a new record to the VBS output file

sparam record: byte string containing data

creturn: None

#get the length of the record

record length len(record)

convert length to binary

record length_raw struct.pack(">i", record length)

add length to output data

self.out file.write(record_length_raw)

#add date to output

self.out file.write(record)
def write many(self, iterable: typing. Iterable[bytes]) -> None:

Convenience method to write multiple records from an iterable

param Iterable: iterable providing records as bytes

:return: None

for record in iterable:

self.write(record)

def close(self) -> None:

def

def exit(self, exc type, exc_val, exc_tb) -> None:

Finalise the VBS file output by adding the zero length file record.

:return: None

#add zero length to end of record

self.out_file.write(struct.pack(">1", 0))

self.out_file.seek(0)

enter_(self, *args, **kwargs):

return self

self.close()

class Ipmwriter (VbsWriter):

IPM writer can be used to write records to a Mastercard IPM file

22

>>>> with 10.BytesIO() as ipm_out:

writer IpmWriter(ipm_out)

writer.write({'MTI': '1111', 'DE2': '9999111122221111'))

writer.close()

If the required file is 1014 block format, then set the blocked parameter to True.
>>> with io.BytesIO() as Ipm_outs

writer Ipiriter(ipm out, blocked-True)

writer.write(('MT': '1111', 'DE2': 9999111122221111"))

writer.close()

All standard python encoding schemes are supported. Hainframe systems likely use cp500

You can provide the specific file encoding if required.

>>> with ic.BytesIO() as ipm_out: writer

Ipewriter(ips_out, encoding cp500) writer.write({'I': '1111', 'DE2': 9999111122221111')) writer.close()

Alternatively use as a context manager to ensure closure at end of processing

12

>>> with io.Bytes10() as ipm outs

with Ipewriter(ipm out, encoding cp500") as writer: writer.write("HTI': '1111', 'DE2': 9999111122221111"})

definit (self, file obj: typing.Binary10, encoding: str None, iso config: dict None, **kwargs):

Create a new Ipiriter

sparan file_obj: the file object to write to paras encoding: the file encoding

self.encoding encoding self.iso config. iso config

super(Ipelwriter, self). init (file obj, **kwargs)

def write(self, obj: dict) -> None:

Writes new record to IPM file

param obj: dictionary object containing 1508583 elements,

See :py:mod: cardutil.iso8583" for expected dict object keys.

:return: None
"""
record pack(obj, encoding self.encoding, iso_config-self.iso_config) super(Ipewriter, self).write(record)

def write many(self, iterable: typing. Iterable[dict]) -> None:

Convenience method to write multiple records from an iterable

param iterable: iterable providing records as dict

:return: None

for record in iterable: self.write(record)

def unblock_1014(input_data: typing-Binary 10, output data: typing.BinaryIO):

Unblocks a 1014 byte blocked file object

param input_data: 1014 blocked IPM file object

param output_data: unblocked file object

pad char blx40

while True:

record input data.read(1014)

if not record:

break

if len(record) 1 1014:

raise McilpmDataError("Invalid record size for 1014 blocked')

if record [-2:] != pad_char 2:

raise McilpmDataError('Invalid line ending for 1014 blocked')

output_data.write(record[0:1012])

output data.seek(e) input data.seek(0)
def block 1014(input data: typing.Binary 10, output data: typing.Binary10):

Creates a 1014 byte blocked file object

param input data: file object to be 1014 byte blocked

param output data: 1014 byte blocked file object

pad char blx40

while True:

record Input data.read(1012)

end of data

if not record:

break

#incomplete 1012 block if len(record) 1 1012:

record (1012 len (record)) pad char

output data.write(record+ (pad_char 2))

output data.seek(e)

input data.seek(0)

def vbs list_to bytes(byte list: iter, **kwargs) -> bytes:

Convenience function for creating VBS byte strings (optionally blocked) from list of byte strings

param byte listi a list containing byte string records

param kwargs: any options to be passed to Vbskwriter constructor. See spy:mod: cardutil.mciipm.Vbswriter

:return: single byte string containing VBS data.

file out lo. Bytes10()

vbs out Vbswriter(file_out, **kwargs)

for rec in byte list: vbs_out.write(rec)

vbs_out.close()

return file_out.read()
def vbs_bytes_to_list(vbs_bytes: bytes, **kwargs) -> list:

Convenience function for unpacking VBS byte strings to byte string list

param vbs bytes: single byte string containing VBS data

param kwargs: any options to be passed to VbsReader constructor. See spy:mod: cardutil.clipm.VbsReader

return: a list containing byte string records

file in io.BytesI0(vbs bytes)

return [record for record in VbsReader (file in, **kwargs)]

if name ==  'main':

Import doctest

doctest.testmod()
