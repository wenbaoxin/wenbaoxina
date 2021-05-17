class chushi:
    __name = ""
    __age = 0
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def zhucook(self):
        print("正在煮饭")
class chushi2(chushi):
    def chaocook(self):
        print("正在炒菜")
class chushi3(chushi2):
    def zhucook(self):
        print(self.getage(),"的",self.getname(),"师傅正在煮饭")
    def chaocook(self):
        print(self.getage(),"的",self.getname(),"师傅正在炒菜")

a = chushi3()
a.setname("老王")
a.setage(99)
a.zhucook()
a.chaocook()



