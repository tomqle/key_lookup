import openpyxl

wb = openpyxl.load_workbook('test.xlsx')

sheet1 = wb['Sheet1']
