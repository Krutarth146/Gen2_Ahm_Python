_ = 90 + 80j

print(type(_))

f = 2
print(type(f))

print(_ + f)  # Implicit type conversion


h = True
h = str(h)  # Explicit Type conversion
print(type(h))  # <class 'str'>

e = 90   # int 
w = True   # Bool

print(e+w)   # 91


f = "90.89"
print(int(float(f)))   # 90

h = None
print(type(h))   # <class 'NoneType'>

# Operator Precedence and associativity
print(2*(3+5))   # 16
print(2**(3**3))  # 134217728

# while Loop

# _ = 99
# while (_ >= 25):
#     print(_,end=' ')
#     _-=2   # Assignment O/p -> Priority Low

print()
# _ = 99
# while (_ >= 1):
#     if _ % 5 == 0 or _ % 7 == 0 and (_ % 10 == 0 and _ % 4 == 0):
#         print(_,end=' ')
#     _-=1   # Assignment O/p -> Priority Low


num = 981   # -> 189

counter = 0
sum = 0

while num > 0:
    rem = num % 10   # 9
    # sum = sum+ pow  # 189
    num = num // 10  # 0
    counter += 1   # 3

print(counter)   # 3
print(sum)    # 189

# 1 to 10000 -> Palindrome,Armstrong, Prime, Perfect, Twin, LCM, HCM