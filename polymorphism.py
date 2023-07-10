# Polymorphism

# Poly - Many
# Morph - Forms

# right ----> right - wrong, right - left
# who ------> kon, k j


# Methods  ---> len(), min(), max()
print(len("Mithil"))   # 6
print(len([10,20,30]))  # 3

def fun(a,b,c):
    print(a,b,c)

def fun(a,b):
    print(a,b)

fun(10,20)
fun("Meet", 90.78)

class Royal:
    def __init__(self):
        self.fees = 0

    def A(self):
        print("This is A Method Under Royal class without Args.")

    # def A(self,num1):
    #     print("This is A Method Under Royal class with Args.")


class Technosoft(Royal):
    def __init__(self):
        pass

    def A(self):
        print("A Method Under Technosoft class")

    # def A(self,num3):
    #     print("A Method under Technosoft class with 1 Arg.")

    # def A(self,num3, num4):
    #     print("A Method under Technosoft class with 2 Arg.")


    # def A(self):
    #     print("This is A Method Under Technosoft class")


class Institute(Royal):
    def A(self):
        print("A Method Institute class without Args.")

# nikunj = Technosoft()
# nikunj.A(50)  # This is A Method Under Technosoft class




list1 = [Royal(), Technosoft(), Institute()]
print(type(list1[0]))  # <class '__main__.Royal'>
print(list1)

for i in list1:
    i.A()