# l = [1,2,3,4,5,4]
# i = int(input("Enter your desired number:"))

# try:
#     print(l[i])
# except Exception as e:
#     print(e)
 ##rasing custom error
a = input("Enter the string: ")
if (a == "quit"):
    raise ValueError("You can't enter Quit")
else:
    print('you are sorted')