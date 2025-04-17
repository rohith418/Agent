import argparse
import sys
from db.dbmanager import DBManager
from multiplex.clientsocketthread import ClientSocketHandlen
from util.config import Config
from util.wfcryptomanager import WFCryptoUti]


Raw


Blar


class MainVCG:
def init_(self, fileConfig: str, env:str="dev') -> None:
self.env
env
self.config:Config = Config(fileConfig)


self.listThreads:list = ]


#Initialize cryptors: Without this Cryptors can'be used as keys are there in keystore
WFCryptoutil().initialize(self.config)
DBManager.initConfig(self.config)


def start(self):
for i in range(2):
host = self.config.get("tsys.servers", str(i)+".host")
if host != None and host !=
port = self.config.get("tsys.servers", str(i)+".port")
cs = ClientSocketHandler (host, int(port), f"client(i)")
cs.start()
self.listThreads.append(cs)
#cs.join()


def stop(self):
for cs in self.listThreads:
cs:ClientSocketHandler
cs.terminate()


cS


if


name_


#


main__'


print("server starting..")
parser - argparse.ArgumentParser(description=""'Wells Fargo Commercial Cards - Virtual Card Authorization service
This is IS0 Client connects to TSYS servers to process iso messages "")
parser. add argument(- -env',
help= environment for running sewtice
parser.add_argument("-config, help='Full path for config file", required-False)
like dev/sit/uat/prod /bcp
required=True)


args
parser .parse_ _args()


print("server args", args)


conFile
"app-config.ini"


if args. config:
conFile = args.config


vcg= MainVCG(conFile, args.env)
try:
Vcg.start ()


#Keeping the process alive
while True:
user_input = input("Enter something (Ctrl+C to exit): ")
print(f"You entered: (user_input)")
except KeyboardInterrupt as kex:
print("Key interrupt", kex)
vcg.stop()
sys.exit()
except Exception as ex:
print("other Exception", ex)
raise ex
