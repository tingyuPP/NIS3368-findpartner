from function import *

action_type = input()

if action_type == '1':
    print("register(user_name, passwords)")
    user_name = input()
    passwords = input()
    result = register(user_name, passwords)
    print("result%s" % result)

elif action_type == '2':
    print("login(user_name, passwords)")
    user_name = input()
    passwords = input()
    result = login(user_name, passwords)
    print("result%s" % result)

elif action_type == '3':
    print("change_password(user_name, password, new_passwords)")
    user_name = input()
    password = input()
    new_password = input()
    result = change_password(user_name, password, new_password)
    print("result%s" % result)

elif action_type == '4':
    print("check_user(user_name)->User")
    user_name = input()
    result = check_user(user_name)
    print(result)