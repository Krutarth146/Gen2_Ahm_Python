# User Defined Functions

# Functions -> Code Reusability

# FUnction Syntax:

# 1. Func. Defination
# 2. Func. Calling

# void sum();  // Declration


# void sum()  // Defination
# {

#     int a,b;
#     printf(a+b);
# }

# main()
# {
#     sum();  // calling    

# }


# Func. Types
# 1. W/o return type and w/o args
# 2. W/o return type and with args
# 3. with return type and w/o args
# 4. with return type and with args


# 1. W/o return type and w/o args

def Meet():
    print(78 + 90)  # 168

Meet()   # Calling

# 2. W/o return type and with args

def Ridham(x, y, z):
    print(x*y-z)

Ridham(10,90.7,90)  # 817.0

def Ridham(x, y, z=None):
    print(x+y+z)

Ridham('Kr','utar', 'th')  # Krutarth

# 3. with return type and w/o args


# Args
def Ansh(x, y, *argswww):
    for i in argswww:
        print(i,end=' ')     # 10 20 30 40 450 



Ansh(10,20,30,40,450)   # 33.79

# # 4. with return type and with args

print()
list1 = [(10,20),(20,30),(31,40)]
def Cherish(list90):

    res = [(i,j) for i,j in list90 if i % 2 == 0]
    return res


print(Cherish(list1))   # [(10, 20), (20, 30)]

# 4. Prime Numbers  using 4th Type


if 9 < 8:
    pass
else:
    print("Hii")


# functions: enumerate, yield, zip, lambda, map, reduce, filter, 

# Modules: itertools, datetime, random

list1 = [10,20,10,40,50]
list2 = [4,5,6,7,8,9]

ans = [i for i in zip(list1,list2)]

print(ans)   # [(10, 4), (20, 5), (10, 6), (40, 7), (50, 8)]


res = [(w,j) for w,j in enumerate(list1,100)]
print(res)  # [(0, 10), (1, 20), (2, 10), (3, 40), (4, 50)]


def range1():
    for i in range(5):
        return i
    
print(range1())   # 0


def range1():
    for i in range(5):
        yield i
print()
for e in range1():
    print(e,end=' ')  # 0 1 2 3 4