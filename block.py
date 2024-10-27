from openpyxl.styles import Alignment, Border, Side
import calendar

class Block:
    def __init__(self, month, year, worksheet):
        self.month = month
        self.year = year
        self.worksheet = worksheet

    def date_row(self, col, row):
        _, num_days = calendar.monthrange(self.year, self.month)
        
        medium_side = Side(style="medium")
        dotted_side = Side(style="dotted")

        for i in range(1, num_days + 1):
            weekday_index = calendar.weekday(self.year, self.month, i)
            weekday_name = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"][weekday_index]
            
            day_cell = self.worksheet.cell(row=row, column=col + i - 1)
            date_cell = self.worksheet.cell(row=row + 1, column=col + i - 1)
            day_cell.value = weekday_name
            date_cell.value = i
            day_cell.alignment = Alignment(horizontal="center")
            date_cell.alignment = Alignment(horizontal="center")

            if i == 1:
                day_cell.border = Border(left=medium_side, top=medium_side, right=dotted_side, bottom=None)
                date_cell.border = Border(left=medium_side, top=None, right=dotted_side, bottom=medium_side)
            elif i == num_days:
                day_cell.border = Border(left=dotted_side, top=medium_side, right=medium_side, bottom=None)
                date_cell.border = Border(left=dotted_side, top=None, right=medium_side, bottom=medium_side)
            else:
                if weekday_name == "Fr":
                    day_cell.border = Border(left=dotted_side, top=medium_side, right=medium_side, bottom=None)
                    date_cell.border = Border(left=dotted_side, top=None, right=medium_side, bottom=medium_side)
                else:
                    day_cell.border = Border(left=dotted_side, right=dotted_side, top=medium_side, bottom=None)
                    date_cell.border = Border(left=dotted_side, right=dotted_side, top=None, bottom=medium_side)