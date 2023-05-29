list1 = [[10,20,30,76] , 
         [40,50,60,88], 
         [70,80,90,78],
         [40,50,60,88]
         ]

print(len(list1))   # 3

for row in range(len(list1)):  # [10,20,30]
    if row % 2 == 0:
        for col in range(len(list1[row])):
            print(list1[row][col],end=' ')  # 10 20 30 40 50 60 70 80 90
    else:
        for col in range(len(list1[row])-1,-1,-1):
            print(list1[row][col],end=' ') 

# --------------------  Sum of Diagonal Elements
print()
sum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i==j:
            sum += list1[i][j]



print(sum)


# List Comprehensension

list1 = []

for i in range(1,11):
    if i % 2 != 0:
        list1.append(i)

print(list1)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [i for i in range(1,11)]
print(list2)


list2 = [i for i in range(1,11) if i % 2 != 0]
print(list2)  # [1, 3, 5, 7, 9]


list10 = [78,2,3,4,5,6]

square = [i*i for i in list10]
print(square)  # [6084, 4, 9, 16, 25, 36]

cube = [i**3 for i in list10]
print(cube)  # [474552, 8, 27, 64, 125, 216]


# ans = [(78,474552), (2,8), (3,27)....]
ans = [(i,i**3) for i in list10]
print(ans)  # [(78, 474552), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216)]

list10 = [78,2,3,4,5,6]

# ans = [(78,78), (78,2), (78,3).....]

for i in list10:   # 78 , 2
    for j in list10:  # 78, 2,3,4,5,6
        print((i,j),end=' ')

ans1 = [(i,j) for i in list10 for j in list10]
print(ans1)



'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''

# Task
list1 = [1,0,0,1,1,0,0,1,1,0]

ans= [1,1,1,1,1,0,0,0,0,0]


