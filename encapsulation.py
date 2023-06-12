class Royal:
    no_of_students = 300  # Public
    _password = 87654321   # class Variable  (Protected)
    __account_money = 800000000000000000000  # Private

    def __init__(self, name, roll):  # Constructor
        self.group_name = name + str(roll)
        self.name = name
    
    def change_name(sel, modified_name):  # Instance Method
        sel.name = modified_name

    @classmethod
    def change_password(cls):
        cls._password = input()
        print("Password Updated!")

    @classmethod
    def add_amount(cls, fees):
        cls.__account_money += fees
        print(f"Your Updated Bal is {cls.__account_money}")

    @staticmethod
    def Feedback_of_royal():
        print("Good")



# ayush = Royal()

# print(Royal.password)
# Royal.change_password()

# print(Royal.password)
print(Royal._password)  # 87654321

Royal.change_password()
print(Royal._password)

# print(Royal.__account_money)
print(Royal._Royal__account_money)  # 800000000000000000000

Royal.add_amount(50000)