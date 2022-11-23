from pathlib import Path
import requests
from xlwt import Workbook
import traceback
import xlrd

_path = Path.cwd()
_absolute_path = (str(_path)) + '..\\..'
_x_read_data = _absolute_path + '\\resources\\mm-blocks-data.xlsx'
_x_prod_workbook = xlrd.open_workbook(_x_read_data)
_x_prod_sheet = _x_prod_workbook.sheet_by_name('Sheet1')

print('retrieving alt data and creating excel doc.')

def _get_uk_alt_text():
    alt = []
    for i in range(9, 24):
        _x_prod_sku = _x_prod_sheet.cell_value(i, 3)
        _x_cat_name = _x_prod_sheet.cell_value(i, 2)
        _prod_url = requests.get(f"{_x_prod_sku}")
        try:
            _json_prod = _prod_url.json()
            _json_prod_alt = _json_prod['productName']
            alt.append(_json_prod_alt)  
        except ValueError:
            print(f'UK ~ Error getting data from: {_x_cat_name} ~ SKU: {_x_prod_sku}')
            alt.append('No Alt.')
    return alt
def _get_us_alt_text():
    alt = []
    for i in range(8, 15):
        _x_prod_sku = _x_prod_sheet.cell_value(i, 4)
        _x_cat_name = _x_prod_sheet.cell_value(i, 2)
        _prod_url = requests.get(f"{_x_prod_sku}")
        try:
            _json_prod = _prod_url.json()
            _json_prod_alt = _json_prod['productName']
            alt.append(_json_prod_alt)  
        except ValueError:
           print(f'US ~ Error getting data from: {_x_cat_name} ~ SKU: {_x_prod_sku}')
           alt.append('No Alt.')
    return alt
def _get_de_alt_text():
    alt = []
    for i in range(8, 15):
        _x_prod_sku = _x_prod_sheet.cell_value(i, 5)
        _x_cat_name = _x_prod_sheet.cell_value(i, 2)
        _prod_url = requests.get(f"{_x_prod_sku}")
        try:
            _json_prod = _prod_url.json()
            _json_prod_alt = _json_prod['productName']
            alt.append(_json_prod_alt)  
        except ValueError:
           print(f'DE ~ Error getting data from: {_x_cat_name} ~ SKU: {_x_prod_sku}')
           alt.append('No Alt.')
    return alt

_alt_uk = _get_uk_alt_text()
_alt_us = _get_us_alt_text()
_alt_de = _get_de_alt_text()

_wrb = Workbook(_absolute_path + '\\resources\\mm-blocks-data-alt-output.xls')
uk_wrbs = _wrb.add_sheet('data',  cell_overwrite_ok=True)
us_wrbs = _wrb.add_sheet('us_data',  cell_overwrite_ok=True)
de_wrbs = _wrb.add_sheet('de_data',  cell_overwrite_ok=True)

for row, word in enumerate(_alt_uk, start=0):
    uk_wrbs.write(row, 0, word)
for row, word in enumerate(_alt_us, start=0):
    us_wrbs.write(row, 0, word)
for row, word in enumerate(_alt_de, start=0):
    de_wrbs.write(row, 0, word)

_wrb.save(_absolute_path + '\\resources\\mm-blocks-data-alt-output.xls')



