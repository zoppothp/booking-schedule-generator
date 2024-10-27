from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from date_row import DateRow  # Import the DateRow class

# Initialize Workbook and Worksheet
wb = Workbook()
ws = wb.active
ws.title = "Jänner"

# Define fonts and styles
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill("solid", fgColor="000000")

# Set up title
ws.merge_cells("B1:C1")
ws["B1"].value = "Landhaus Zoppoth"
ws["B1"].font = header_font
ws["B1"].alignment = Alignment(horizontal="center", vertical="center")
ws["B1"].fill = header_fill

# Initialize DateRow for January 2025 and apply it
date_row = DateRow(month=1, year=2025)
date_row.setup_dates(ws, start_col=4)

# Additional code to set row heights, column widths, and other data as needed...

# Save workbook
wb.save("booking-schedule.xlsx")