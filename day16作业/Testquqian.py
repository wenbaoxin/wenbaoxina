import unittest
from bankthree import bank_adduser
from bankthree import User
class Test_getmoney(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.bank_adduser = bank_adduser()
    def test_getmoney(self):
        self.user.setAccount("0a3f4357")
        self.user.setPassword("1")
        self.user.setMoney(1)
        a = 0

        save = self.bank_adduser.getmoney(self.user)
        self.assertEqual(a,save)

    def test_getmoney1(self):
        self.user.setAccount("01234567")
        self.user.setPassword("1")
        self.user.setMoney(1)
        a = 1

        save = self.bank_adduser.getmoney(self.user)
        self.assertEqual(a,save)

    def test_getmoney2(self):
        self.user.setAccount("0a3f4357")
        self.user.setPassword("8989898998989")
        self.user.setMoney(1)
        a = 2

        save = self.bank_adduser.getmoney(self.user)
        self.assertEqual(a,save)

    def test_getmoney3(self):
        self.user.setAccount("0a3f4357")
        self.user.setPassword("1")
        self.user.setMoney(100)
        a = 3

        save = self.bank_adduser.getmoney(self.user)
        self.assertEqual(a,save)