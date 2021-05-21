import unittest
from bankthree import bank_adduser
from bankthree import User
from bankthree import Address
class Testbank_savemoney(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.address = Address()
        self.bank_adduser = bank_adduser()
    def test_savemoney(self):
        self.user.setAccount("8abb3f97")
        self.user.setPassword("123654")
        self.user.setMoney(1999.01)
        a = 1

        save = self.bank_adduser.savemoney(self.user)
        self.assertEqual(a,save)

    def test_savemoney1(self):
        self.user.setAccount("98574844")
        self.user.setPassword("123654")
        self.user.setMoney(1999.01)
        a = False

        save = self.bank_adduser.savemoney(self.user)
        self.assertEqual(a, save)