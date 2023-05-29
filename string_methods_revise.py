str1 = "Amulakh Desai is Good Person123."

print(str1.casefold())  # amulakh desai is good person123.

print(str1.encode())  # b'Amulakh Desai is Good Person123.'

str2 = "Ståle"
print(str2.encode())  # b'St\xc3\xa5le'

print(str2.encode(encoding="ASCII",errors="replace"))  # b'St?le'
print(str2.encode(encoding="ASCII",errors="namereplace"))  # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ASCII",errors="ignore"))  # b'Stle'
print(str2.encode(encoding="ASCII",errors="backslashreplace"))  # b'St\\xe5le'
print(str2.encode(encoding="ASCII",errors="xmlcharrefreplace"))  # b'St&#229;le'


str1 = "Amulakh Desai is\tGood Person123."
print(str1.expandtabs(16))  # Amulakh Desai is                Good Person123.

print(str1.endswith('.',2,5))   # False

# str3 = "{name} bhai is Good {gender}".format(name="Desai", gender = "Boy")  # Desai bhai is Good Boy
str3 = "{} bhai is Good {}".format("Desai","Boy")  # Desai bhai is Good Boy
str3 = "{1} bhai is Good {0}".format("Desai","Boy")  # Boy bhai is Good Desai


print(str3)


str3 = "{Name} bhai is Good {gender}"
dict1 = {"Name" : "Desai", "gender" : "Boy"}

print(str3.format_map(dict1))

str1 = "          AmulakhDesaiisGoodPerson123       "
print(str1.isalnum())  # True

print(str1.isprintable())  # True
print(str1.lstrip())  # AmulakhDesaiisGoodPerson123
print(str1.rstrip())  #           AmulakhDesaiisGoodPerson123
print(str1.strip())   # AmulakhDesaiisGoodPerson123




str10 = "Hello meetG"


table = str10.maketrans("meet", "Heet", "G")

print(table)  # {109: 72, 101: 101, 116: 116, 71: None}

print(str10.translate(table))  # Hello Heet



str1 = "Amulakh Desai\nis Good\nPerson123."
print(str1.partition(' '))  # ('Amulakh', ' ', 'Desai is Good Person123.')
print(str1.rpartition(' '))  # ('Amulakh Desai is Good', ' ', 'Person123.')
print(str1.split('l'))      # ['Amu', 'akh Desai is Good Person123.']

print(len(str1))  # 32
print(str1.rjust(40))  #         Amulakh Desai is Good Person123.

print(str1.removeprefix('Amu'))  # lakh Desai is Good Person123.
print(str1.removesuffix('3.'))  # Amulakh Desai is Good Person12
print(str1.splitlines())  # ['Amulakh Desai', 'is Good', 'Person123.']

str1 = "Amulakh_desai is Good Person123."
print(str1.title())  # Amulakh_Desai Is Good Person123.
