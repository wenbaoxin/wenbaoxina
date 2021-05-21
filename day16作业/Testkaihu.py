import unittest
from bankthree import bank_adduser
from bankthree import User
from bankthree import Address
class Testbank_adduser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.address = Address()
        self.bank_adduser = bank_adduser()
    def test_kaihu(self):
        self.user.setAccount("98989898")
        self.user.setUserame("857857")
        self.user.setPassword("258")
        self.address.setCountry("中国")
        self.address.setProvience("阿拉伯")
        self.address.setStreet("大家雕塑")
        self.address.setDoor("第五")
        self.user.setMoney(0)
        a = 1

        add = self.bank_adduser.addbank_adduser(self.user,self.address)
        self.assertEqual(a,add)

    def test_kaihu1(self):
        self.user.setAccount("8abb3f97")
        self.user.setUserame("857857")
        self.user.setPassword("258")
        self.address.setCountry("中国")
        self.address.setProvience("阿拉伯")
        self.address.setStreet("大家雕塑")
        self.address.setDoor("第五")
        self.user.setMoney(0)
        a = 2

        add = self.bank_adduser.addbank_adduser(self.user,self.address)
        self.assertEqual(a, add)
