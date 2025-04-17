from abc import ABC, abstractmethod

from typing import List

from clearinglib.transactions.record import ClearingRecord

class BaseRecordHandler (ABC):

def _init_(self, file:str, runmode: str) -> None:

super().init_()

self.runMode = runmode

self.CRecords: List [ClearingRecord]=list()

self._curPos = 0

self._totRec = 0

self.filePath = file

self._fileIdentifier = self._genFileIdentifier()

self.Not SupportCount = 0

self.MsgRecCount = 0

def iter(self):

self._curPos = 0

self._totRec = 0

self._parser(self.filePath, self.runMode)

return self
def

next(self) -> ClearingRecord:

if self._curPos len(self.CRecords):

item self.CRecords [self._curPos]

self._curPos += 1

return item

else:

self._curPos = 0 #reset the current position

raise StopIteration

@property

def FileID(self) -> str:

return self. _ fileIdentifier

@property

def TotalRecords (self) -> int:

return self._totRec

@TotalRecords.setter

def TotalRecords (self, totRecods: int) -> None:

self._totRec = totRecods

@abstractmethod

def_parser(self, file:str, mode:str) -> None:

pass

@abstractmethod
def writeToFile(self) -> bool:

pass

@abstractmethod

def updateRecord (self, record: ClearingRecord) -> bool:

pass
