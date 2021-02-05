print("motorway Tolls program")
print("-"*45)
print("\tvenicle 4 wheel press 1")
print("\tvenicle 6 wheel press 2")
print("\tvenicle more 6 wheel press 3")
four_wheel=["ลาดกระบัง-->บางบ่อ:25 บาท","ลาดกระบัง-->บางประกง:30 บาท","ลาดกระบัง-->พนัสนิคม:45 บาท""ลาดกระบัง-->บ้านบึง:55 บาท""ลาดกระบัง-->บางพระ:60 บาท"]
six_wheel=["ลาดกระบัง-->บางบ่อ:40 บาท","ลาดกระบัง-->บางประกง:45 บาท","ลาดกระบัง-->พนัสนิคม:75 บาท""ลาดกระบัง-->บ้านบึง:90 บาท""ลาดกระบัง-->บางพระ:100 บาท"]
more_six_wheel=["ลาดกระบัง-->บางบ่อ:60 บาท","ลาดกระบัง-->บางประกง:70 บาท","ลาดกระบัง-->พนัสนิคม:110 บาท""ลาดกระบัง-->บ้านบึง:130 บาท""ลาดกระบัง-->บางพระ:140 บาท"]
press=int(input("chose venicle:"))
if press == 1:
    print("venicle 4 wheel Tolls ")
    for x in four_wheel:
        print("\n",x)
elif press == 2:
    print("venicle 6 wheel Tolls ")
    for x in six_wheel:
        print("\n",x)
elif press == 3:
    print("venicle more 6 wheel Tolls ")
    for x in more_six_wheel:
        print("\n",x)




