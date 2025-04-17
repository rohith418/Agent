from dataclasses import dataclass
import datetime


@dataclass
class AuthRow:
id:int
PAN:str
PANExpiry:str
PANcvv:str
VCN:str
VCNExpiry:str
VCNcvv:str
status: str
VCNID:str
VCNTYpe:str
VCNAmount:float
