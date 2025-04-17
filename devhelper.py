from apitesterui.devmodels import VCNRoW
import requests
import json


class VirtuAPIS:


@staticmethod
def createVCN(vcnRow: VCNRow) -> VCNRow I list[str]:
req{
"sourcePAN": vcnRow.PAN,
"sourcePANExpiry": vcnRow.PANExpiry,
"sourcePANcvV": NcnRow.PANCVV
"vcStartDate": vcnRow.VCNStartDate
"vcEndDate": vcnRow.VCNEndDate,
"allowedMCCs": [vcnRow.allowedMCCs]
"vcnAmount": vcnRow.VCNAmount
"vcnMultiUse": "Y" if vcnRow.VCNMultiUse -- "on" else "N"
"vcnCurrency": vcnRow. VCNCurrency,
"vcToleranceUnder": vcnRow.VCNToleranceUnder
"vcToleranceOver": vcnRow.VCNToleranceOver
"needTokenisedVCN": False
}
print(req)


resp = requests.post("http://127.0.0.1:8123/vcn/v1/create',json.dumps(req))
#print(resp, resp.text())
jResp=json.loads(resp.text)
#print(resp.json())
if resp.status_code==200:
if jResp['status']=-'200" and jResp['code'].upper ()=- 'SUCCESS':
vcnRow.VCN = jResp['vcn']
vcnRow.VCNcVV = jResp['vcnCW']
VcnRow.VCNExpiry = jResp['vcnExpDt"]
vcnRow.VCNID= jResp['vcnId']
vcnRow.VCNTYpe= jResp["vcnType']
return vcnRow
elif resp.status_code==422:
errs=[]


for item in jResp[`detail']:
errs.append(item["msg'])
return errs
else:


raise Exception(f'Unhandled Server Error with response codetresp.status_code): (resp.text}')
