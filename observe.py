from _future_ import annotations
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):


a##


The Observer interface declares the update method, used by class Observable:.


@abstractmethod
def update(self, subject: IObservable) -> None:
nnr


Receive update from subject.


pass


class IObservable(ABC):


"a"


The Observable interface declares a set of methods for managing subscribers.


브#키


@abstractmethod
def attach(self, observer: Observer) -> None:


Attach an observer to the subject.


pass


@abstractmethod
def detach(self, observer: Observer) -> None:
"""
Detach an observer from the subject.
"""
pass


@abstractmethod
def notify(self) -> None:


"#n


Notify all observers about an event.


pass


class Observable(IObservable):


nn


The Qbservable owns some important state and notifies observers when the state
changes


E


stateChanged = False


@property
def stateChanged(self):
return self._stateChanged


@stateChanged.setter
def stateChanged(self, changed: bool):
if(self.__stateChanged !- changed):
self.__stateChanged
=


changed
self.notify()


For the sake of simplicity, the Observable's state, essential to all
subscribers, is stored in this variable.


observers: List[Observer] = []


List of subscribers. In real life, the list of subscribers can be stored
more comprehensively (categorized by event type, etc.).


def


attach(self, observer: Observer) -> None:
print("Observable: Attached an observer.")
self._observers.append(observer)


def detach(self, observer: Observer) -> None:
self._observers.remove(observer)


def notify(self) -> None:
mam
Notify all observers about an event
for observer in self._observers:
observer.update(self)
self.__stateChanged = False
