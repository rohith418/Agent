from virtupay.controlers.cardhelper import CardHelper
M
from util.constants import WFC
from virtupay.controlers.vcndataapis import VCNDataAPIs
import logging as LOG


class VirtuPay:
def _init(self) -> None:
pass


def getPANmappedBinRange(self, pan: str) "-> tuple:
rows - VCNDataAPIs. getBinRange(
if rows is not None:
for br in rows:
if pan.startswith(br[4]):
return br


raise Exception(f"Bin range not configured for pan: (pan[:5]


def createCard(self, inMsg: VCNCreateRequest) -> VCNCreateResponse:
LOG. info(f'binrange-(binRange)")
binRange - self.getPANmappedBinRange(inMsg.sourcePAN)
if binRange is not None:
vcnPrefix = binRange[2]
binRangeID - binRange[3]
vcnLength - binRange[5]
vcnReady- False
vcn ='


maxTryGenVCN = S
tried =
while maxTryGenVCN > tried:
vcn CardHelper.generateVCN(vcnPrefix,vcnLength)
rs - VCNDataAPIs.findVCN(vcn)
#print(rs)
if rs == None:
vCnReady
=


True
break
tried =tried+1
if not vcnReady:
raise Exception(f'failed to generate unique van for (maxTryGenVCN) times")


cVV
CardHelper.generatecW(3)
expDt = inMsg.vcEndDate.strftime(WFC.STR_FORMATS.EXP_DATE)


LOG.debug(f"virtual card generated: (vcn, cvv, expDt)")


copyMsg inMsg.dict_.copy()
copyMsg["vcNum']=vcn
copyMsg["vcCVV']=cvv
copyMsg['VCEXP']=expDt
copyMsg['binrangeID']=binRangeID


succesISON - VCNDataAPIs.createAndAssingVCN(copyMsg)


return VCNCreateResponse(status=200, code='SUCCESS', vcn=vcn,
else:
LOG.error("Bin range not configured for requested pan')
raise Exception("Bin range not configured for requested pan")


vcnCW=cvv, vcnType=1, vcnExpDt=expDt, vcnId-succes]SON[1])


return VCNCreateResponse (status=201, code="Failed", message="")


def cancelard(self, inMsg: VCNCancelRequest) -> VCNCancelResponse:
if inMsg.vcn !-
...


vcnRow = VCNDataAPIs .FinVCNByID(inMsg.VcnId
if vcnRow:
if vcnRow[1]!- inMsg.vcn:
raise Exception(f'VCN and VCN ID combination is not matching with our record!')
elif vcnRow[2] in (WFC.VCN_STATUS.AUTHORISED, WFC.VCN_STATUS.CANCELLED, NFC.VCN_STATUS.EXPIRED, WFC.VCN_STATUS.SETTLED, WFC.VCN-STATUS SETTLEMENT_IN_PROGRESS):
raise Exception(f"VCN can not be cancelled as the status is (vcnRow[2])!") #TODO-Convert status to readable
else:


VCNDataAPIs.cancelVCN(inMsg.vcnId)
return VCNCancelResponse (status= '200. ^ code= SUCCESS" "
vcn-inMsg.van, vcnId-inMsg .vcnId)


else:
return VCNCancelResponse (status='401"


code='FAILED', message-f"Card with id (inMsg.vcnId) not found")


else:
raise Exception(f'Both ID and


VCN are required cancel')


return VCNCancelResponse(status="401",


code= 'FAILED'


message="Unknown response")


def updateCard(self, inMsg: VCNUpdateRequest) -> VCNUpdateResponse:
if inMsg.vcn != ":
vcnRow = VCNDataAPIs.findVCNByID(inMsg.vcnId)
if vcnRow:
if vcnRow[WFC.VCN_MASTER_COLS.vC_num] != inMsg.vcn:
raise Exception(f"VCN and VCN ID combination is not matching with our record!')
elif vcnRow[WFC.VCN_MASTER_COLS.status] in (WFC.VCN_STATUS.AUTHORISED, WFC.VCN_STATUS.CANCELLED, WFC.VCN_STATUS.EXPIRED, WFC.VCN_STATUS.SETTLED, WFC.VCN_STATUS
raise Exception(f'VCN can not be updated as the status is (vcnRow[WFC.VCN_MASTER_COLS.status])!') #TODO-Convert status to readable
else:
colVals -
panUpdated - False


if inMsg.sourcePAN != None and len(inlsg.sourcePAN) > 13:
if inMsg.sourcePANcVV -- None or inMsg.sourcePANcVV =-
or inMsg.sourcePANExpiry == None or inMsg.sourcePANExpiry =-
raise Exception( When updating PAN for your VCN, you have to provide both CVV/Exp date')
panID=-1
panRow = VCNDataAPIs.findPAN(inMsg.sourcePAN)
if panRow and panRow[WFC.PAN_MASTER_COLS.pan_id]:
# colVals[`pan']=inMsg.sourcePAN
# colVals['pan_cvv`]=inMsg-sourcePANcvv
# colVals['pan_exp"]-inMsg.sourcePANExpiry
panID-panRow[WFC.PAN_MASTER_COLS.pan_id]


VCNDataAPIs.updatePAN(panID, inMsg.sourcePANcvv, inMsg.sourcePANExpiry)
if panRow[IFC.PAN_MASTER_COLS.pan_cvv]!=inMsg.sourcePANcvv or panRow[WFC.PAN_MASTER_COLS.pan_exp]!=inMsg.sourcePANExpiry:
panUpdated = True


else:


panID = VCNDataAPIs.insertPAN(inMsg.sourcePAN, inMsg.sourcePANcvv, inMsg.sourcePANExpiry, WFC.PAN_STATUS.PAN_ACTIVE)
panUpdated = True


if panID != -1 and panID != int(vcnRow[WFC.VCN_MASTER_COLS.pan_id]):
colVals[pan_id']=panID


if inMsg.vcnMultiuse and inMsg.vcnMultiuse!=vcnRow[WFC.VCN_MASTER_COLS.multiuse]:
colVals['multiuse']=inMsg.vcnMultiUse
colVals[ vc_flag'
WFC.VCN_F FLAG.MULTIY_ AUTH if inMsg vcnMultiUse== 'Y else WFC. VCN_FLAG. SINGLE_ AUTH


if inMsg.vcEndDate and isinstance(inMsg.vcEndDate, (datetime.date, datetime.datetime)):
if inMsg .VcEndDate.strftime(WFC.STR_ FORMATS. .DATE_ ONLY)!= datetime. date. strftime(vcnRow[HFC. VCN MAS TER,. COLS.valid till],NFC.STR FORMATS. DATE_ ONLY):
colVals["valid_till']=inMsg.vcEndDate
colVals['vc_exp']=inMsg.vcEndDate.strftime(WFC.STR_FORMATS.EXP_DATE)


if inMsg.vcEndDate < datetime.date.today():
colVals[status'] = WFC.VCN_STATUS.EXPIRED
if inMsg.vcToleranceUnder and inMsg.vcToleranceUnder!=vcnRow[WFC.VCN_MASTER_COLS.tolerance_min] and inMsg.vcToleranceunder > 0
colVals["tolerance_min']=inMsg.vcToleranceUnder


if inMsg.vcToleranceOver and inMsg.vcToleranceOver!=VcnRow[WFC.VCN_MASTER_COLS.tolerance_max] and inMsg.vcToleranceOver > 0:
colVals["tolerance_max']-inMsg.vcToleranceover
colVals['overall limit']=float(vcnRow[WFC.VCN_MASTER_COLS.VC_amt]) + insg.vcToleranceover


try:
VCNDataAPIs.updateVCN(inMsg.vcnId, colVals)
return VCNUpdateResponse(status='200", code-"SUCCESS', message="SUCCESS", vcn=inMsg.vcn, vcnId=inMsg.vcnId)
except Exception as e:
LOG.error(f'update error: (e)")
if panUpdated:
return VCNUpdateResponse(status="200", code="SUCCESS
message="PAN UPDATED, But seems like no other fields updated"
(e)1
errors=[f'Error:
vcn=inMsg.vcn, vcnId=inMsg.vcnId)
else:


return VCnupdateResponse(status="201", code='FAIlEd'
message="Failed updated VCN"
errons=[f'Error: (e)'])


else:
raise Exception(f'Both ID and VCN are required cancel')


return VCNUpdateResponse(status='401


code='FAILED


message="Unknown response")
