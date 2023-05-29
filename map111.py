# Map

list1 = [10,20,30,405,50]


def square(list2):
    list3 = []
    for i in list2:
        list3.append(i**2)
    return list3

print(square(list1))  # [100, 400, 900, 164025, 2500]


print(list(map(lambda x : x*x, list1)))  # [100, 400, 900, 164025, 2500]


# filter

import statistics

avg = statistics.mean(list1)
print(avg)
# agni = list(map(lambda x : avg > x, list1))  # [True, True, True, False, True]
agni = list(filter(lambda x : avg > x, list1))  # [10, 20, 30, 50]
print(agni)



fruits = ['', "banana", 'apple', 'cherry', '']

print(list(filter(None,fruits)))   # ['banana', 'apple', 'cherry']

v = None

print(type(v))  # <class 'NoneType'>



# reduce

from functools import reduce

list2 = [20,33,44,66,21]

print(reduce(lambda a,b : a*b, list2))   # 40249440
print(reduce(lambda a,b : a+b, list2))   # 184

import operator
print(reduce(operator.add, list2))   # 184

from itertools import accumulate

print(list(accumulate(list2,lambda a,b : a+b)))  # [20, 53, 97, 163, 184]

# Map, reduce, filter --> 10 Programs

temp = [("Ahm",41), ("Vadodara",33), ("Kheda", 28)]   # --> Convert into Farenheit

print(list(map(lambda pair : (pair[0],(9/5)*(pair[1]) + 32 ), temp)))
# °F = (°C × 9/5) + 32
# [('Ahm', 105.8), ('Vadodara', 91.4), ('Kheda', 82.4)]