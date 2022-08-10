class Person:
    def __init__(self,fname,lname):
        self.fisrt_name=fname
        self.last_name=lname
    
    def print_name(self):
        print(f'name:{self.fisrt_name} {self.last_name}')

class Student(Person):
    pass

p1=Person('han', 'gyumin')
p1.print_name()

s1=Student('jin','sengmin')
s1.print_name()