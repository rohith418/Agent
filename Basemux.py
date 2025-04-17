from abc import abstractmethod


from iso.isomsgbearer import ISOMsgBearer


class BaseMux:
@abstractmethod
def terminate(self) -> None:


pass


class TransBaseMux(BaseMux):
def terminate(self) -> None:
self.terminated = True


@abstractmethod


def appendTxQueue(self, msg:ISOMsgBearer):


pass
