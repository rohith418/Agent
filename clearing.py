#Incoming
Parameters



import argparse
import datetime
import os
import sys


from clearinglib.actions import ClearingActions
from clearinglib.transactions.record import ClearingRecord
from clearinglib.transhandlers.basehandler import BaseRecordHandler
from clearinglib.transhandlers.visahandler import VisaRecordHandler
from clearinglib.transhandlers.masterhandler import MasterCardRecordHandler
from clearinglib.processtransaction import ProcessTransaction


import logging


from db dbmanager import DBManager
from util.config import Config
from


util.wfcryptomanager import WFCryptoUtil
LOGGER = logging.getLogger(_name)
LOGGER. setLevel(logging.INFO)
logging.getLogger(.setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


if


name_


main_


parser argparse.ArgumentParser (description='Wells Fargo Virtual Cards-VISA BASEII/MasterCard IPM cleaning processor')
parser.add_argument("-t", dest='src_type', help="Source file type (Visa-v/Mastercard-m)")
parser.add_argument("-s", dest='src', help="Source file name with complete path")
parser.add_argument("-d", dest="dest", help-"Destination file name", required=False)
parser.add_argument("-m", dest='mode', help="Run mode (Default='T")", required=False)
args= parser.parse_args()
1_src_type = str(args.src_type)
1_src str(args.src)
l_dest = str(args.dest) if args.dest else l_src+".out"
1_mode - str(args.mode) if args.mode else "T"
fName = os.path.basename(1_src)


logging.info("Clearing


process starting..")
config:Config = Config("app-config.ini")
logging.info(f"Initializing Crypto Manager..")
#Initialize cryptors: Without this Cryptors we can't use encryption keys are there in keystore
WFCryptoUtil().initialize(config)
DBManager.initConfig(config)
logging.debug(f"Datasetting: [DBManager.DBConnPoolSettings ")
LOGGER.info(f'CLEARING FILE PROCESS STARTED-[fName)")
#p-psutil.Process(os.getpid())
#LOGGER. . info("Memory: xs GB", P . Iemory_info()
vmS, /1000009009)
#LOGGER.info('The CPU usage is: %s', psutil.cpu_percent(4))
rh:BaseRecordHandler = None
if l_src_type.upper() == 'V`:
rh-VisaRecordHandler(l_src,l_mode)
#LOGGER.info(rh.TotalRecords," processed for file id: ", rh.FileID)
#LOGGER.info(rh.NotSupportCount, " are not supported, ", rh.MsgRecCount
are updated msg records")
else:
rh - MasterCardRecordHandler(1_src, l_mode)


for tran in rh:
LOGGER.info (f"record(ftran._dict_)) processing')
#
ca=ClearingActions(
# c=ClearingRecord(t),'T')
# c.FunctionCode='05.
#c.ProcessType = '1"
#c.AcquirerID="323232323232
# c.RefNum = '2323232322.
# c.CardNum= '4159282716415737
c.ClearingType = 'C'
#
#
c.CardExpDate
"2410
I
# c.TransactionAmt = 300
#c.TransactionDate = '2024-09-05
# #("fileName":"Udayafile1.pdf","test": 02.3, "col2":2)
#rs = ca.createOriginalTran(c)
print(rs)
sys.exit(0)


isDup, recFile = ca.IsFileAlreadyProcessed(rh.FileID, mode=l_mode)


clearingID = -1
if not isDup:
clearingID = ca.InsertClearingFile(fName,rh.FileID, 1_mode, rh.TotalRecords)
elif recFile:
clearingID recFile.get("clearingID')
#TODO - write logic for duplicate records


pt ProcessTransaction(clearingID=clearingID, destFile= l_dest, runMode=l_mode, tranSchema=l_src_type.upper(), reRun= isDup)


startAt=0
stopAt=2
for tran in rh:


LOGGER.info (f'record((startAt+1)) processing')
pt.do(tran)
rh,updateRecord(tran)
LOGGER.info (f'record(startAt+1)) completed')
startAt+=1
if startAt >=stopAt: break


rh.writeToFile()
pt.complete()


ca.updateFileStats(clearingID, ("total_records": rh.TotalRecords,
LOGGER.info(f'CLEARING FILE PROCESS COMPLETED-[fName)')


processed_records': pt.proceedTransCount,


process_en_date': datetime.datetime.now()))


LOGGER.info("Memory: %s GB", p.memory_info().vms/1000000000)
#LOGGER. info('The CPU usage is: %s', psutil.cpu_percent(4))
