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

elif action_type == '5':
    print("check_my_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_my_notice(user_name)
    print(result)

elif action_type == '6':
    print("check_my_enabled_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_my_enabled_notice(user_name)
    print(result)

elif action_type == '7':
    print("check_my_disabled_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_my_disabled_notice(user_name)
    print(result)

elif action_type == '8':
    print("check_request_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_request_notice(user_name)
    print(result)

elif action_type == '9':
    print("check_request_answered_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_request_answered_notice(user_name)
    print(result)

elif action_type == '10':
    print("check_request_refused_notice(user_name)->list[Notice]")
    user_name = input()
    result = check_request_refused_notice(user_name)
    print(result)

elif action_type == '11':
    print("change_user_info(new_user_info:User)")

elif action_type == '12':
    print("search_notice_all(notice_type:Basic_Type, notice_content:Notice)->list[Notice]")
    notice_type_str = input()
    notice_type = Basic_Type(notice_type_str)
    notice_content = input()
    result = search_notice_all(notice_type, notice_content)
    print(result)

elif action_type == '13':
    print("search_notice_type(notice_type: Basic_Type)->list[Notice]")
    notice_type_str = input()
    notice_type = Basic_Type(notice_type_str)
    result = search_notice_type(notice_type)
    print(result)

elif action_type == '14':
    print("search_notice_content(notice_content:str)->list[Notice]")
    notice_content = input()
    result = search_notice_content(notice_content)
    print(result)


