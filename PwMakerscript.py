import string
import secrets

def PasswordMaker():
  lower_case = string.ascii_lowercase
  upper_case = string.ascii_uppercase
  numbers = string.digits
  characters = "!@#$%&"
  user_num = int(input("How long do you want your password?: "))
  #upper_count = int(input("How many upper case letters do you want?: "))
  
    
    
  password = "".join(secrets.choice(lower_case+upper_case+numbers+characters) for i in range(user_num)) 
  

  
  return password

PasswordMaker()