ans = lambda x : x**3

print(ans(10))

# --------------

res = lambda a,b : a+b

print(res(10,33))  # 43

# lambda

def desai(x,y,z):
    return x*y*z

print(desai(20,44,31))  # 27280

javab = lambda x,y,z : x*y*z

print(javab(20,44,31))

# ----------------------------------

def demo(p):
    return lambda x,r : x * p * r


amulakh = demo(400)

print(amulakh(20,300))  # 2400000


def multiplier(n):
    return lambda d : d * n

res1 = multiplier(40)
res2 = multiplier(50)


print(res1(20))
print(res2(10))

# -----------------------------


def quadratic_function(a, b, c):
    return lambda x : (a * (x ** 2)) + (b * x) + (c)


res = quadratic_function(5,3,2)

print(res(4))  # 94


list1 = [40,50,690,21,22]

# list1.sort(key = lambda)
print(list1)


def royal(x,y,*sample,z=88):
    print(sample)

royal(20,304,50,89,22,3,4)  # (20, 304, 50)


def dev(*args, **cherish):
    # print(cherish)
    # for i in cherish.items():
    # for i in cherish.values():
    for i in cherish:
        print(i)

    print(args[2])

dev(10,20,30,name= "Vishwa", place = "Surat", age = 19, roll = [10,20,30,40])  # {'name': 'Vishwa', 'place': 'Surat', 'age': 19, 'roll': [10, 20, 30, 40]}