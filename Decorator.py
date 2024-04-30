class DataReport:
    def display(self):
        return "Report Data"

class Decorator(DataReport):
    _component: DataReport = None

    def __init__(self, component: DataReport):
        self._component = component

    def display(self):
        return self._component.display()

class AuthorizedReport(Decorator):
    def display(self):
        return f"Authorized: {super().display()}"
