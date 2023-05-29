list1 = []
print(type(list1))  # <class 'list'>

tuple = ()
print(type(tuple))  # <class 'tuple'>

dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = {10,}
print(type(set1))  # <class 'set'>


# ------------------------------------

# array -> Same Datatype

# import array

# import numpy as np
# arr1 = np.array([10,20,30,40])



list1 = [10, 90, 89, 78, 67]
print(list1)  # [10, 90, 89, 78, 67]

tup1 = (10, 90, 89, 78, 67)
print(tup1)

print(list1.__sizeof__())  # 88
print(tup1.__sizeof__())   # 64


list1 = [10, 90, 89.78, True, 78+9j, [2,2,3], (4,4,5), {10,20,10}, {'Name' : "Meet"}, 'M', "Dhiraj Sir"]

print(list1)  # [10, 90, 89.78, True, (78+9j), [2, 2, 3], (4, 4, 5), {10, 20}, {'Name': 'Meet'}, 'M', 'Dhiraj Sir']

print(len(list1))  # 11

# Indexing
print(list1[0])  # 10
print(list1[-3])  # {'Name': 'Meet'}


# Slicing

print(list1[3:8])  # [True, (78+9j), [2, 2, 3], (4, 4, 5), {10, 20}]
print(list1[3:8:2])  # [True, [2, 2, 3], {10, 20}]
print(list1[-5:-10:3])  # []
print(list1[-5:-10:-3])  # [(4, 4, 5), True]
print(list1[-3:-8:2])  # []


# List Methods

list1 = [10,90,89,78,67,67.90,10,10,10]

print(id(list1))  # 2152137634496

print(sum(list1))  # 401.9
print(sum(list1) / len(list1))  # 66.98333333333333

print(sorted(list1[2:]))  # [78, 67.9, 67, 10, 10, 10, 10]

list1.sort(reverse=True)
print(list1)  # [90, 89, 78, 67.9, 67, 10]

list1.reverse()
print(list1)

# list charcteristics: Ordered (Indexed), Mutable (Changeble), Allow Duplicates

# list1.append(100)
# print(list1)  # [10, 10, 10, 10, 67, 67.9, 78, 89, 90, 100]

# list1.append("ROyal")
# print(list1)  # [10, 10, 10, 10, 67, 67.9, 78, 89, 90, 100, 'ROyal']

# list1.extend('100')
# print(list1)  # [10, 10, 10, 10, 67, 67.9, 78, 89, 90, 100, 'ROyal', '1', '0', '0']

# list1.extend("Techno")
# print(list1)  # [10, 10, 10, 10, 67, 67.9, 78, 89, 90, 100, 'ROyal', '1', '0', '0', 'T', 'e', 'c', 'h', 'n', 'o']

list1 = [10,90,89,78,67,67.90,10,10,10]
list2 = [10,20,30,40,50,90]
# list1+=list2
# print(list1)  # [10, 10, 10, 10, 67, 67.9, 78, 89, 90, 100, 'ROyal', '1', '0', '0', 'T', 'e', 'c', 'h', 'n', 'o', 10, 20, 30, 40, 50, 90]


# list1.append(list2)
# print(list1)  # [10, 90, 89, 78, 67, 67.9, 10, 10, 10, [10, 20, 30, 40, 50, 90]]

# list1.extend(list2)
# print(list1)  # [10, 90, 89, 78, 67, 67.9, 10, 10, 10, 10, 20, 30, 40, 50, 90]

list1.insert(3,"Private")
print(list1)  # [10, 90, 89, 'Private', 78, 67, 67.9, 10, 10, 10]

list1.insert(-1,"Cherish")
print(list1)  # [10, 90, 89, 'Private', 78, 67, 67.9, 10, 10, 'Cherish', 10]

list1[2] = "Vansh"
print(list1)  # [10, 90, 'Vansh', 'Private', 78, 67, 67.9, 10, 10, 'Cherish', 10]



list1 = [10,90,89,78,.67]


for i in list1:
    print(i,end=' ')  # 10 90 89 78 0.67


list2 = [[20,90,78], 
         [34, 89, 67], 
         [89,56,34]]

print(len(list2))  # 3


for j in list2:  # [20,90,78]  [34, 89, 67] ..
    for _ in j:   # 20 90 78 34 89 67 ..
        print(_,end=' ')   # 20 90 78 34 89 67 89 56 34