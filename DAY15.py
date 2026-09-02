# time = float(input("enter time: "))
# if(0< time < 12):
#     print("good morning")
# elif(12< time < 17):
#     print("good afternoon")
# elif(17<= time < 22):
#     print("good evening")
# else:
#     print("good night")
import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = time.strftime("%H")
print(timestamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)
# a = int(input(" the time is: ", ))