name=[]
while(True):
    print("#"*25)
    print("wigleg game shop")
    print("add [a]")
    print("show list [s]")
    P=input("log out [x]\n")
    if P=='a' :
        N=input("press shopkeeper info(pass:name:province)")
        name.append(N) 
        print("**********suceess!!*************")
    elif P=='s':
        print('{0:-<26}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('pass','name','province'))
        print('{0:-<26}'.format(""))
        for x in name:
            e=x.split(":")
            print("{0[0]:<6}{0[1]:<10}{0[2]:<10}".format(e))
            continue
    elif P=='x':
        A=input("you are exit?(N/Y):")
        if A=='Y':
            break
        if A=='N':
            continue
             


