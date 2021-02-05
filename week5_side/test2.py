def menu():
    global choice
    print("\n","*"*10,"CD shop","*"*10)
    print('show product [s]\nadd product [a]\nlog out [x]\n')
    choice = input('cloose order: ')
name = []
mon = []
def show():
    class shop:
        def __init__(self,name1,money1,name2,money2,name3,money3,name4,money4) :
            self.name1 = name1
            self.money1 = money1
            self.name2 = name2
            self.money2 = money2
            self.name3 = name3
            self.money3 = money3
            self.name4 = name4
            self.money4 = money4
        def shows(self) :
            print("-------product-------\n")
            print("1.",self.name1,self.money1,"บาท")
            print("2.",self.name2,self.money2,"บาท")
            print("3.",self.name3,self.money3,"บาท")
            print("4.",self.name4,self.money4,"บาท")
            n = 5
            m = 0
            while m < len(name) :
                print(n,".",name[m]," ",mon[m],"บาท")
                m = m+1
                n = n+1
            print("\n")
    x = shop("adult VDO CD","200","cartoon CD","60","Blank CD","40","Music CD","250")
    x.shows()

def add():
    class puss:
        while 1>0 :
            q = str(input("\nadd product or press Exit\nadd name product "))
            if q == "exit" :
                print("\n")
                break
            w = input("add price" +q+" :")
            name.append(q)
            mon.append(w)
            print("add success!!")
            e = input("are you need add product (y/n):")
            if e == "n":
                break

while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        add()
    elif choice == 'x':
        o =str(input("you are exit ?(y/n) :"))
        if o == "y":
            print("thank you for using")
            break
        else:
            print("return to menu")