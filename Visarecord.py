from clearinglib.transactions.record import ClearingRecord

class VisaClearingRecord (ClearingRecord):

def _init_(self, deJson:dict, runmode: str) -> None:

super().init(de]son-delson, runmode=runmode)

self.CardType = "0"
