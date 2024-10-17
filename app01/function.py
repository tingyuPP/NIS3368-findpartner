# from function_class import *
from database import *
# 注册函数，输入密码，创建新账户，返回用户id
def register(password):
    user_id = create_user()
    user = User(user_id, password)
    change_user_database(user_id, user)
    return user_id

# 登陆函数，输入用户id和密码，返回是否成功登录{0：登录成功，1：密码错误，2：id不存在}
def login(id, passwords):
    user = check_user_database(id)
    if user:
        if user.passwords == passwords:
            if_success = 0  # 登录成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = 2  # id不存在
    return if_success

# 更改账号密码，输入用户id、当前密码和新密码，返回修改是否成功{0：修改成功，1：当前密码错误，2：id不存在}
def change_password(id, password, new_passwords):
    user = check_user(id)
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
def check_user(id):
    user = check_user_database(id)
    return user

# 查看拥有需求，输入用户id，返回需求列表
def check_my_notice(id):
    user = check_user_database(id)

    my_notice = []
    return my_notice

# 查看申请需求，输入用户id，返回申请的需求
def check_request_notice(id):
    request_notice = []
    return request_notice

# 更改用户信息，输入用户id，更改过后的全部用户信息（应该是一个User类），返回是否成功
def change_user_info(id, new_user_info):
    if_success = id
    return if_success

# 检索需求，输入检测type，检测的内容（应该是一个Notice类，但是其中只需要检测type对应的位置有数值即可），返回检索到的需求列表
def search_notice(type, notice_content):
    # type{0:大类，1:小类，2:时间，3:地点}
    result = []
    if type == 0:
        result = []
    return result

# 发布需求，输入需求内容（Notice类）
def add_notice(notice_content):
    if_success = 0
    return if_success

# 对某个需求发起请求，输入需求id，返回是否成功
def request_notice(id):
    if_success = 0
    return if_success

# 应答某个需求的请求，输入需求id，申请人id，是否接收，返回是否成功
def anwser_rquest(notice_id, request_id, if_anwser):
    if_success = 0
    return if_success

# 挂起需求，输入需求id，返回是否成功
def disable_notice(id):
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

