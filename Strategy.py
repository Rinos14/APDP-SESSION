class ReportContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        return self._strategy.do_algorithm()

class ConcreteStrategyA:
    def do_algorithm(self):
        return "Result of ConcreteStrategyA"

class ConcreteStrategyB:
    def do_algorithm(self):
        return "Result of ConcreteStrategyB"
