from apitesterui.devhelper import VirtuAPIs
from apitesterui.screenhtmls import Not_found, new_form, list_vcns, get_vcn_tr,MAX_ROWS_IN_DISF
from authtesterui.screenhtmls import AuthPage
from fasthtml.common import *
from hmac import compare_digest
from apitesterui.devmodels import SAMPLE_DATA, VCNRow
from sqlite_minutils.db import Database, Table as DBTable
# required for sqlalchemy:
#from fastsql import *


db:Database = database("dev_data/virtupay1.db')


vcns:DBTable=db.create(VCNRow,pk="id",replace=True)
#vcns:DBTable=db.create(VCNRow,pk="id",if_not_exists=True)


login_redir = RedirectResponse('/login'


status_code=303)
def beto el ea, sess):
#printlf before called: free diet )')
auth = reg, scope auth'] = sess get auth', None)
if not outhi return login reader
vans xt al)
beware = Beto era albero e, skip=f:'(faviconlaico', c'/static/ ti
support - fast and (before but a
exception handle sofala. Not found),
hors-(for 201235(... Sortable"),
Markdown]5( markdown'),
Link/re1= stylesheet, heeft static/style-sheet, css'),


'[, 0807/,


OzPORE = birthplace (200 063
BADD work
def 1ac nf):
from - Form action=/logan', method-'post')(
Input (10= name', placeholder - Name, VALUE= admin),
Input fide and, types password, placeholder. Password, value- admin'),
Button( 100in:))
return Titled( Logan", frm)
@dataclass
class Login: name:str; pwd:str


@rt("/login")
def post(login:Login, sess):
if not login.name or not login.pwd: return login_redir


if not (login.name=='admin' and login.pwd=="admin"): return login_redir
sess['auth'] 'admin
return RedirectResponse(/', status_code=303)


@app.get("/logout")
def logout(sess):
del sess[auth']
return login_redin


@patch


def ft (item:VCNRow) :
#print(item.dict)
rows-get_vcn_tr(item, edit)


return rows


ert("/")
def get(auth):
title - "VirtuPay APIs: VCN list"
print(auth)
top - Grid(H1(title),
Div(A('Authorize', href-'/authorize"),
style='text-align: right'),
Div(A('logout', href=/logout'),
style='text-align: right'))
add Div(Button('Create new VCN', hx_post=addClick, target_id='vne-vcn'),
id='vne-vcn')


frm 1ist_vcns([*vcns(order_by="id desc', limit-MAX_ROWS_IN_DISP)])
card = Card(Div(frm), header-add, footer=Div(id='current-vcn"))
return Title(title), Container(top, card)
@rt
def reorder(id:list[int]):
for i,id in enumerate(id): vcns.update(status=i, id=id_)
return tuple(vcns(order_by='id desc`, limit=MAX_ROWS_IN_DISP))


retTable=vcns.upsert(r_vcn)
sMsg=H3("Card Updated/Saved')
def saveVCN(r_vcn:VCNRow):
retTable:VCNRow = None
print(f'row: (r_vcn)")
if r_ycn.id:
else:
Ørt


resp - VirtuAPIs.createVCN(r_vcn)
if isinstance(resp, VCNRow):
retTable=vcns.insert(resp)
else:
items- ]
for m in resp:
items.append(H3(m))
sMsg=Div(*items)
newCard
if retTable:
+
retTable.VCN), Br(), Label('New VAN CW:


newCard=Div(Label("New VAN:
Br(), Label("New VAN Exp: ' + retTable.VCNExpiry))


+ retTable.VCNcVV),


header - Div(Button('Create new VCN', hx_post=addClick, target id-"vne-vcn')
Br(),sMsg)
return header, newCard


ert
def addClick():
return new_form(saveVCN)


@rt


def remove(id:int):
vcns.delete(id)
return clear("current-vcn')


ert
def edit(id:int):
res = new_form(saveVCN, True)
return fill_form(res, vcns[id])


ert
def replace(r_vcn: VCNRow): return vcns.update(r_vcn), clear('current-vcn')
@rt


def retr(id:int):
r_vcn = vcns[id]


btn = Button('delete'
name='id', value=id, target_id-f'vcn-[r_vcn.id)
hx_post=remove, hx_swap="outerHTML")
return Div(H2(r_vcn.PAN), Div(r_vcn.VCN, c1s="markdown"), btn)


import platform
hName = platform.uname()[1]
serve(host-hName,port=3210)
