from function_class import *

# 创建用户，无输入，返回user id
def create_user():
    id = 0
    return id

# 创建需求，无输入，返回notice id
def create_notice():
    id = 0
    return id

# 查看用户，输入用户id，返回用户类，没有查询到则返回None
def check_user_database(id):
    user = User()
    return user

# 查看需求，输入需求id，返回需求类，没有查询到则返回None
def check_notice_database(id):
    notice = 0
    return notice

# 全字段检索需求，输入索内容，在全字段检索，返回检索结果（需求id列表）
def search_notice_database(notice_content):
    notice_list = []
    return notice_list

# 按照大类检索需求，输入搜索内容（某个大类Basic_Type，大类是是现在function_class.py的枚举型），返回需求id列表
def search_notice_type_database(notice_type):
    notice_list = []
    return notice_list

# 按照大类和关键字检索，关键字在除大类以外的4个用户自定义字段（小类、时间、地点、活动描述）中检索，返回需求列表
def search_notice_all_database(notice_type, notice_content):
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
