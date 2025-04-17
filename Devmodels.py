from dataclasses import dataclass
import datetime


@dataclass
class VCNROW:
id:int
PAN:str
PANExpiry:str
PANcvv:str
VCN:str
VCNExpiry:str
VCNcvv:str
VCNStartDate : str
VCNEndDate : str
allowedMCCs:str
VCNAmount: str
VCNMultiUse:str
VCNCurrency:str
VCNToleranceUnder:str
VCNToleranceOver:str
VCNTokenised:bool
status: str
VCNID:str
VCNTYpe:str
SAMPLE_DATA=[("id":1,"PAN":"3535506278211044","PANExpiry":"2901","PANcvv":101,"VCN":"3581925761061554","VCNExpiry":"2506", "VCNcvv":555,"VCNStartDate":"2025-02-04", "VCNEndDate":"2025-04-05", "VCNAmount":5977.52,"VCNCurrency":840,"VCNToleranceUnder":0.75,"VCNToleranceOver":4.2,"VCNTokenised":False,"status":"A"},
Sample data needs to enter
