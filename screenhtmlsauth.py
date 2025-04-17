from apitesterui.devhelper import VirtuAPIS
from .authmodel import AuthRow
from apitesterui.devmodels import VCNRow
from fasthtml.common import Titled, Div, Hidden, Label, Input, Group, Form, Button, Table, Thead, Tr, Th, Td, Container, Grid, Card, H1, A, H4, Title, Textarea
from fasthtml import FastHTML, Routex
from fasthtml.live_reload import FastHTMLWithLiveReload
from sqlite_minutils.db import Database, Table as DBTable
from socket import socket
import json
import random as
rn
DISP_FLDS


('VCN': 'VCN"
MAX_ROWS_IN_DISP = 20


VCNcvV*: "VCN CVV"


VCNExpiry":'Exp Dt"


PAN:"PAN", "PANExpiry":"PAN Exp Dt'


PANcVV': "PAN CWV')


class AuthPage:


def _init(self, app:FastHTML | FastHTMLWithLiveReload, db:Database) -> None:
self.app app
self.db = db
self.authTable:[BTable = None
self.VCNTable:DBTable = None
self.__initDB()
self.app.router.add_route('/authorize',self.authorize,["get",'post"],'authorize')
self.app.router.add_route('/payvcn',self.doAuthrization,["post"],'payvcn')
pass
def _initDB(self):
self.authTable:DBTable=self.db.create(AuthRow,pk="id",replace=True)
self.VCNTable = self.db.tables[0]
print(self.VCNTable, self.authTable)
#selfauthTable:DBTable=self.db.create(AuthRow,pk="id",if_not_exists=True)
#self.db.query


def authorize(self, auth):
title = "Authorize Service: Payments"
print(auth)
top - Grid(H1(title)
Div(A("Virtual APIs', href="/"),
style='text-align: right'),
Div(A("logout`, href='/logout'),
style='text-align: right'))
frm = self.new_form()
card Card(Div(frm, id="auth-form'), header=H4('Do Payment wtih VCN:'), footer=Div(id="list-auths'))
return Title(title), Container(top, card)


def new_fields(self, edit,**oob):
return Div(
Div("Pay through VCN:', Hidden(id="new-id", name='id")) if edit else Div("Create New VCN'),
Label("VCN', Input(id="new-VCN", name="VCN", placeholder="VCN", type='number', required="true", pattern="^\df16)$")),
Label('VCN Expiry Date', Input (id="new-VCNExpiry", name-"VCNExpiry", placeholder="YYNM" ,type='number', required="true", pattern="^\d(4)S")).
Label("VCN CVV', Input (id="new-VCNcV", name="VCNcv", placeholder="3 Digit", type='number', required="true", pattern="^\d(3]S")).
Hidden(id="new-PAN", name="PAN")
Hidden(id="new-PANExpiry", name="PANExpiry")
Hidden(id="new-PAdcvy", name="PANcVY").
Hidden(id="new-status", name="status")
Hidden(id="new-VCNID", name="VCNID")
Hidden(id="new-VCNTYpe", name="VCNTYpe")
Label('VCN Amount', Input (id-"new-VCNAmount", name="VCNAmount", placeholder="Amount", type='number', step="any", required="true").
id='form-fields', **oob
)
def new_form(self, edit-False, **oob):
new_inp - self.new_fields(edit, **oob)
frm = Form(hx_post="/payvcn', target_id="auth-form')(
new_inp,Group(


Button("Authorize") if not edit else Button("Re-Authorize")
)
)
return frm
def doAuthrization(self, r_auth:AuthRow);
print(f"row: [r_auth)')
sMsg=H4("VCN Auth Response:")
retTable = None
# if r_auth.id:
#, retTable=self.authTable.upsert(r_auth)
# else:
resp- VirtuAPIs.createVCN(r_auth)
#
# if isinstance(resp, AuthRow):
#
retTable-self.authTable.insert(resp)
#
else:
#
items=[]
print(resp)
#
for m in resp:
#
items.append(H4(m))
#
sMsg=Div(*items)
ARN = rn. randint (10000000000o, 999999999999)
inMsg = 'DE11': '000812"
DE126": "0040000000000090F1F04943".format(r_auth.VCNcvv.encode("cp500).hex(>.upper()),
'DE126_SUBFLDS': ('DE10': '10 ()".format(r_auth.VCNcv)),
'DE14': r_auth.VCNExpiry
'DE18`
'3001"
E
'DE19': '0826'
'DE2': r_auth.VCN,
'DE20" :"0840",
DE22': '0120"
DE25': '08'
DE3': '000000'
DE32
493488"
DE37": str(ARN)


DE4': "(:13.2f)".format(r_auth.VCNAmount).replace(" ','0').replace(".','")


'DE40': '101".
'DE41: "98123456"
DE42': "99999999999999
'DE43': "PayPal
Arizona
US'
DE43.1": "PayPal


'DE43.2": 'Arizona
'DE43.3': 'US'
'DE49": "0840"
'DE7':
" 0808110000.
'MTI': '0100"3


ベ


inMisg = json.dumps(inMsg).replace(",,',In')# inMsg.format(r_auth.VCNcvv.encode("cp500").hex(),r_auth.VCNcvw.


isoOutMsg
vcnFound = False
row: VCNRow = None
for row in self.VCNTable.rows:
if r_auth.VCN == row['VCN']:
vcnFound = True
break
appAmount=0.0
resCode = '00'
cvvMatch = 'M'
pan = 000000000000000e
panExp
"


'0000
if vcnFound:


print(row["PAN'],row["PANExpiry"],row['VCNcvv`],row['VCNAmount'])


pan = row["PAN']
panExp = row['PANExpiry']
appAmount - float(row["VCNAmount'])


if r_auth.VCNAmount > float(row['VCNAmount']):


resCode
"51°


if r_auth.VCNcV != row['VCNcvv']:
resCode
=


'63
cvvMatch='N'


if int(r_auth.VCNExpiry) !- int(row['VCNExpiry"]):


resCode- 54
else:
resCode
'14"
cvvMatch='N'


=


outMsg
f
DE102': r_auth. VCN,
DE11': '000812"
'DE14': panExp.
'DE18': '3001"
DE19': '0826'
DE2': pan,
'DE20': '0840'
"DE22' : '0120'
DE25': '08'
DE3': '000000
DE32': '493488
DE37': str(ARN)
DE39': resCode,
DE4': "(:13.2f>".format(appAmount).replace("",'@").replace(".","").
DE40'
"101"
DE41`: '98123456"
DE42': '99999999999999
'DE43': 'PayPal
DE43.1': 'PayPal.         '
DE43.2": "Arizona
DE43.3":'US"
DE44: '5


Arizona


US"


DE44 SUBFLDS': (


+cvvMatch,
DE1": '5"
DE2':
DE3':
DE4:
.


DE10": cvvMatch,


'DES':
DE6': "
'DE7': "
'DE8": "
'DE9: "


DE49": "0978'.
'DE7": '0808110000",
"MTI':
0110


isoOutMsg= json.dumps(outMsg).replace(',',',In')


header - Div(sMsg,
Label("Auth Request Message:', Textarea(inMsg, cols-100, rows-15)
),
Label(`Auth Response Message:',Textarea(isoOutMsg, cols-100,
rows-15)
),
Button(A("New Auth Request", href='/authorize, style-'color: white'))


return


header


def list_vcns(self, data):
headers Tr(*[Th(tt, cls=`styled-table-thead-td') for tt in DISP_FLDS.keys()],Th("Edit', cls='styled-table-thead-td')
table = Table(Thead(headers), *data, cls='styled-table')
return Div(table
style='width:100%")


def get_vcn_tr(self, item:AuthRow, editAction)
rows = Tr(*[Td(str(item._getattribute_(key)),cls='styled-table-tbody-td') for key in DISP_FLDS.keys()].
Td(Button('Edit', hx_post=editAction.rt(id=item.id), target_id="auth-form"),cls="styled-table-tbody-td"))


return rows
