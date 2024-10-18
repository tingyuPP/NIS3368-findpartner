# from function_class import *
from database import *
# 注册函数，输入密码，创建新账户，返回用户id
def register(password):
    user_id = create_user()
    user = User(user_id, password)
    change_user_database(user_id, user)
    return user_id

# 登陆函数，输入用户id和密码，返回是否成功登录{0：登录成功，1：密码错误，2：id不存在}
def login(user_id, passwords):
    user = check_user_database(user_id)
    if user:
        if user.passwords == passwords:
            if_success = 0  # 登录成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = 2  # id不存在
    return if_success

# 更改账号密码，输入用户id、当前密码和新密码，返回修改是否成功{0：修改成功，1：当前密码错误，2：id不存在}
def change_password(user_id, password, new_passwords):
    user = check_user(user_id)
    if user:
        if user.passwords == password:  # 用户存在且密码正确
            user.passwords = new_passwords
            if_success = 0  # 更改密码成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = 2  # id不存在
    return if_success

# 查看个人信息，输入用户id，返回用户类
def check_user(user_id)->User:
    user = check_user_database(user_id)
    return user

# 查看拥有需求，输入用户id，返回需求列表
def check_my_notice(user_id)->list[Notice]:
    user = check_user_database(user_id)
    notice_list = user.my_notice_id_list
    my_notice = []
    for i in notice_list:
        my_notice.append(check_notice_database(i))
    return my_notice

# 查看申请需求，输入用户id，返回申请的需求
def check_request_notice(user_id)->list[Notice]:
    user = check_user_database(user_id)
    notice_list = user.request_notice_id_list
    request_notice = []
    for i in notice_list:
        request_notice.append(check_notice_database(i))
    return request_notice

# 更改用户信息，输入用户id，更改过后的全部用户信息（除了passwords，passwords应该使用change_passwords)（应该是一个User类），返回是否成功{0：修改成功，1：修改失败}
def change_user_info(user_id, new_user_info):
    user = check_user_database(user_id)
    if user:
        user.nick_name = new_user_info.nick_name
        user.sex = new_user_info.sex
        user.hobby = new_user_info.hobby
        user.introduction = new_user_info.introduction
        if_success = 0
    else:
        if_success = 1
    return if_success

# 检索需求，输入大类，检测的内容（应该是一个字符串），返回检索到的需求列表（没有则为空）
def search_notice_all(type, notice_content):
    # type{0:大类，1:小类，2:时间，3:地点}
    result_id = search_notice_all_database(type, notice_content)
    result = []
    for i in result_id:
        result.append(check_notice_database(i))
    return result


# 按照大类检索需求，输入大类，返回检索到的需求列表（没有则为空）
def search_notice_type(notice_type):
    result_id = search_notice_type_database(notice_type)
    result = []
    for i in result_id:
        result.append(check_notice_database(i))
    return result

# # 按照内容检索需求，输入具体内容（应该是一个字符串），返回检索到的需求列表（没有则为空）
def search_notice_content(notice_content):
    result_id = search_notice_content_database(notice_content)
    result = []
    for i in result_id:
        result.append(check_notice_database(i))
    return result

# 发布需求，输入发布者id，需求内容（Notice类）
def add_notice(user_id,notice_content):
    notice_id = create_notice()

    # 在notice中记录拥有用户的id
    notice_content.owner_id = user_id

    # 在notice拥有者下加入notice的id
    user = check_user_database(user_id)
    user.my_notice_id_list.append(notice_id)
    if_user_success = change_user_database(user_id, user)

    if_notice_success = change_notice_database(notice_id, notice_content)
    if_success = if_user_success and if_notice_success
    return if_success

# 对某个需求发起请求，输入需求id、申请人id、申请人联系方式，返回是否成功
def request_notice(notice_id, user_id, contact):
    user = check_user_database(user_id)
    notice = check_notice_database(notice_id)

    # 在用户中记录申请
    user.request_notice_id_list.append(notice_id)

    # 在需求中记录request
    request = Request(user_id, contact, 0)
    notice.request_list.append(request)

    if_user_success = change_user_database(user_id, user)
    if_notice_success = change_notice_database(notice_id, notice)
    if_success = if_user_success and if_notice_success

    return if_success

# 应答某个需求的请求，输入需求id，申请人id，是否接收{1：接收，2：拒绝}，返回是否成功
def answer_request(notice_id, user_id, if_answer):
    notice = check_notice_database(notice_id)
    if_success = 1
    for request in notice.request_list:
        if request.id == user_id:
            request.answer = if_answer
            if_success = 0
    return if_success

# 挂起需求，输入需求id，返回是否成功
def disable_notice(id):
    notice = check_notice_database(id)
    if_success = 1
    if notice:
        notice.if_disabled = True
        if_success = 0
    return if_success

# 唤醒需求，输入需求id，返回是否成功
def enable_notice(id):
    if_success = 0
    return if_success

# 更改需求内容，输入需求id，更改后的需求（全部内容，应该为Notice类），返回是否成功
def change_notice(id, notice_content):
    if_success = 0
    return if_success

# 判断是否本人需求，输入用户id和需求id，返回是否为user拥有的需求
def is_my_notice(uer_id, notice_id):
    result = 0
    return result

