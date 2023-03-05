import re

class AgeNotWithinRange(Exception):
    def msg(self):
        print("Age not between 15 and 21.")

class NameNotValid(Exception):
    def msg(self):
        print("Name is having numbers or special character.")

class Student:
    def __init__(self,rollno,name,age,course):
        try:
            self.rollno = rollno
            self.name = name
            self.age = age
            self.course = course

            regEX = r'\d|\W'
            result = re.findall(regEX,name)

            if(age<15 or age>21):
                raise AgeNotWithinRange
            elif len(result)!=0:
                raise NameNotValid
    
        except AgeNotWithinRange as err:
            err.msg()
        except NameNotValid as err1:
            err1.msg()

q="y"
while q.lower()=="y":
    try:
        rollno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        S1 = Student(rollno,name,age,course)
    except ValueError:
        print(ValueError)
        print("Enter interger value for age")
    q=input("want to continue? (y/n): ")
