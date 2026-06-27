class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @classmethod
    def fromsrt(cls,string):
        name , marks = string.split("-")
        return cls(name , int(marks)) 
string = "ayush-85"
e1 = student.fromsrt(string)
print(e1.name)
print(e1.marks)