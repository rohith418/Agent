from clearinglib.iso.mcipm import IpmReader

from clearinglib.transactions.record import ClearingRecord

from clearinglib.transhandlers.basehandler import BaseRecordHandler

import logging

from clearinglib.transactions.mcrecord import IPMClearingRecord

class MasterCardRecordHandler (BaseRecordHandler):

IDENTIFIER BYTE LOCATIONS

[34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]

def _init_(self, file: str, runmode: str) -> None:

super().init(file, runmode)

def _genFileIdentifier(self) -> str:

lenIndetifier len (MasterCardRecordHandler. IDENTIFIER_BYTE_LOCATIONS)

id_bytes bytearray (lenIndetifier)

id_value=

try:

with open(self.filePath, "rb") as raf:

while i < lenIndetifier:

raf.seek(MasterCardRecordHandler. IDENTIFIER_BYTE_LOCATIONS[1-1])

id_bytes [i 1:1] raf.read(1)

11

id_value id_bytes.hex()[:2 (1-1)]

logging.debug("File ID is [%s]", id_value) raf.seek(0)

except Exception as ex:

logging.error("_genFileIdentifier Function")

raise ex
return id_value

def _parser(self, file: str, runmode: str)->None:

with open(file, 'rb') as ipm_in:

reader IpmReader(ipm_in, blocked=True)

for record in reader:

#iso_config=spec["mci_parameter_tables"])

self.CRecords.append(IPMClearingRecord(record, runmode))

#print(f"\nRecord (i):\n", vars (self.CRecords[i-1]))

def updateRecord(self, record: ClearingRecord) -> bool:

return super().updateRecord (record)

def writeToFile(self) -> bool:

return super().writeToFile()
