class DataSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class DataObserver:
    def update(self, subject):
        print("Data has been updated")
