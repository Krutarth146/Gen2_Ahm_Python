# File 1. Text File (t)  2.Binary File (b)

# FIle Opening Modes
# 'w' - Write Mode  (Overwrite)
# 'r' - Read Mode
# 'a' - Append Mode
# 'x' - If file exists then it will generate an Error
# '+' - "Read + Write"

fp = open("first.txt","w")
fp.write("Hello, I am Meet Patel!\nOm Patel")

list1 = ["\nHello, I am Amulakh Desai!\n","Hello, I am Jenish\n", "Hello, I am Khush\n"]

fp.writelines(list1)
fp.close()

f1 = open("first.txt","r")
# temp = f1.read()
# print(temp)
print(f1.tell())   # 0
  
print(f1.readline())  # Hello, I am Meet Patel!
print(f1.tell())  # 25
print(f1.readline())  # Om Patel
print(f1.tell())   # 35
print(f1.readline())  # Hello, I am Amulakh Desai!
print(f1.tell())   # 63
print(f1.readline())  # Hello, I am Jenish
print(f1.tell())   # 83
print(f1.readline())  # Hello, I am Khush
print(f1.tell())   # 102
print(f1.readline())  # 
print(f1.tell())   # 102
f1.seek(0)
print(f1.readlines())  # ['Hello, I am Meet Patel!\n', 'Om Patel\n', 'Hello, I am Amulakh Desai!\n', 'Hello, I am Jenish\n', 'Hello, I am Khush\n']
print(f1.tell())  # 102


# (SEEK_END,-5)
# (SEEK_SET,-5)
# (SEEK_CUR,-5)
f1.close()

fo = open("snake1.jpg","rb")
x = fo.read()
fo.close()

# print(x)

fs = open("scopy.jpg","wb")
fs.write(x)
fs.close()

import pickle
list1 = ["ROyal ", "Technosoft"]

with open('data1.txt', 'wb') as f2:
    pickle.dump(list1,f2)


f4 = open("data1.txt","rb")
temp1 = pickle.load(f4)
print(temp1)  # ['ROyal ', 'Technosoft']