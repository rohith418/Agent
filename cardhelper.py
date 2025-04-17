from random import randint
import datetime
import secrets


card_types = ["visal3", "visal6", "mastercard"]
cvv_lengths - [3,3,3,3]


class CardHelper:


@staticmethod
def generatecW(length) ->str:


"


Generates
◦


type-specific CW number


CC_CVV


for x in range(length)
cc_cvv.append(secrets.randbelow(9))


return ".join(map(str,cc_cvv))


@staticmethod


def generateVCN(type, cardlenght=None):


De
T
1, 1), def_length
elif t = card_types[1] or t == card_types[2]:
return [5, randint(1,5)], def_length - 2
return [3, randint(4,7)], 13
return [4], def_length
== card_types[0]:
if t.endswith("16"):
return [4], 12
elif t == card_types[4]:
elif t == card_types[3]:
def_length = 16
return [6,
else:
def prefill(t):
if
else:


return [], def_length


def finalize(nums):
check_sum
e


check_offset
(len(nums) + 1) * 2
for i, n in enumerate(nums):
if (i+ check_offset) X 2 == 0:
n_ = n*2
check_sum += n_ -9 if n_ 7 9 else _
n
+=
n_- n*2
+
check_sum
else:
return nums


[10
S (check, sum
10)


try:
t = type.lower ()
except:


pass


if X in card_types:
initial, rem - prefill(t)
else:


try:


t - int(t)
except:
print("[ERROR] invalid bin/card type")


raise Exception("[ERROR] invalid bin/card type")
str(t)]


initial
[int(x) for x in
rem = cardlenght-len (initial)


so_far - initial + [randint(1,9) for x in range(rem - 1)]
returnme - str(int("".join(map(str,finalize(so_far)))))


return returnme
