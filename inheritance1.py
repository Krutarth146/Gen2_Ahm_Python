# Inheritance ---> Heridity


class Alto:
    wheels = 4   # class Variable

    def __init__(self):
        self.seating_cap = 4   # Instance Variable
        self.brake = 2
        self.gear = 5
        print("Alto Constructor is called")


    def set_gear(sl):   # Instance Method
        print(sl.brake)
        
    def set_brake(self):
        print(f"Alto has {self.brake} Brakes.")

    @classmethod
    def set_wheels(cls):  # class Method
        print(cls.wheels) 

    @staticmethod
    def display():
        print("This is Alto Class Static Method")

# a1 = Alto()


# class Ferrari : public Alto
class Ferari(Alto):
    def __init__(self):
        super().__init__()
        self.safety = 10
        print("Ferari Constructor is Called")

    def safety_method(self):
        print("This is safety Method Under Ferrari Class")

f1 = Ferari()

f1.display()  # This is Alto Class Static Method
f1.set_wheels()  # 4  # class Method
f1.set_brake()  # Alto has 2 Brakes.




# --------------------------------------------


class A:
    def __init__(self):
        self.w = 0


    def methodA(self):
        print("Method A")

    
class B(A):
    def methodB(self):
        print("Method B")
    
class C(A):
    def methodC(self):
        print("Method C")

    
class D(B,C):
    def methodD(self):
        print("Method D")

d1 = D()

d1.methodB()
d1.methodB()
d1.methodA()  # Method A
print(d1.w)  # 0


