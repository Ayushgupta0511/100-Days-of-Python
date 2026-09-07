#use for mapping
info  = {"name":"ayush","age":20,"Eligible":"yes"}
# for key in info:
#     print("for",key,"value is",info[key])
# print(info.items())
# for keys,values in info.items():
#     print("for",keys,"value is",values)
# del info
info.pop("name") #delete particular
info.popitem()#delete the last one 
print(info)