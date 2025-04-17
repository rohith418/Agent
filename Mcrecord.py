import datetime

from clearinglib.transactions.record import ClearingRecord

import math

import logging

logger = logging.getLogger()

class IPMClearingRecord (ClearingRecord):

def _init(self, deJson:dict, runmode: str) -> None: super()._init(deJson, runmode)

self.CardType = "1"

self.MessageType = self.getValue('MTI')

self.FunctionCode = self.getValue('DE24')

self.CardExpDate = self.getSafeValue('DE14')

self.RefNum = self.getSafeValue('DE31')

self. TransactionAmt = self.getSafeValue('DE4')

self. TransactionCurrency self.getSafeValue('DE49')

self.ReconciliationAmt self.getSafeValue('DE5')

self.ReconciliationCurrency self.getSafeValue('DE50')

self.CardholderAmt = self.getSafeValue('DE6')

self.CardholderCurrency self.getSafeValue('DE51')

strTrnsDate = self.getSafeValue('DE12')

if(len(strTrnsDate) !=12):

strTrnsDate = datetime.datetime.now().strftime("%y%m%d%H%M%S")

self. TransactionDate = strTrnsDate

self.RevlIndicator self.getSafeValue("PDS_48.PDS25")

self.POSDataCodes = self.getSafeValue("DE22")

self.PCode = self.getSafeValue('DE3')

self.MsgReasonCode self.getSafeValue("DE25")

self.MCC = self.getSafeValue("DE26")

self. AcquirerID = self.getSafeValue("DE32")

self. RetrievalRefNum = self.getSafeValue("DE37")

self. AuthCode = self.getSafeValue("DE38")

self. TerminalID= self.getSafeValue("DE41")

self. ReceiverID = self.getSafeValue("DE100")
self.DestinationID= self.getSafeValue("DE93")

exchangeRate = self.getSafeValue("DE10")

if exchangeRate != "": self. ExchangeRate format_rate(exchangeRate)

exponent self.getSafeValue('PDS_48.PDS148')

if exponent != '": self.CurrExponent exponent [3:4]

self. ForwarderID = self.getSafeValue("DE33")

self.CardAcceptorID = self.getSafeValue("DE42")

merDetails = self.getSafeValue("DE43")

if merDetails != "":

#INFINITE WOMEN S CARE\\502 WASHINGTON AVE\\LOS BANOS \\93635

CA USA

mName, mAddress, mCity, mZipStateCountry= merDetails.split('\\)

self.Merchant Name mName

self.MerchantAddress mAddress

self.MerchantCity = mCity

if mZipStateCountry != "":

self. MerchantPostCode mZipStateCountry[:10]

self.MerchantState = mZipStateCountry [10:13]

self.MerchantCountry mZipStateCountry [13:16]

self. setTransType()

self. TransType = self._getIPMType()

def_setTransType(self):

msg type self. MessageType

function_code= self.FunctionCode

p_code self.PCode

p_code_value = 0
if p_code != "":

p_code_value = int(p_code [0:2])

revl_indicator self.RevlIndicator

logger.debug(f"mode={self.RunMode), msgType={msg_type),functionCode={function_code), pCode=(p_code), RevlIndic={revl_indicator).")
if self.RunMode "T":

if msg_type == "1240":

if function_code == "200":

if p_code_value <= 18 or p_code_value == 50:

self.ProcessType = "0"

self.ClearingType = "D" elif p_code_value = 20 or p_code_value == 28: self. ProcessType = "0" self.ClearingType = "C" else: logger.debug("Ignoring this record")

elif function_code in ["205", "282"]:

if p_code_value <= 18 or p_code_value == 50: self. ProcessType = "L" self.ClearingType = "D" elif p_code_value == 20 or p_code_value = 28: self.ProcessType = "L" self.ClearingType = "C"

else: logger.debug("Ignoring this record")

else:

logger.debug("Ignoring this record")
elif msg type == "1442":

if function_code in ["450", "453", "451", "454"]:

if if p_code_value <= 18 or p_code_value == 50:

self.ProcessType = "L"

self.ClearingType = "C"

elif p_code_value 20 or p_code_value == 28:

self.ProcessType "L"

self.ClearingType = "D"

else:

logger.debug("Ignoring this record")

if (revl_indicator=="R"):

if self.ProcessType == "0": self. ProcessType="L"

if self.ClearingType == "D": self.ClearingType ="C"

if self.ClearingType == "C": self.ClearingType = "D"

def _getIPMType(self):

mti self.MessageType

functionCode self. FunctionCode

if mti == "1240":

if functionCode == "200":

return 1;

if functionCode in ["205", "282"]:

return 2;

elif mti == "1442": return 5

elif mti == "1740": return 13

elif mti= "1644":

if functionCode == "603": return 6

if functionCode == "640": return 7

if functionCode == "680": return 8

if functionCode == "685": return 9

if functionCode = "688": return 10

if functionCode == "695": return 11
if functionCode == "696": return 4

if functionCode == "697": return 12

return 0

def format_rate(field):

try:

power int(field[0])

amount = float(field[1:])

amount / math.pow(10.0, power)

return str(amount)

except ValueError:

logger.debug("Unparseable rate")

return ""
