import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook("transaction.xlsx")
sheet = wb["工作表1"]
cell = sheet["A1"]

cell2 = sheet.cell(1,1)

print(cell.value)
print(cell2.value)

print(sheet.max_row)

for row in range(1, sheet.max_row + 1):
    print(row)
    print(sheet.cell(row, 1).value)
    sheet.cell(row, 2).value = row


values =Reference(sheet, min_row = 1, max_row=sheet.max_row, min_col= 2, max_col=2)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, "e2") ###添加图标

wb.save("transaction.xlsx")
### workbook 工作簿 sheet 表格 cell单元格
### max_row最大行数 value单元格的值


