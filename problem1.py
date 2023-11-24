#class - blueprint used to create objects


#objects- an instance of a class 

#instances - Specific occurence of an object - the actual object created from a class
#Has own data but shares methods in the class 
#instance + object is used interchangeable - concrete realization of a class

#method - functions associated w a class
#attribute - variable associated w a class 

#Class Variables - shared by all instances of a class
#Instance Variables - unique to each instance
#You can access class variable by class name or instance of a class (self)
# ** In this case, class name is Employee

#Regular Methods - automatically take instance (self) as first argument 
#Static Methods - don't pass instance or class automatically - have logical connection w class
#Turn reg method to static method - add decorator @staticmethod
#Class Methods - automatically take class (cls) as first argument
#Turn regular method to class method - add decorator @classmethod
#Convention for class variables - cls
#Can use class methods as alternative constructors
#con't class methods provide multiple ways to create objects

#Inheritance - can make subclasses that have same functionality as parent class
#Can add methods/change the features for a subgroup 

class Employee:
    #emp_amt = 0
    raise_amt = 1.05
    #Name, Pay, Email - attributes of the class
    #__init__ is the initializer/constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." +last+"@company.com"

        #Employee.emp_amt += 1
    #A method of a class - a function in a class 
    # Each Method within a class automatically takes the instance as the first argument   
    def fullname(self):
        return f"{self.first} {self.last}"


    def eoy_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # #Working w class not instance
    # @classmethod
    # def set_raise_amt(cls,amount):
    #     cls.raise_amt = amount

    # #Alternative Constructor Using Class method
    # #Convention: def from_ 
    # @classmethod
    # def from_string(cls,emp_str):
    #     #Splits the string 
    #     first, last, pay = emp_str.split("-")
    #     #Creates and returns a new employee object
    #     return cls(first, last, pay)
    # #Static Method example - can pass in the arguments you want to work w
    # #If you dont access the class or instance anywhere in the function, use static method
    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True

   
    # def net_pay(self):
    #     return f"{self.pay}"  

    # def gross_pay(self):
    #     new_pay = int(self.pay * 1/2)
    #     return f"{new_pay}"

#subclass of class Employee    
class Developer(Employee):
   raise_amt = 1.6
   #When creating a new __init__  method, use super().__init__(self args from parent class)
   #Can use className.__init__(self, args from parent __init__) instead of super() if doing one inheritance
   #allows Employee class to handle first, last, pay args while Developer class handles prog_lang
   def __init__(self, first, last, pay, prog_lang):
       super().__init__(first, last, pay)
       self.prog_lang = prog_lang
#Never pass mutable data types as __init__/ default args
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
       super().__init__(first, last, pay)
       if employees is None:
            self.employees = []
       else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
           self.employees.append(emp)
    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())


dev_1 = Developer("Zoe","Carter",60000, "python")
dev_2 = Developer("Rossini", "Bessentie", 100000, "SQL")
mgr_1 = Manager("Aurora", "Bessentie", 1000, [dev_1])

print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))
#print(mgr_1.pay)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()
#print(mgr_1.add_emp("Sean"))
#print(mgr_1.print_emp())
#print(dev_1.email)


# print(help(Developer))
# print(dev_1.email)
# import datetime
# my_date = datetime.date(2023, 10, 2)
# print(Employee.is_workday(my_date))

# emp_str_1 = "Jane-Doe-5000"
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# emp_1.set_raise_amt(2.06)
# #Employee.raise_amt = 1.03
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)



# import random
# def get_choices():
#     options = ["rock","paper","scissors"]
#     player_choice = str(input("Enter a choice (rock, paper, scissors): "))
#     computer_choice = random.choice(options)
#     choice = {"player":player_choice, "computer":computer_choice}
#     return choice

# def check_win(player, computer):
#     print(f"You chose {player}, Computer chose {computer}.")
#     if player == computer:
#         return "Draw"
#     elif player == "rock":
#         if computer == "scissors":
#             return "Rock beats Scissors"
#         else:
#             return "Paper beats Rock"
#     elif player == "paper":
#         if computer == "rock":
#             return "Paper beats Rock"
#         else:
#             return "Rock beats Scissors"
#     elif player == "scissor":
#         if computer == "paper":
#             return "Scissor beats paper"
#         else:
#             return "Rock beats Scissors"

# wins = check_win("rock","paper")
# choices = get_choices()
# # print(wins)