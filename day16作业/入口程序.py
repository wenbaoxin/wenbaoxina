import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
a = unittest.defaultTestLoader.discover(r"H:\PycharmProjects\工商银行",pattern="Test*.py")
suite.addTests(a)
b  = open(file="银行测试报告.html",mode="w+",encoding="utf-8")
c= HTMLTestRunner.HTMLTestRunner(
    stream= b,
    title="银行测试报告",
    verbosity=2,
    description="银行业务逻辑测试用例"
)
c.run(suite)