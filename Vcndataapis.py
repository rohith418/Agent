from db.dbmanager import DBManager
import psycopg2
from psycopg2.extras import Json
import datetime
import logging as LOG
from util.constants import WFC


def


dictDateToStr(d:dict)->dict:
for key, obj in d.items():
if isinstance(obj, (datetime.date, datetime.datetime)):
d[key]-obj.isoformat()
return d


class VCNDataAPIS:
binrange: dict = None


@staticmethod
def getBinRange() -> dict | None:
Retrieve data from the bin range table
if not (VCNDataAPIs._binrange -- None):
return VCNDataAPIs.__binrange
else:
try:


with DBManager.getConn() as conn:
with conn.cursor()
as cur:
Str501- "" UPDATE of ICE dot pan master SET pan cry-(s), pan exports) WHERE san ada's,
car executestrial, pan erv, pan exp, pan 101)
print! The number of updated PANS: ", our nowcount)
I COMMIT the changes to the database
conn commie ()
return cur. rowcount
except (Exception, psycopg2.DatabaseError) as error:
LOG.error(f'failed update pan: (error)')
raise error


return


@staticmethod


def insertVCN(vcNumber, values:list):
insert data into the VAN table
can_id
I
-1
try:
with DBManager.getConn() as conn:
with conn.cursor() as cur:
strSQL="""INSERT INTO wf_vcg_db.t_vc_master(
C_num, vC_cv, vc_exp, pan_id, binrange_id, status, created_at, updated_at, currency_id, vc_amt, multiuse, tolerance_min, tolerance_ max,
treated by, modified_by, valid_from, valid_till, fraud_code, debit_count, credit_count, last_auth_dt, last _clearing_dt, merchant_name, merchant id.
tx_limit, overall_limit, auth_count, clearing_count, auth_amount, crearing_amount, vc_flag
VALUES (?, ?, ", ?, ?, ?, 2, 2, 2, 2, ?, ?, ?, 2, ?, ?, ?, ?, ?, 3, ?, 2, ?, 2, 2, 2, 2, 2, ?, ?, >) RETURNING vc_id;""
cur.execute(strSQL, values)
print("The number of VANs inserted: ", cur.rowcount)
row = cur.fetchone()


if row:
can_id
row[0]


commit the changes to the database
#
conn. .
commit(


xcept (Exception, psycopg2.DatabaseError) as error:
print(error)
finally:


return can_ id
@staticmethod
def cancelVCN(vcnId:int):
update data into the vc table


try:
with DBManager.getConn() as conn:
with conn.cursor() as cur:
strSQL="""UPDATE wf_vcg_db.t_vc_master
SET status=(%s), updated_at=now() WHERE vC_id=(%s);""
cur.execute(strSQL, [WFC.CANCELLED, vcnId])
LOG.debug(f"The number of vcn updated: ( cur.rowcount?")


commit the changes to the database
#
conn.commit()


except (Exception, psycopg2.DatabaseError) as error:
LOG.error(f'Cancel VCN failedferror)')
raise Exception( Cancel VCN Failed due tob error')


@staticmethod
def updateVCN(vCnId:int, columvalues:dict):
update data into the vc table """
if columvalues:
if len(columvalues.items()) - 0:
raise Exception("No valid attributes updated in the request")
LOG.debug(f'updateVCN: (columvalues)")
else: raise Exception("No values updated in the request")


liCols
[]
liValues=[]


for key, val in columvalues.items():
liCols.append(key
=(%s), ')
liValues.append(val)


strSQL=""'UPDATE wf_vcg_db.t. vC_master
SET
+
join(liCols) +


updated_at-now() NHERE vc_id=(%s);""


liValues.append(vcnId)
try:


with DBManager.getConn() as conn:
with conn.cursor( as cur:


cur.execute(strSQL, liValues)
LOG.debug(f"The number ofvcn updated: t cur.rowcount)")


commit the changes to the database
#
conn. commit()


except (Exception, psycopg2.DatabaseError) as error:
LOG.error(f'Update VCN failed(error), (strSQL)")
raise Exception("Update VCN Failed due to db error')
