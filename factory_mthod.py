class ReportFactory:
    def get_report(self, report_type):
        if report_type == 'finance':
            return FinanceReport()
        elif report_type == 'sales':
            return SalesReport()
        else:
            raise ValueError("Unknown Report Type")

class FinanceReport:
    def generate(self):
        return "Generating finance report"

class SalesReport:
    def generate(self):
        return "Generating sales report"
