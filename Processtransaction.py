from clearinglib.actions import ClearingActions
from clearinglib.transactions.record import ClearingRecord


class ProcessTransaction:


def _init_(self, clearingID:int, destFile:str=""
self.clearingID
clearing1 .
IE


runMode: str='T', tranSchema:str = 'V'


reRun: bool
False) -> None:
=


self.destFile = destFile
self.runMode = runMode
self.tranSchema = tranSchema
self.reRun = reRun
self. .proceedTransCount


def do(self, tran:ClearingRecord):
actions = ClearingActions()
if self.reRun:
#TODO - write duplicate file trans-double check logic
if self.runMode -- 'T' and (tran.ProcessType in ['O','L','M']):
actions.mapOiginal(tran)
if tran.ProcessType =='0':
actions.insertAddendaTrans(tran)
elif tran. ProcessType == ['O','L', "M']:
actions.mapLinked(tran)
#--Rerun ends here
elif tran.ProcessType == '0' or (self.runMode == "T' and tran.ProcessType == 'L'):
actions.createOriginalTran(self.__applyFilters(tran))
elif tran.ProcessType == 'L':
actions.createLinkedTran(tran)
elif self.runMode == "T' and tran.ProcessType == "M.
actions.map0iginal(tran)
elif tran.ProcessType == 'M':
actions.mapLinked(tran)


self.proceedTransCount += 1


def _applyFilters(self T+ran:ClearingRecord)
-> dict:
filteredDict = tran.__dict


if tran.TransactionAmt:
filteredDict["TransactionAmt"] float(tran.TransactionAmt)/100
if tran.CardholderAmt:
filteredDict["CardholderAmt"] float(tran.CardholderAmt)/100
if tran.ReconciliationAmt:
filteredDict["ReconciliationAmt"] float(tran.ReconciliationAmt)/100


return {k: v for k, v in filteredDict.items() if v}
def complete(self):
       pass
