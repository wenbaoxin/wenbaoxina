import unittest
from bankthree import bank_adduser
from bankthree import User
class Test_changemoney(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.bank_adduser = bank_adduser()
    def testchangemoney(self):
        self.user.setAccount("0a3f4357")
        inu="70673e1b"
        self.user.setPassword("1")
        self.user.setMoney(2)
        a = 0

        change = self.bank_adduser.transfer(self.user,inu)
        self.assertEqual(a,change)

    def testchangemoney1(self):
        self.user.setAccount("564645555")
        inu="70673e1b"
        self.user.setPassword("1")
        self.user.setMoney(2)
        a = 1

        change = self.bank_adduser.transfer(self.user,inu)
        self.assertEqual(a,change)

    def testchangemoney2(self):
        self.user.setAccount("0a3f4357")
        inu="70673e1p"
        self.user.setPassword("1")
        self.user.setMoney(2)
        a = 1

        change = self.bank_adduser.transfer(self.user,inu)
        self.assertEqual(a,change)

    def testchangemoney3(self):
        self.user.setAccount("0a3f4357")
        inu="70673e1b"
        self.user.setPassword("989898989898")
        self.user.setMoney(2)
        a = 2

        change = self.bank_adduser.transfer(self.user,inu)
        self.assertEqual(a,change)

    def testchangemoney4(self):
        self.user.setAccount("0a3f4357")
        inu="70673e1b"
        self.user.setPassword("1")
        self.user.setMoney(898989)
        a = 3

        change = self.bank_adduser.transfer(self.user,inu)
        self.assertEqual(a,change)