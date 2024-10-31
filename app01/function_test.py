from function import *

while True:
    action_type = input("please enter action type")

    # ok
    if action_type == '1':
        print("register(user_name, passwords)")
        user_name = input()
        passwords = input()
        result = register(user_name, passwords)
        print("result:%s" % result)

    # ok
    elif action_type == '2':
        print("login(user_name, passwords)")
        user_name = input()
        passwords = input()
        result = login(user_name, passwords)
        print("result:%s" % result)

    # ok
    elif action_type == '3':
        print("change_password(user_name, password, new_passwords)")
        user_name = input()
        password = input()
        new_password = input()
        result = change_password(user_name, password, new_password)
        print("result:%s" % result)

    # ok
    elif action_type == '4':
        print("check_user(user_name)->User")
        user_name = input()
        result = check_user(user_name)
        if result != -1:
            print(result.user_name)
            print(result.sex)
            print(result.hobby)
        else:
            print(result)

    # ok
    elif action_type == '5':
        print("check_my_notice(user_name)->list[Notice]")
        user_name = input()
        result = check_my_notice(user_name)
        if result != -1:
            for i in result:
                print(i.basic_type)
        else:
            print(result)

    # ok
    elif action_type == '6':
        print("check_my_enabled_notice(user_name)->list[Notice]")
        user_name = input()
        result = check_my_enabled_notice(user_name)
        if result != -1:
            for i in result:
                print(i.basic_type)
        else:
            print(result)

    # ok
    elif action_type == '7':
        print("check_my_disabled_notice(user_name)->list[Notice]")
        user_name = input()
        result = check_my_disabled_notice(user_name)
        if result != -1:
            if result:
                for i in result:
                    print(i.basic_type)
        else:
            print(result)

    # ok
    elif action_type == '8':
        print("check_request_notice(user_name)->list[Notice]")
        user_name = input()
        result = check_request_notice(user_name)
        if result != -1:
            for i in result:
                print(i.basic_type)
                print(i.owner_contact)
        else:
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
        user_name = input()
        user = check_user(user_name)
        user.nickname = input()
        change_user_info(user)

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

    # ok
    elif action_type == '15':
        print("add_notice(user_name:str)")
        user_name = input()
        result = add_notice(user_name)
        print(result)

    # 如果notice_id不存在会报错/自己request自己的notice是否需要报告
    elif action_type == '16':
        print("request_notice(notice_id:int, user_name:str, contact:str)")
        notice_id = input()
        notice_id = int(notice_id)
        user_name = input()
        # contact = input()
        result = request_notice(notice_id, user_name)
        print("result:%s" % result)

    # ok
    elif action_type == '17':
        print("answer_request(notice_id, user_name, if_answer)")
        notice_id = input()
        notice_id = int(notice_id)
        user_name = input()
        if_answer = input()
        result = answer_request(notice_id, user_name, if_answer)
        print("result:%s" % result)

    elif action_type == '18':
        print("disable_notice(notice_id)")
        notice_id = input()
        notice_id = int(notice_id)
        result = disable_notice(notice_id)
        print("result:%s" % result)

    elif action_type == '19':
        print("enable_notice(notice_id)")
        notice_id = input()
        notice_id = int(notice_id)
        result = enable_notice(notice_id)
        print("result:%s" % result)

    # ok
    elif action_type == '20':
        print("change_notice(notice_content:Notice)")
        print("notice_id, basic_type, owner_contact")
        notice_id = input()
        notice_id = int(notice_id)
        notice =check_notice_basic_database(notice_id)
        notice.basic_type = input()
        notice.owner_contact = input()
        result = change_notice(notice)
        print("result:%s" % result)

    elif action_type == '21':
        print("is_my_notice(user_name, notice_id)")
        user_name = input()
        notice_id = input()
        notice_id = int(notice_id)
        result = is_my_notice(user_name, notice_id)
        print("result:%s" % result)

    elif action_type == '22':
        print("id_to_name(user_id)")
        user_name = input()
        result = id_to_name(user_name)
        print("result:%s" % result)

    elif action_type == '23':
        print("name_to_id(user_name)")
        user_name = input()
        result = name_to_id(user_name)
        print("result:%s" % result)

    elif action_type == '24':
        print("check_request_user(notice_id) -> list[int]")
        post_id = int(input())
        user_list = check_request_user(post_id)
        user_info_list = []
        if user_list:
            for user_id in user_list:
                user_info_list.append(check_user(id_to_name(user_id)))
        for i in user_info_list:
            print(i.nickname)
