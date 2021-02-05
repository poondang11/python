import time
name = []
score =[]
temes = []
hit = []
def time_():
    timeis = time.localtime()
    a = time.strftime('%d %B %Y ,%H:%M:%S',timeis)
    print(a)

num = int(input("press number Practice:"))
for i in range(num):
    print("people no.",1+i)
    na =input("Name:")
    sc=float(input("score:"))
    t=float(input("time:"))
    name.append(na)
    score.append(sc)
    temes.append(t)
    hit.append(sc/t)
for i in range(num):
    j = i
    for j in range(num):
        if hit[i] > hit[j]:
            a,b,c,d = hit[i],name[i],score[i],temes[i]
            hit[i],name[i],score[i],temes[i] =  hit[j],name[j],score[j],temes[j]
            hit[j],name[j],score[j],temes[j] = a,b,c,d
timeis = time.localtime()
a = time.strftime('%A',timeis)
b = time.strftime('%Y',timeis)
print("shotgun"+a+"training",b,"\ncondtion : 1")
time_()
print("-"*77)
print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("no.","PTS","time","competitor#Name","hit factor","state points","state percent"))
print("-"*77)           
for i in range(num):
    stawe_po =(hit[i]/hit[0])*50
    stawe_pe =(stawe_po/(hit[0]/hit[0]*50))*100
    print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format(i+1,int(score[i]),int(temes[i]),name[i],"%.4f"%hit[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))