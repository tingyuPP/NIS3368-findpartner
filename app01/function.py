# from function_class import *
from django.db.models.expressions import result

from app01.database import *


# 注册函数，输入用户名、密码，创建新账户，返回是否修改成功{0：成功，1：失败}
def register(user_name, passwords):
    user_id = create_user(user_name)
    if not user_id:
        return 1
    user = User(user_id, user_name, passwords)
    if_success = change_user_basic_database(user)
    return if_success

# 登陆函数，输入用户id和密码，返回是否成功登录{0：登录成功，1：密码错误，2：id不存在}
def login(user_name, passwords):
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
        if user.passwords == passwords:
            if_success = 0  # 登录成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = -1  # user不存在
    return if_success

# 更改账号密码，输入用户id、当前密码和新密码，返回修改是否成功{0：修改成功，1：当前密码错误，2：id不存在}
def change_password(user_name, password, new_passwords):
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
        if user.passwords == password:  # 用户存在且密码正确
            user.passwords = new_passwords
            change_user_basic_database(user)
            if_success = 0  # 更改密码成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = -1  # user不存在
    return if_success

# 查看个人信息，输入用户id，返回用户类
def check_user(user_name)->User:
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
    else:
        return -1   # user不存在
    return user

# 查看拥有需求，输入用户id，返回需求列表
def check_my_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        if notice_list:
            for i in notice_list:
                my_notice.append(check_notice_basic_database(i))
    else:
        return -1   # user不存在
    return my_notice    # 没有则返回None

# 查看拥有的处于唤醒态的需求，输入用户id，返回需求列表
def check_my_enabled_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        for i in notice_list:
            notice =check_notice_basic_database(i)
            if not notice.if_disabled:  # 如果处于唤醒态
                my_notice.append(notice)
    else:
        return -1   # user不存在
    return my_notice

# 查看拥有的处于挂起态的需求，输入用户id，返回需求列表
def check_my_disabled_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        for i in notice_list:
            notice =check_notice_basic_database(i)
            if notice.if_disabled:  # 如果处于挂起态
                my_notice.append(notice)
    else:
        return -1   # user不存在
    return my_notice

# 查看申请需求，输入用户id，返回申请的需求（所有状态的）
def check_request_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        for i in notice_list:
            notice = check_notice_basic_database(i)
            result_request_notice.append(notice)
    else:
        return -1   # user不存在
    return result_request_notice

# 查看通过的申请需求，输入用户id，返回通过的申请需求（所有状态）
def check_request_answered_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        for i in notice_list:
            answer_state = check_request(user_id,i)
            if answer_state[0] == 1: # 如果处于被通过态
                result_request_notice.append(check_notice_basic_database(i))
    else:
        return -1   # user不存在
    return result_request_notice

# 查看被拒绝的申请需求，输入用户id，返回被拒绝的申请需求（所有状态）
def check_request_refused_notice(user_name)->list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        for i in notice_list:
            answer_state = check_request(user_id,i)
            if answer_state == 2: # 如果处于被拒绝态
                result_request_notice.append(check_notice_basic_database(i))
    else:
        return -1   # user不存在
    return result_request_notice

# 更改用户信息，输入更改过后的全部用户信息（包括id）（应该是一个User类），返回是否成功{0：修改成功，1：修改失败}
def change_user_info(user_name:str, new_user_info:User):
    user_id = name_to_id(user_name)
    if user_id:
        change_user_basic_database(new_user_info)
        if_success = 0
    else:
        return -1  # user不存在
    return if_success

# 检索需求，输入大类，检测的内容（应该是一个字符串），返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_all(notice_type:Basic_Type, notice_content:str)->list[Notice]:
    # type{0:大类，1:小类，2:时间，3:地点}
    result_id = search_notice_all_database(notice_type, notice_content)
    result_notice = []
    for i in result_id:
        notice = check_notice_basic_database(i)
        if not notice.if_disabled:  # 如果需求处于唤醒态
            result_notice.append(notice)
    return result_notice

# 按照大类检索需求，输入大类，返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_type(notice_type:Basic_Type)->list[Notice]:
    result_id = search_notice_type_database(notice_type)
    result_notice = []
    for i in result_id:
        notice = check_notice_basic_database(i)
        if not notice.if_disabled:  # 如果需求处于唤醒态
            result_notice.append(notice)
    return result_notice

# # 按照内容检索需求，输入具体内容（应该是一个字符串），返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_content(notice_content:str)->list[Notice]:
    result_id = search_notice_content_database(notice_content)
    result_notice = []
    for i in result_id:
        notice = check_notice_basic_database(i)
        if not notice.if_disabled:  # 如果需求处于唤醒态
            result_notice.append(notice)
    return result_notice

# 发布需求，输入发布者id（需求内容可以调用change_notice）
def add_notice(user_name:str):
    user_id = user_name_to_id(user_name)
    notice_id = None
    if user_id:
        notice_id = create_notice(user_id)
    else:
        return -1  # user不存在
    return notice_id

# 对某个需求发起请求，输入需求id、申请人id、申请人联系方式，返回是否成功
def request_notice(notice_id:int, user_name:str, contact:str):
    user_id = user_name_to_id(user_name)
    if_success = False
    if user_id:
        request = Request(user_id, contact, 0)
        if_success = add_request(notice_id,request)
    else:
        return -1  # user不存在
    return if_success

# 应答某个需求的请求，输入需求id，申请人id，是否接收{1：接收，2：拒绝}，返回是否成功
def answer_request(notice_id, user_name, if_answer):
    user_id = user_name_to_id(user_name)
    if_success = False
    if user_id:
        request = Request(user_id, None, if_answer)
        if_success = change_request_state(notice_id, request)
    else:
        return -1  # user不存在
    return if_success

# 挂起需求，输入需求id，返回是否成功
def disable_notice(notice_id):
    notice = check_notice_basic_database(notice_id)
    if_success = False
    if notice:
        notice.if_disabled = True   # 挂起
        if_success = True
    return if_success

# 唤醒需求，输入需求id，返回是否成功
def enable_notice(notice_id):
    notice = check_notice_basic_database(notice_id)
    if_success = False
    if notice:
        notice.if_enabled = False   # 唤醒
        if_success = True
    return if_success

# 更改需求内容，输入更改后的需求（包括id，应为Notice类），返回是否成功
def change_notice(notice_content:Notice):
    if_success = change_notice_basic_database(notice_content)
    return if_success

# 判断是否本人需求，输入用户id和需求id，返回是否为user拥有的需求{0：是，1：否，2：用户不存在，3：需求不存在}
def is_my_notice(user_name, notice_id):
    user_id = user_name_to_id(user_name)
    if user_id:
        user_notice_list = check_user_own_list(user_id)
        if_own = False
        for i in user_notice_list:
            if i == notice_id:
                if_own = True
                break
    else:
        return -1  # user不存在
    return if_own

# 通过user_id查看user_name
def id_to_name(user_id):
    user_name = user_id_to_name(user_id)
    return user_name

# 通过user_name查看user_id
def name_to_id(user_name):
    user_id = user_name_to_id(user_name)
    return user_id