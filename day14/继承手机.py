import time
class OlderPhone:
    __Phonenumer = ""
    __voice = ""
    def setPhonenumber(self,Phonenumber):
        self.__Phonenumer = Phonenumber
    def getPhonenumber(self):
        return self.__Phonenumer
    def setvoice(self,voice):
        self.__voice =voice
    def getvoice(self):
        return self.__voice
    def call(self,callnumber):
        callnumber = str(callnumber)
        print(self.__Phonenumer,"正在给",callnumber,"打电话","正在响铃",self.__voice)
class Newphone(OlderPhone):
    __name = ""
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def call(self,callnumber):
        super().call(callnumber)
        print("语音拨号中")
        for i in range(3):
            time.sleep(1)
            print(".", end="")
        print("品牌为",self.__name,"的手机真好用")
b = OlderPhone()
b.setPhonenumber("554447448788")
b.setvoice("苍茫的天涯是我的爱")
b.call("5658494945684")

a = Newphone()
a.setname("棋手i帝豪斯帝国搜狗")
a.call("55482488455")

# 3
class cc:
    __name = ""
    __size = 0
    __color = ""
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setsize(self,size):
        self.__size = size
    def getsize(self):
        return self.__size
    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color
    def show(self):
        print("您的手机型号为",self.getname(),"尺寸为：",self.getsize(),"颜色为：",self.getcolor())
class phone(cc):
    def show(self):
        super().show()
a = phone()
a.setname("诺基亚")
a.setsize(7.9)
a.setcolor("红色")
a.show()