dictionary =[]
pra=[]
kum=[]
i=1
def menu():
    global select
    print("\nDictionary\n 1.add word\n 2.show word\n 3.delete word\n 4.Exit")
    select = input("press select:")

def add():
    dictionary.insert(0,input("add word:"))
    pra.insert(0,input("type word(n. v. adj .adv):"))
    kum.insert(0,input("mean:"))
    print("\tadd word suceess!!")
def show():
    print("--------vocabulary----------")
    print("word type mean")
    x = 0
    while x < len(dictionary):
        print(dictionary[x],' ',pra[x],' ',kum[x])
        x= x+1
def delete():
    x=str(input("key you word delete:"))
    x2=str(input("you are want delete"+x+"(y/n):"))
    if x2 == 'y':
        z=0
        while z<len(dictionary):
            if x==dictionary[z]:
                del pra[z]
                del kum[z]
                z=z+1
            dictionary.remove(x)
            print("delete\t" +x+ "\tsucess!!")
        else:
            print("cancel")        

while True:
    menu()
    if select == '1':
        add()
    elif select == '2':
        show()
    elif select == '3':
        delete()
    else:
        o=str(input("you are exit?(y/n):"))
        if o == 'y':
            print("thank you to use program")
            break
        else:
            print("back to menu")