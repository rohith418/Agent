import datetime
from pydantic import BaseModel, Field, root_validator
from util.constants import WFC
from util.currencycodes import CURRENCY_CODES
from util.helpers import codeExists, findNgetKeyValue, validateCreditCard
from util.mcccodes import MCC_CODES


class VPBaseResponse(BaseModel):
# createdOn : datetime.datetime - Field(default=datetime.datetime.now())
# lastUpdatedOn: datetime.datetime = Field(default-datetime.datetime.now())
#


createdBy:str
Field(default="VirtupayAPI")
# lastUpdatedBy:str = Field(default="VirtupayAPI")
status:str = Field(default="")
code:str = Field(default="")
message:str = Field(default="")
errors:list[str] = []


class VCNCreaeRequest (BaseModel):
sourcePAN:str = Field(min_length=13, max_length=19, title='PAN')
sourcePANExpiry:str = Field(min_length=4, max_length=4, title- 'PAN Exp Dt (YYMM)", regex=r"Id(4)5")
sourcePANcvv:str= Field(min_length=3, max_length-4, title= PAN CW", regex-r"Id(3,4)$")
vcStartDate
datetime.date
vcEndDate
datetime.date
allowedMCCs:list[str] = Field(default=[], description="List of MCC codes", min_items=1)
vcnAmount: float = Field(ge-0.1, title='VCN Amount")
vcnMultiUse:str -= Field(default="N", title-'Is Mutliuse Card")
vcnCurrency:str = Field(default="840")
vcToleranceUnder:float = Field(default=0.0, le=100, ge=0)
vCToleranceOver:float = Field(default=0.0, le-100, ge-0)
needTokenisedVCN:bool = Field(default=False)


@root_validator ()
def verifyFields(cls, values):
s_dt = values.get("vcStartDate")
e_dt:datetime.date = values.get ("vcEndDate")
if s_dt < datetime.date.today():
raise ValueError(f"start date((s_dt) < (datetime.date.today())) should be greater than today")


if e_dt
r s_dt:


raise ValueError(f"end date((e_dt)) should be greater than start date")


if e_dt > (s_dt + datetime.timedelta(days-WFC.VCN_MAX_NUM_OF_DAYS_VALID)):
raise ValueError(f"end date(fe dt)) should not be greater than start date


X


(WFC. VCN MAX_ NUM_ OF DAYS. VALID?")


strPanExp = values.get("sourcePANExpiry")


try:


dtPanExp = datetime.datetime.strptime(strPanExp,'%y%m")


except:


raise ValueError("Invalid PAN Expiry date')
dtVcnExp = datetime.datetime(e_dt.year,e_dt.month,1)


if dtVcnExp > dtPanExp:
raise ValueError(f"PAN is expiring before VCN ((strPanExp)<(e_dt.strftime("%y%m')>)..")


if len(values.get("allowedMCCs")) > 0:
for mcc in values.get("allowedMCCs"):
if codeExists(MCC_CODES, code=mcc): continue
raise ValueError(f"Invalid MCC (mcc)")


if not validateCreditCard(values.get("sourcePAN")):
raise ValueError(f'Invalid PAN (values.get("sourcePAN"))")
currCode = values.get('vcnCurrency')
if not codeExists(CURRENCY_CODES, isoCode=currCode, code=currCode):
raise ValueError(f'Invalid Currency Code (currCode)')


return values


class VCNCreateResponse(VPBaseResponse) :
Vcn:str = Field(default="")
vcnCW:str = Field(default="")
VcnExpDt:str - Field(default="")
VcnId:str = Field(default="")
pan:str = Field(default="")
VcnType:str - Field(default-"")


class VCNCancelRequest (BaseModel):
vcnId: int = Field(description="unique id of virtual card")
vcn: str - Field(description="Virtual Card Number")


class VCNCancelResponse(VPBaseResponse):
vcnId: int = Field(description="unique id of virtual card", default--1)
vcn: str = Field(description="Virtual Card Number",default='-')
class VCNUpdateRequest (BaseModel):
vcnId: int = Field(description="unique id of virtual card")
vcn: str = Field(description="Virtual Card Number")
sourcePAN:str | None - Field(default=None, description="Only in case if PAN need to be updated",min_length-13, max_length=19, title="PAN'>
sourcePANExpiry:str | None - Field(default-None, description="Only in case if PAN need to be updated",min_length=4, max_length=4, title="PAN Exp Dt(YYMM)", regex=r"ldf4)5
;ourcePANcVV:str | None - Field(default-None, description="Only in case if PAN need to be updated",min_length-3, max_length-4, title-"PAN CW", regex-r"Id(3,4)$"
VcEndDate : datetime.date | None = Field(default=None, description="If VCN Expiry date need to be updated then fill it"
#allowedMCCs:list[str] = []
vcnMultiUse:str | None = Field(default=None)
vcToleranceUnder:float | None = Field(default=None)
vcToleranceOver:float | None = Field(default=None)


@root_validator()
def verifyFields(cls, values):
s_dt
datetime. .date.today ()
e_dt:datetime.date = values.get("vcEndDate")


if e_dt:
if e_dt S_dt:
raise ValueError(f"end date((e_dt)) should be greater than today")
vcn=values.get("vcn")
if vcn and not validateCreditCard(vcn):
raise ValueError(f'Invalid VCN (vcn)')


pan-values.get("sourcePAN")
if
pan:


if not validateCreditCard(pan):
raise ValueError(f'Invalid PAN (pan)')
strPanExp = values.get("sourcePANExpiry")
try:


dtPanExp= datetime.datetime.strptime(strPanExp,'%y%m")


except:


raise ValueError(Invalid PAN Expiry date')
if e_dt:


dtVcnExp = datetime.datetime(e_dt.year,e_dt.month,1)


if dtVcnExp > dtPanExp:
raise ValueError(f"PAN is expiring before VCN ((strPanExp)<[e_dt.strftime("%y%m")))..")


return values


ass VCNUpdateResponse(VPBaseResponse):
vcn:str = Field(default="")
vcnId:str = Field(default="")
pan:str = Field(default="")
