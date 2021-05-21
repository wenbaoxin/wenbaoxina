import unittest
import xlwt
import xlrd
from 计算器 import jisuanqi
from ddt import ddt
from ddt import data
from ddt import unpack
class Excel():
    a = []
    wb = xlrd.open_workbook(filename="数据.xlsx",encoding_override=True)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(0,rows):
        a.append(sheet.row_values(i))
b = Excel()
c = b.a
@ddt
class Testadd(unittest.TestCase):
    @data(*c)
    @unpack
    def test_add(self,e,f,g):
        calc = jisuanqi()
        sum = calc.add(e,f)
        self.assertEqual(g,sum)
