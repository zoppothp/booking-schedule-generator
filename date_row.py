from openpyxl.styles import Alignment
import calendar

class DateRow:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.days = ["mo", "di", "mi", "do", "fr", "sa", "so"]

    def setup_dates(self, ws, start_col):
        # Set up weekdays for the entire row
        for i, day in enumerate(self.days * 5, start=start_col):
            ws.cell(row=2, column=i).value = day
            ws.cell(row=2, column=i).alignment = Alignment(horizontal="center")
        
        # Set up the dates row based on the days in the month
        _, num_days = calendar.monthrange(self.year, self.month)
        for i in range(1, num_days + 1):
            ws.cell(row=3, column=start_col - 1 + i).value = i
            ws.cell(row=3, column=start_col - 1 + i).alignment = Alignment(horizontal="center")