from threading import  Thread
import time
marquee = 0
num = 0
getnum = 0
money = 0
l = 0
class timep(Thread):
    def run(self) -> None:
        global l
        while l<300:
            time.sleep(1)
            l+=1



class coooker(Thread):
    coookername = ""
    def run(self) -> None:
        global l
        global num
        global marquee
        while l <300:
            if marquee >= 300:
                time.sleep(3)
            else:
                num = num+1
                marquee = marquee +1
        else:
            print(self.coookername,"造了",num,"个面包","现在框里有",marquee,"个面包")
class Client(Thread):
    clientname = ""
    def run(self) -> None:
        global getnum
        global  marquee
        global money
        while l<300:
            if marquee <=0:
                print("框里没有面包稍等一下")
            else:
                getnum =getnum + 1
                money = getnum *10
                print(self.clientname,"共买了",getnum,"个面包","花费",money,"元")

t = timep()
c1 = coooker()
c2 = coooker()
c3 = coooker()
c4 = coooker()
c5 = coooker()
c6 = coooker()
c1.coookername = "厨师一"
c2.coookername = "厨师二"
c3.coookername = "厨师三"
c4.coookername = "厨师四"
c5.coookername = "厨师五"
c6.coookername = "厨师六"

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()

s1 = Client()
s2 = Client()
s3 = Client()
s4 = Client()
s5 = Client()
s1.clientname = "顾客一"
s2.clientname = "顾客二"
s3.clientname = "顾客三"
s4.clientname = "顾客四"
s5.clientname = "顾客五"

s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
t.start()

