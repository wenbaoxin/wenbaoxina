class person:
    __age = 0
    __sex = ""
    __name = ""
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def setsex(self,sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
class worker(person):
    def play(self):
        print(self.getname(),"正在干活")
class student(person):
    __num = ""
    def setnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num
    def sing(self):
        print("学号为",self.getnum(),self.getage(),"岁的",self.getname(),"正在唱歌")
    def study(self):
        print("学号为",self.getnum(),self.getage(),"岁的",self.getname(),"正在学习")
a = student()
a.setname("小红")
a.setage("985")
a.setsex("女")
a.setnum("89897489484")
a.sing()
a.study()