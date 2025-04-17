from util.observe import Observable, Observer


class MyObservable (Observable):
def init_(self)
-)


None:
self._state
"New"


def doSomework(self):
print ("set new state")
self. state
"Chnged"
self.stateChanged True


def dootherthing(self):
print("state not changed")


class ConcreteObserverA(Observer):
def update(self, subject: Observable)


Y
None:
if subject.stateChanged:
print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
def update(self, subject: Observable)


->
if subject.stateChanged:
None:
print("ConcreteObserverB: Reacted to the event")


if


name_
# The client code.
main__":


subject = MyObservable()


observer_a = ConcreteObserverA(
subject.attach(observer_a)


observer_b
subject.attach(observer_b)
ConcreteObserverB()


subject.doOtherthing()
subject.doSomework()


subject.detach(observer_a)


subject.doSomework()
