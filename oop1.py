# OOP --> Object Oriented Programming

# int a = 90;
# structure----> User defined Datatype
# class student
# {
#     int id;
#     float marks;
#     char name[10];

    # void set_data()
    # {
    #    id = 90;
    #    marks = 800;
    # }

    # void display()
    # {
    # cout<<id<<endl<<marks;
    # }
# };

# class -> Blueprint
# object -> Instance

# Instance & Class Variable
# class Student:
#     id = 90  
#     name= "Khush"
#     marks = 896 


      #      int   a  in C
# struct  Student s1  in CPP
    #     Student s2  in CPP
# vansh = Student()   in python


# vansh = Student()
# cherish = Student()

# Constructor ---> To solve Intialization Problem
# Student()
# {

# }
# this Keyword in CPP, java

class Bank():
    ROI = 5   # Class Variable

    # def __init__(self):
    #     self.id = int(input("Enter Id: "))    # Instance
    #     self.name = input("ENter Name: ")
    #     self.balance = 0

    def __init__(self,id, name):   # Parametrized Constructor
        self.id =  id    # Instance
        self.name = name
        self.balance = 0

    def add_deposit(self, amount):   # Instance method
        self.balance += amount

    def withdraw(self, amount):   # Instance method
        self.balance -= amount

    def check_bal(self):
        return self.balance

    @classmethod
    def check_ROI(cls):   # Instance method
        return cls.ROI
    
om = Bank(10, "Om")
cherish = Bank(20, "Cherish")

om.add_deposit(5000)
cherish.add_deposit(30)

print(om.check_bal())
print(cherish.check_bal())

print(Bank.ROI)   # 5
# print(Bank.balance)   # Error

print(cherish.ROI)  # 5
print(om.ROI)  # 5


# om.ROI = 10

# print(Bank.ROI)
# print(cherish.ROI)
# print(om.ROI)

Bank.ROI = 56

print(Bank.ROI)   # 56
print(cherish.ROI) # 56
print(om.ROI)   # 56

om.age = 90

print(om.age)
# print(cherish.age)   # GIves Error


print(Bank.check_ROI())   # 56