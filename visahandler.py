from clearinglib.transhandlers.basehandler import BaseRecordHandler

import logging

from clearinglib.transactions.record import ClearingRecord

import os, clearinglib.transhandlers.visa_dict as visa_dict from clearinglib.transactions.visarecord import VisaClearingRecord from datetime import datetime
LOGGER logging.getLogger(name_)

# constants

#block size for VISA clearing

VISA BLOCK SIZE = 168

BLOCK_END_SIZE = 1 #One char is \n, actual block + 1
class VisaRecordHandler (BaseRecordHandler):

IDENTIFIER_BYTE_LOCATIONS = [1,2,9,10, 11, 12, 13, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 77, 78, 79, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
class VisaRecordHandler (BaseRecordHandler):

IDENTIFIER_BYTE_LOCATIONS = [1,2,9,10,11,12, 13, 27, 28, 29, 30, 31

def init_(self, file: str, mode: str) -> None:

super().init(file, mode)

def_genFileIdentifier(self) -> str:

byte_elem bytearray(1)

id_value = "

try:

i = 0

with open(self.filePath, "rb") as raf:
while i < len (VisaRecordHandler. IDENTIFIER_BYTE_LOCATIONS):

#print("ID LOC:", i, VisaRecordHandler. IDENTIFIER_BYTE_LOCATIONS [1])

raf.seek(VisaRecordHandler. IDENTIFIER_BYTE_LOCATIONS[i])

raf.readinto(byte_elem)

id_value += chr(byte_elem[0])

i  += 1

LOGGER.info("File ID is [%s]", id_value)
except Exception as ex:

LOGGER.error("_genFileIdentifier Function")

raise ex

return id_value

4

def updateRecord(self, record: ClearingRecord) -> bool:

return super().updateRecord(record)

def writeToFile(self) -> bool:

return super().writeToFile()

def_parser(self, v_file: str, mode: str) -> None:

# check incoming file exists

if not (os.path.exists(v_file)):

LOGGER.info('File'+v_file + does not exist!!)

exit(1)

# find string

blocksize =  VISA_BLOCK_SIZE+BLOCK_END_SIZE

recLen=int(os.path.getsize(v_file)/blocksize)

LOGGER.info("filesize:", v_file, reclen)

UMIT:dict={}
1-0

rectoProcess = 0

recUpdated 0

recIgnorede

self.Not SupporCount = e

self.CRecords=[]

with open(v file, 'r', blocksize) as src file: # changed rb to r

while i recten:

src_file.seek(i blocksize)

block src_file.read(blocksize)

14-1

mti-block[0:4]

If uMIT.get(mti):

UMIT [mti] UMIT.get(mti)+1

else: uMIT[mti]=1

vcr-self. getTCRRow(block)

if vcr.TransCode not in ['90', '91', '92'] and vcr.TransComponent Seq in ['0', '1']:

self. setTransTypes (vcr)

vcr.TxType self._txType(vcr)

if ver.TransComponentSeq'0':

tDt vcr.TransactionDate

if tDt 1"": vcr.TransactionDate format_visa_tran_date(tDt) if self.runMode !='T':

tant vcr. TransactionAmt tCurr vcr.TransactionCurrency

vcr.TransactionAmt vcr.CardholderAmt

vcr.TransactionCurrency vcr.CardholderCurrency

vcr.CardholderAmt tAmt

vcr.CardholderCurrency Curr

self.CRecords.append(vcr)

recToProcess+ 1

LOGGER.debug(f"\nrecord (recToProcess}-update (recUpdated): ", vars(vcr))

elif ver.TransComponent Seq'1':

lastVCR self.CRecords[len(self.CRecords)-1]

LastVCR.MsgTextBlock vcr.MsgTextBlock
lastVCR.CardAcceptorID vcr.CardAcceptorID

lastVCR. TerminalID vcr.TerminalID

recupdated + 1

LOGGER.debug(f"\nrecord (recToProcess) update (recUpdated): ", vars(lastVCR))

recIgnored 1

self. TotalRecords recToProcess

self.MsgRecCount recupdated

print("Ignored: ", recignored, UMIT)

def

getTCRRow (self, str)->VisaClearingRecord:

#print ('TC' str[0:2], visa dict.TC[str[0:2]]) #TC

key str[0:2]+'X'+str[3:4]

if key in visa dict.TCR:

tervisa dict.TCR[key]

else:

ter visa dict.TCR ELSE

self.Not SupportCount + 1

#7000: print('TCR is not supported yet, key)

vcr-VisaClearingRecord((),self.runMode)

for i in tor:

sti[0]

en-1[1]

ds-1[2]

tag-None

if len(i)4: tag 1[3]

vstr[st-1:st+en-1]

#rec[tag]-v

if tag: setattr(ver, tag, v)

#print(ds + ':' ,v)
return ver

def set Trans Types (self, rec:VisaClearingRecord): transCode rec. TransCode usageCode rec. UsageCode

TCQ rec.TCQ

if self.runMode "T":

if transCode= "05":

if TCQ= "0": if usageCode

"1": LOGGER.debug("Original Sales Presentment") rec. Process Type = "0" rec.ClearingType = "D"

else:

LOGGER.debug("Second Sales Presentment") rec. ProcessType "L"-rec. ClearingType = "D"

elif TCQ "1":

LOGGER.debug("Account Funding") rec. ProcessType = "0"

rec.Clearing Type - "D"

elif transCode == "06":

if TCQ= "0": LOGGER.debug("Credit Presentment") rec. Process Type = "L" rec.ClearingType = "C"

elif TCQ "2": LOGGER.debug("Cardholder Funds Transfer")

rec. Process Type

"0"

rec.ClearingType = "C"

elif transCode "07":

if TCQ "1":

LOGGER.debug("Original Cash Presentment") rec. Process Type "0" rec.ClearingType "0"

else:
LOGGER.debug("Second Cash Presentment") rec. Process Type "L" rec.ClearingType "D"

elif transCode = "25": LOGGER.debug("Sales Reversal") rec. ProcessType = "L" rec.Clearing Type "C"

elif transCode "26": LOGGER.debug("Credit Reversal") rec. Process Type = "L" rec.Clearing Type "D"

elif transCode == "27": LOGGER.debug("Cash Reversal") rec. ProcessType = "L" rec.Clearing Type "C"

elif transCode == "15": LOGGER.debug("Sales Chargeback") rec. ProcessType = "L" rec.Clearing Type "C"

elif transCode "16": LOGGER.debug("Credit Chargeback") rec. ProcessType = "L" rec.ClearingType = "D"

elif transCode == "17": LOGGER.debug("Cash Chargeback") rec. ProcessType = "L" rec.Clearing Type = "C"

elif transCode == "35": LOGGER.debug("Sales Chargeback Reversal ") rec. ProcessType = "L"

rec.ClearingType = "D"

elif transCode == "36":
LOGGER.debug("Credit Chargeback Reversal ")

rec. ProcessType = "L"

rec.Clearing Type = "C"

elif transCode == "37":

LOGGER.debug("Cash Chargeback Reversal ")

rec. ProcessType = "L"

rec.Clearing Type = "D"

def_txType(self, rec: VisaClearingRecord):

trans code rec. TransCode

usage_code rec. UsageCode

if trans code == "05":

if usage code. == "1":

return "1"

if usage code == "2":

return "2"

elif trans code == "06":

if usage_code = "1": return "3"

if usage_code == "2": return "4"

elif trans_code == "07":

if usage_code == "1":

return "5"

if usage_code == "2":

return "6"

elif trans_code == "01":

if usage_code == "1":

return "7"

if usage_code == "2":

return "8"

elif trans code == "02":

if usage_code == "1":

return "9"

if usage_code == "2":

return "10"

elif trans code == "04":

if usage code == "1":

return "11"

if usage code == "2":

return "12"
elif trans code == "25":

if usage code "1":

return "13"

if usage code="2":

return "14"

elif trans code == "26":

if usage code = "1":

return "15"

if usage code = "2":

return "16"

elif trans code == "27":

if usage_code == "1":

return "17"

if usage code == "2":

return "18"

return "0"

def format visa_tran_date(visa_date):

LOGGER.debug(visa_date)

visa_mm int(visa_date[:2])

yy_date=

curr date datetime.now().strftime("%y%m")

curryy int(curr_date[:2])

curr mm int(curr_date[2:4])

if visa mm > curr mm:

tmp_year str(curryy 1)

if len(tmp_year) 1:

yy_date "0" + tmp year visa date

else:

yy_date= tmp year + visa date

else:

yy_date curr_date[:2] + visa_date

return yy_date + "000000"
