# 1. 
# vehicles = 200  # (2W + 4W)
# wheels = 540

# Find 2w, 4w???

# -----------------------------------

# 2. list1 = [[10,20,30], [3,9,80,78], [33,99,22,11,66]]

# Find Second Highest ELement from each inner list   ---> (lambda, map, reduce, filter)

# Ans. [20,78,66]

# -----------------------------------

# 3. if count of '#' and '*' in string are same then print 0, if count of '#' is more than '*' ---> print(-1) otherwise print(1) 

# Ex1. str1 = "He*#l#l*o"   # Ans. 0


# 4 Mississippi  ---> {'M' : 1, 'i' : 4, 's' : 4, 'p' : 2}

# ---------------------------------------------------------

str1 = "Ja#grav#**"

# '#'  and '*'
c1 = 0
c2 = 0

for i in str1:
    if i == '#':
        c1 += 1
    if i == '*':
        c2 += 1

if c1 == c2 and c1!=0:
    print(0)






# Prime Number


# 19 --> 1,19
# 24 --> 1,2,3,4,6,8,12,24
# 29 --> 1,29
# 23 --> 1,23
num = 28
divisor = 0
for i in range(1,num+1):   # 1 to 23
    if num % i == 0:
        divisor+=1
        print(i,end=' ')

print("Divisors:",divisor)


if divisor == 2:
    print("Prime Number")
else:
    print("Not Prime Number")


# Loops, if else, functions

# Palindrome, Armstrong, Perfect, Prime, Twin, Sum of Digits

test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
k = 2
list1 = []
for x in test_list:
    flag = 0
    for g in x:
        if len(str(g)) == k:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        list1.append(x)
print(list1)


list2 = [x for x in test_list if all(len(str(g)) == k for g in x)]
print(list2)


test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]
res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
print(res)