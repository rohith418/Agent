import binascii
from array import array


class BitArray:
endian
big
bytes = b''


def init(self, endian='big'):
self.endian = endian


def frombytes(self, array_bytes):
self.bytes = array_bytes


def tobytes(self):
return self.bytes


def tolist(self):
swap_bytes = array('B', self.bytes)
if self.endian == 'little':
for i, n in enumerate(swap_bytes):
swap_bytes[i] = int("(:08b)".format(n)[::-1], 2)
width = len(self.bytes)*8
swapped_bytes = swap_bytes.tobytes ()
bit_list = '/bytes:0/width¥b?'.format (bytes=int(binascii.hexlify(swapped_bytes), 16), width=width)
return [bit == '1' for bit in bit_list]


def fromlist(self, bytelist).
it https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-:
binary_value = "`.join([1' if val else '0' for val in bytelist])
self.bytes = int(binary_ value, 2)to_bytes(len(binary_value) // 8, byteorder="big')
