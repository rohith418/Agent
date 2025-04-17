import os
from fasthtml.common import*
from fasthtml components Import (51 Icon, 51 button, 51 ment, Smithy Item, 51 menu Item, 51 menu item,
51 breadcrumb, 51 breadcrumb Item, 51 breadcrumb item, SI card, S) Input, 51 form)
#from virtues models cardmodels import VCNCreateresponse, VCNCreateRequest
Import datetime
from pedantic import baselloaded, field, root validator
from sqlite minute's do import Database, Table as DbTable, DEFAULT, foreignkeys Type, Default, over, able, ottointerior
dataClass
Class VCN Row
Id: int
PAN: Str
PANERAI y Str
PANcvv: Str
db - Database( data/virtupay.db')
db['vcn_cards'].create((


id':int,


PAN':str,


'PANExpiry':str,


PANcvV istr


VCN':str,


mx


VCNExpiry':str,
VCNcvv':str,
VCNStartDate


datetime.date,


VCNEndDate


datetime.date,


'allowedMcCs':str,
VCNAmount": float,
VCNMultiUse':str,


VcNCumrency " stn"
VCNToleranceUnder ":float,
VCNToleranceOver':float
VCNTokenised":bool,
status
str.


1, pk="id", if_not_exists=-True) #replace=True)
try:


# #TTTw


pr int (db["ven_cards"].get(2))
except NotFoundError as e:
print("Record not found')


def sl_link(*args, *kwargs): return(jsd('@shoelace-style',


shoelace


def beforeFunct(req, sess):


cdn'


*args, prov="npm', **kwargs))
def beforeFunct(req, sess):


pass


app FastHTML(


# before= Beforeware(beforeFunct,
skip-[r'/faviconI.ico', r'/scripts/.*"


r'.*I.css', r",*I.js']
# ),
hdrs=(
Meta(charset='UTF-8'),
Meta(name=`viewport', content='width=device-width, initial-scale=1.0"),
sl_link ("themes/light.css', typ='css').
sl link( shoelace- autoloader .js' type= module
Script(src='https://cdn.tailwindcss.com').
Link(rel=`stylesheet', href-'static/style-sheet.css"),
))
rt = app.route


d=f`fos.getcwd())\ldevtools|lapitesterui\/static
#print(d)


app.routes.append(Mount("/static`, app=StaticFiles(directory=d), name='static'))


def icon(nm, text, **kw): return S1_icon(slot="'prefix', name=nm, **kw), text
def menu(nm, text, path): return Sl_menu_item(*icon(nm, text), cls='rounded-md', hx_get-path)
def breadcrumbs (*crumbs): return S1_breadcrumb(*map(S1_breadcrumb_item, crumbs))
def make_add_newbn(): return S1_button(icon("credit-card-2-front', 'Create New VCN'),variant-'primary', size= small', cls='mr-2",hx_get='/list-cards hx_target='*details')
@rt('/")
def get ():
return Title('VirtuPay Dev Tools'), Div(
Header (
Div(*icon("tools', 'VirtuPay Dev Tools', cls='mr-2'),
cls='text-xl font-bold flex items-center'),
Div(
Nav(
S1 menu(


menu('house-door', 'Dev Tools', '/devtools')
# menu('graph-up', 'Analytics', '/rev').
menu(credit-card', 'Card APIs', '/list-cards")
menu('check-circle`, 'Authorise VCN', '/auth-vcn')
menu('gear', 'Settings', '/settings')
), hx_target='#toolDiv', cls='w-64 bg-white border-r border-gray-200 p-4 overflow-y-auto')
Main(
breadcrumbs('Home', 'Dev Tools').
Hl("Welcome to VirtuPay Dev Tools", cls-'text-2x1 font-bold mt-4 mb-2")
P("Dev Tools are helpful for debugging and validating VirtuPay Services in non Production Environment.", cls="mb-8").
Div(make_add_newbn(),id="details')
Div(list_vcns(), id='toolDiv', cls-'grid grid-col5-1 md: grid-cols-1 lg:grid-cols-1 ),
cls-"flex-1 p-8 overflow-y-auto
cls='flex flex-1 overflow-hidden'),
cls-'h-full flex flex-col bg-gray-50")


@rt('/det1')
def get(title:str): return Div(f'Details for ftitle)")


def show_vcn_card(item):
#new_inp = Input (id="new-title", name="title", placeholder-"New Todo")
# add = Form(hx_post=create, target_id="details', hx_swap="afterbegin")(
Group(new_inp, Button("Add")))
add l_form(
Hidden(id='id', name='id' )
51_input(id="PAN', placeholder='PAN Number', name='PAN', label-"PAN:', clearable=true)
S1_input(id-"PANExpiry', placeholder='YYMM', name='PANExpiry', label-'PAN:', clearable=true)
51_input(id="PANcvv', placeholder-'PAN CW", name="PANcVY', label="PAN CW:', clearable-true), Br(),
S1 _button(
*icon('question-circle", 'Save'),
variant='primary', size='small', cls='mr-2", type-'submit",hx_post='/create", hx_target-'#details')#, hx_swap="afterbegin")
)
return S1_card(
add,
      cls='flex flex-col justify-between')


hx_target


def list_vcns():
#return show_vcn_card('Total Users'
data = [
("vcn': '4545454545454545
('vcn': '4545343454543456'
('vcn': "4545453600343201"
f'vcn': '4545423608002102.


"1,234',


"+5.2% from last week')


"cvv':"343',
`cvv': '674'
'cvv':'894"
'cVv':'500'


exp': '2512°
'exp':"2701"
exp':'2611"
exp':'2505


pan': '4102323232323222'),
pan': "4102323232323222'),
pan': 4102323232323222"),
pan': "4102323232323222'),


J


tbHeaders - ['VCN CARD', 'VCN CW', 'Exp Dt', 'PAN', "Edit']
headers = Tr(*[Th(tt, cls='styled-table-thead-td') for tt in tbHeaders])

editBtn=Td(5l_button(icon("pencil-square', 'Edit', ),variant='primary', size='small', cls='mr-2", hx_get='/list-cards,hx_target='#details'),cls-'styled-table-tbody-td')
rows = [Tr(*[Td(str(item[key]),cls='styled-table-tbody-td') for key in item.keys()], editBtn) for item in data]
table = Table (Thead(headers), *rows, cls='styled-table')
return Div(table
style="width:100%")
@rt(/devtools')


def get(): return list_vcns()
@rt(/list-cards')
def get(): return show_vcn_card(["Revenue', '$12,345', "+2.4% from last month'])
@rt('/auth-vcn')
def get(): return show_vcn_card('Revenue', '$12,345", "+2.4% from last month')
@rt("/settings')
def get(): return show_vcn_card( "Active Projects', "42', "3 new this week)
@rt("/create")
def post(data:VCNRow, sess):
print(data, sess)
return Div(H1('Data Saved'))
serve(host="localhost', port=3210)
