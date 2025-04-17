import sys
import


time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from util.wfcryptomanager import WFCryptoUtil
from virtupay.virtualpay import VirtuPay
from virtupay.models.cardmodels import * #VCNCancelRequest, VCNCancelResponse, VirtuCardReqMessage, VirtuCardResMessage
import logging
from util.config import Config
from db.dbmanager import DBManager


Raw
Blame


logging.basicConfig(
stream-sys.stdout,
level-"INFO"
format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s]:%(message)s"
datefmt="%d/%b/%Y-%H:%M:%5"


logging.info("VirtuPay starting..")


config:Config Config("app-config.ini")


logging.info(f"Initializing Crypto Manager..")


#Initialize cryptors: Without this Cryptors we can't use encryption keys are there in keystore
WFCryptoUtil().initialize(config)


DBManager.initConfig(config)
logging.debug(f"Datasetting: [DBManager.DBConnPoolSettings)")


Software


WF-Ref


vpapp - FastAPI(
title="WF VirtuPay"


description="Wells Fargo Virtual Cards APIs (Create/Cancel/Update etc.,)".
version-="1.0.0"
docs_url="/"


# vpapp.add_middleware(
CORSMiddleware,
# allow_credentials=True,
# allow_methods=["*"],
#
allow_origins=[
#
"http://localhost:3000


#@vpapp.middleware('http')
async def add_process_time_header(req: Request, call_next):
stime = time.time()
response = await call_next(req)
processTime = time.time() - stime
response.headers["X-Process-Time"]=str(processTime)
response.headers['server']="WF-VirtuPay
return response


@vpapp.post("/vcn/v1/create")
async def create(inMsg: VCNCreateRequest) -> VCNCreateResponse:


try:


return VirtuPay().createCard(inMsg)
except Exception as err:
v-VCNCreateResponse(status- |201
code- Failed' message- Failed')
v.errors=[f'Error: ferr?"]
return v


@vpapp-post("/vcn/v1/cance1')
async def cancel(inMsg: VCNCancelRequest) -> VCNCancelResponse:
try:
return VirtuPay() .cancelCard(inMsg)
except Exception as err:
v=VCNCancelResponse(status='201",code='Failed', message='Failed')
v-errors-[f'Error: (err)']
return v
@vpapp.post("/vcn/v1/cancel`)
async def cancel(inMsg: VCNCancelRequest) -> VCNCancelResponse:
try:


return VirtuPay().cancelCard(inMsg)
except Exception as err:


V=VCNCancelResponse(status="201",code='Failed", message="Failed')
v.errors-[f'Error: (err)"]
return V


@vpapp.post("/vcn/v1/update')
async def update(inMsg: VCNUpdateRequest) -> VCNUpdateResponse:
try:


logging.info(f'(inMsg)')
return VirtuPay().updateCard(inMsg)
except Exception as err:


v=VCNUpdateResponse(status='201`,code='Failed', message= 'Failed*)
v.errors=[f"Error: ferr)']
return V


if


name
main__":
"
import uvicorn
uvicorn.run(vpapp, port=5555)
