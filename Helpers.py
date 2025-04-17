from typing import Any
from functools import lru_cache


def


compareInItem(item, **orkeyvals):
if lem(orkeyvals.items())==0: return False
for k,v in orkeyvals.items():
if item[k]==v: return True
return False


def codeExists(listItems, *orkeyvals):
#filter(lambda i:i[keyl]=-valuel,listItems)
return any(_compareInItem(item, **orkeyvals) for item in listItems)
def findNgetKeyalue(getKey, listItems, **orkeyvals)-> Any:


list(fllter(lambda item: _compareInItem(item, **orkeyvals), listItems))
#
1
#if len(1)==0: return None
# return l[0].get(getkey)
for item in listItems:
if __compareInItem(item, *orkeyvals):
return item.get (getKey)
return None


def validateCreditCard(card_number: str) -> bool:
"""This function validates a credit card number."""
#1. Change datatype to list[int]
try:
card_number = [int(num) for num in card_number]
except Exception
as e:
# int() may through if it has any non numeric char
return False
2. Remove the last digit:
checkDigit
card_ -number.pop(-1)
# m Reverse the remaining digits:
card_number.reverse()
#4. Double digits at even indices
card_number
=
[num
2 if idx % 2 == 0
else num for idx, num in enumerate(card_number)]
#5. Subtract 9 at even indices if digit is over 9
#(or you can add the digits)
card_number [num - 9 if idx % 2 -- 0 and num > 9
else num for idx, num in enumerate(card_number)]
#6. Add the checkDigit back to the list:
card_number.append(checkDigit)
#7. Sum all digits:
checkSum= sum(card_number)
# 8. If checkSum is divisible by 10, it is valid.
return checkSum % 10== 0
