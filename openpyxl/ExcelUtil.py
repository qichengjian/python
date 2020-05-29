import openpyxl as xl
from openpyxl.chart import Reference, BarChart


def process_workbook(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['工作表1']
    for row in range(2, sheet.max_row+1):
        cell = sheet.cell(row, 3)
        price = cell.value * 0.9
        price_cell = sheet.cell(row, 4)
        price_cell.value = price

    values = Reference(sheet, min_row=1,
                       max_row=sheet.max_row,
                       min_col=2,
                       max_col=2)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, "e2") ###添加柱状图

    wb.save(filename)

