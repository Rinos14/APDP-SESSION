class DepartmentData:
    def __init__(self, data):
        self.data = data  # Data is a dictionary representing department specifics

    def summarize(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class FinanceData(DepartmentData):
    def summarize(self):
        return f"Total Revenue: {sum(item['revenue'] for item in self.data)}"

# Usage
finance = FinanceData(data=[{'revenue': 1000}, {'revenue': 2000}])
print(finance.summarize())
