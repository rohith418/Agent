from typing import List

class ClearingRecord():

def _init(self, deJson:dict, runmode: str='T') -> None:

self. deJson = deJson

self. TransType: int=1

self. RunMode runmode

self. ProcessType = ""

self.ClearingType = ""

self. TransactionRecord =

self.MessageType = ""

TransactionType =

self.FunctionCode = ""

self.PCode =

self.CardNum = ""

self.CpnId = ""

self.RefNum =

self.MappedCardNum =

self.MappedCardExpDate =

self.MappedRefNum =

self.MappedAcquirerID = ""

self.TransactionAmt =

self.CardholderAmt =

self.ReconciliationAmt =

self. TransactionCurrency =

self.CardholderCurrency =

self. Reconciliation Currency = ""

self. TransactionDate = ""

self.CardExpDate =" " 

self.POSDataCodes =" "
self.MsgReasonCode =

self.MCC = ""

self. Acquirer ID =

self.CardAcceptorID =

self.ReceiverID =

self. ExchangeRate =

self.Forwarder ID =

self.CurrExponent =

self.MerchantID =

self.MerchantName =

self.MerchantAddress =

self.MerchantCity =

self.MerchantState =

self.MerchantPostCode =

self.MerchantCountry =

self. RetrievalRefNum =

self.AuthCode =

self. TerminalID = ""

self.MsgTextBlock =

self.CardType = ""

self.RevlIndicator =

self.RecordCount: int = 0

self. TransCount: int = 0

self.OutputTransCount: int = 0

self.OutputRecordCount: int = 0

self.CPN = ""

self. PrevProcessed:int = 0

self.DestinationID =

self.StartRange =

self.MappedStartRange = ""

self.MappedEndRange =

self.PanExists = False
self. InLineMode False

self. TxType = ""

self.ShouldMapAddenda False

self. UsageCode = ""

self. TransCode =

self.TCQ =

self. TransComponentSeq = ""

self. SubsequentRecord = ""

self. TransactionBinary: bytes=[]

self.ipmType: int = 0

self.Addenda: List [ClearingRecord] = []

self.Duplicate = False

def reset(self):

self. TransactionRecord = "

self.HeadMsg = None

self.Addenda= []

self. TransactionBinary = None

self.ProcessType =

self.Clearing Type =

self.MessageType =

self. TransactionType = ""

self.FunctionCode =

self.PCode = ""

self.CPN =

self.CardNum = ""

self.CpnId =

self. RefNum =

self.MappedCardNum = ""

self.MappedCardExpDate =

self.MappedRefNum = ""

self.MappedAcquirerID =

self. TransactionAmt = " "
self.CardholderAmt =

self.ReconciliationAmt =

self. TransactionCurrency = ""

self.CardholderCurrency = ""

self. Reconciliation Currency = ""

self. TransactionDate =

self.CardExpDate =

self.POSDataCodes =

self.MsgReasonCode =

self.MCC =

self.AcquirerID = ""

self.CardAcceptorID =

self. ReceiverID =

self. ExchangeRate =

self. ForwarderID =

self.CurrExponent = ""

self.MerchantID = HR

self.MerchantName =

self.MerchantAddress = ""

self.MerchantCity =

self.MerchantState = ""

self.MerchantPostCode = ""

self.MerchantCountry =

self. RetrievalRefNum =

self. RevlIndicator = ""

self.AuthCode =

self. TerminalID =

self.MsgTextBlock = ""

self.CardType =

self. UsageCode =

self. TransCode =
self.TxType"

self. TransComponentSeq =

self. SubsequentRecord = ""

self. StartRange = HR

self.MappedStartRange = ""

self.MappedEndRange =

self.DestinationID =

self.PanExists = False

self.ShouldMapAddenda False.

self. InLineMode = False

def getSafeValue(self, key:str, convertPyType: type=None)-> str:

obj self.getValue(key)

if obj:

return str(obj)

return ""

def getValue(self, key:str):

if key.find('.') > 0:

key, subkey-key.split('.')

subList=self._deJson.get(key)

if subList:

return subList.get(subkey)

else:

return self._de]son.get(key)

return None
