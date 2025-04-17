from util.observe import IObservable, Observable, Observer
from threading import Thread


class StatusObserver (Observer):
def _init_(self) -> None:
super()_init_()


def update(self, subject: IObservable) -> None:
if isinstance(subject, Thread):
if not subject.is_alive():
#TODO-Write logic when thredd got interrepted
pass
pass
