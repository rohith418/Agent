from agents.baseagent import BaseAgent

from util.observe import Observable

from agents.agent0100 import Agent0100

from agents.agent0120 import Agent0120

from agents.agent0400 import Agent0400

class AgentManager (Observable):

AgentManager provides pool of agents """Agents are message processors,

Its has below Static methods

get(mti:str)--> Provides Agent based on MTI"""

_shared_instance = None

_agents:dict = dict()

def_new_(cls):

"""virtual private constructor"""

if cls._shared_instance is None:

cls.shared_instance =  super()._new(cls)

cls._shared_instance._initAgents()

return cls._shared_instance

def _initAgents(self):

agM1 = Agent0100()

ag112 =  Agent0120()

agM3 = Agent0400()

self._agents["0100"] = agM1

self._agents["0120"] = agM2

self._agents["0400"] = agM3

self._agents["0420"] = agM3

self._agents["0101"] = agM1

self._agents["0121"] = agM2

self._agents["0401"] = agM3

self._agents["0421"] = agM3

@staticmethod

def get(mti:str) -> BaseAgent:

if AgentManager._shared_instance is None:

AgentManager()

return AgentManager._shared_instance._get(mti)

def _get(self, mti:str) -> BaseAgent:

ba: BaseAgent = None

if mti in self._agents.keys():

ba = self. agents.get(mti)

else:

raise NotImplementedError(f"{mti}is not initialized")

return ba
