user_name = input("Enter your User name ")
password = input("Enter your password ")

password2 = len(f'{password}') 

password3 = password2 * "*"

print(f'Your user name is {user_name}. Your password is {password3} {password2} Characters long')
