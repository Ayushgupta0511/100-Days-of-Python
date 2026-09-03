import time
timestamp   =  time.strftime("%H:%M:%S")
print("Current time is :" , timestamp)
hour = int(input("Enter your desired hour: "))
if hour  <=0 and hour  <12:
    print("good morning")
elif  hour>= 12 and hour  <15:
        print("good afternoon")
elif hour >= 15 and hour <0:
        print("good evening")
# timestamp   =  time.strftime("%H")
# print(timestamp)
# timestamp   =  time.strftime("%M")
# print(timestamp)
# timestamp   =  time.strftime("%S")
# print(timestamp)