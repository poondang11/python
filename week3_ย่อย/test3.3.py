print("press faverite food or press EXIT for exit program")
food=[]
i=0
d=0
while i<=1 :
    d=d+1
    N=input("faverite food อันดับที่ %d คือ:"%d)
    food.append(N)
    if N =='exit':
        break
print("faverite food is",end="")
for x in range(1,d) :
    print(x,".",food[x-1],end="")


