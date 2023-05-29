test_list = [(54, 2), (34, 55), (555, 23), (12, 45), (84, )]
k = 2

# 14. Get a Key From Value in a Dictionary
# -> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 45, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}


val1 = 45

for key,value in D1.items():
    if value == val1:
        print(key)  # Hritik Roshan


dict1 = {"Name" : "Vansh", "ROll" : 900, 'College' : 'Silveroak'}

print(dict1['College'])

# dict1['Year'] = 9000
# print(dict1['Year'])

print(dict1.get('Year', "Year is Not Defined yet."))

l1= [i for i in range(5)]

dict2 = {"str1" : 90}
dict2.setdefault("str2", True)
print(dict2)


l1 = ["r1",'r2','r3','r4','r5']
l2 = [10,20,30,40,[10,20]]


dict2 = {i:j for i,j in zip(l1,l2)}
print(dict2)


cube_dict = {x : x**3 for x in range(1,6)}
print(cube_dict)


str1 = "Vansh"

# {'V' : 'vv', 'A' : 'aa'......}

print({x.upper() : x.lower()*2 for x in str1})

test_list = [(54, 2), (34, 55), (555, 23), (12, 45), (84, )]
k = 2

blank = []
for j in test_list:  # (54, 2)
    flag = 0
    for d in j:
        if len(str(d)) == k:
            flag = 1
        else:
            flag = 0
            break

    if flag==1:
        blank.append(j)
print(blank)

res = [j for j in test_list if all(len(str(d)) == k for d in j)]
print(res)  # [(34, 55), (12, 45), (84,)]

l1 = [9.89,1,-3,8,0]
print(all(l1))  # False
print(any(l1))  # True


list1 = [(10,20), (50,40), (20,88), (11, 23)]
list2 = [(10,10), (50,41), (40,50), (20,88), (45,32), (20,10), (34,23)]


# Intersection

# 1223453


# 1 0 
# 2 1 2
# 3 3 6
# 4 4
# 5 5