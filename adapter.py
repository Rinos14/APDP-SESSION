class OldSystem:
    def specific_request(self):
        return "Specific data from old system"

class SystemAdapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()
