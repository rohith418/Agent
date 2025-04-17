import configparser
import logging as LOG


class Config(object):


def init(self, filePath:str):
self._config:dict = dict()
cg = configparser.ConfigParser ()
cg.read(filenames=[filePath])


for section in cg.sections()
sc dict()
for key, value in cg.items(section)
sc[key]=value
self-_config[section]
SiCl


LOG.debug("configuration loaded:


self. _config)


def get(self, section:str, propName:str, default:any-None) -> str | None:
sc:dict = self._config.get(section)
if sc:
return sc.get(propName.lower(.strip())


return default


def getsection(self, section:str) -> dict | None:
return self._config.get(section)
