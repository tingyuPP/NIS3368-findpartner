from function_class import *

# 创建用户，无输入，返回user id
def create_user():
    id = 0
    return id

# 创建需求，无输入，返回notice id
def create_notice():
    id = 0
    return id

# 查看用户，输入用户id，返回用户类，没有查询到则返回-1
def check_user_database(id):
    user = 0
    return user

# 查看需求，输入需求id，返回需求类，没有查询到则返回-1
def check_notice_database(id):
    notice = 0
    return notice

# 检索需求，输入检索type，检索内容，返回检索结果（需求列表）
# 这部分可以和check_user_database一起实现，但是通过id检索需求会经常调用，所以最好分开实现
def search_notice_database(type, notice_content):
    notice_list = []
    return notice_list

# 修改用户信息，输入用户id、用户修改后的内容，把该id下的内容全部用user_content的内容替换，返回是否修改成功
def change_user_database(id, user_content):
    if_success = 0
    return if_success


# 修改需求信息
def change_notice_database(id, notice_content):
    if_success = 0
    return if_success
