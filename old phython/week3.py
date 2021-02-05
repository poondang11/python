print("choose your menu")
print("#"*25)
print("choose 1 for rent ")
print("choose 2 for pay extra")
C=int(input("choose:"))
if C==1:
    M=int(input("meter?:"))
    if M <= 25:
        print("you pay 25 bath")
    elif M > 25:
        print("your pay 55 bath")
if C==2:
    M=int(input("meter?:"))
    if M <= 25:
        print("you pay 25 bath")
    elif M > 25:
        print("you pay 80 bath")
