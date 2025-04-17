from .devmodels import VCNRON
from fasthtml.common import Titled, Div, Hidden, Label, Input, Group, Form, Button, Table, Thead, Tr, Th, Ta


def Not_found(req, exc): return Titled(`Oh no!', Div('We could not find that page :("))


def new_fields(edit,**oob):
return Div(


Div("Edit VCN:', Hidden(id='new-id`, name-'id")) if edit else Div("Create New VCN')
_abel('PAN', Input(id="new-PAN", name="PAN", placeholder= "PAN", type-"number", value="4123456789012349")),
Label("PAN Expiry Date', Input(id="new-PANExpiry", name-"PANExpiry"," placeholder-"YYMM"",type="number', value='2612")),
Label("PAN CV', Input(id="new-PANcV.", name="PANcv", placeholder="3 Digit", type-"humber", value="234")),
Hidden(id="new-VCN", name="VCN")
Hidden(id="new-VCNExpiry", name="VCNExpiry")
Hidden(id="new-VCNcvv", name="VCNcVV").
Label("VCN Start Date', Input(id="new-VCNStartDate", name="VCNStantDate", type="date"))
Label("VCN End Date', Input(id="new-VCNEndDate", name="VCNEndDate", type="date"))
Label('MCC', Input(id="new-allowedMCCs", name="allowedMC@s", placeholder="MCC", type="number", value='3001`)).
Label("VCN Amount', Input(id="new-VCNAmount", name-"VCNAmount", placeholder="Amount", type="number')),
Label('Multi use', Input(id="new-VCNMultiUse", name="VCNMultiUse", type-"checkbox"))
Hidden(id="new-VCNCurrency", name="VCNCurrency", value="840"),
Group(Label('Tolerance', Input(id="new-VCNToleranceUnder", name="VCNToleranceUnder", placeholder="Under", type="number', value="5")).
Label(-",Input(id="new-VCNToleranceOver", name="VCNToleranceOver", placeholder="Over", type="number', value='5"))
),
Hidden(id="new-VCNTokenised", name="VCNTokenised", value="false')
Hidden(id="new-status", name="status", value="A")
id-'form-fields', soob


def new_form(hxPost, edit=False, **oob):
new_inp = new_fields(edit, **oob)
add = Form(hx_post=hxPost, target_id="vne-vcn')(#, hxlswap="afterbegin"
new_inp,Group(
Button("Add") if not edit else Button("Save")


return add


DISP_FLDS = ["VCN": 'VCN', 'VCNcvV': 'VCN CVV', "VCNExpiry":"Exp Dt", "PAN": "PAN")
MAX_ROWS_IN_DISP = 20
def list_vcns (data):
neaders Tr(*[Th(tt, cls='styled-table-thead-td') for tt in DISP_FLDS.keys()],Th("Edit", cls='styled-table-thead-td'))
table = Table(Thead(headers), *data, cls-"styled-table")
return Div(table
style='width:100%")
def get_vcn_tr(item:VCNRow, editAction):
rows Tr(*[Td(str(item._getattribute_(key)),cls='styled-table-tbody-td') for key in DISP_FLDS.keys()],
Id(Button("Edit', hx_post=editAction.rt(id=item.id), target_id='vne-vcn'),cls='styled-table-tbody-td'))
return rows
