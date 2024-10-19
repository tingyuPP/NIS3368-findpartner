from function_class import *
import mysql_connector

# 创建python和MySQL连接
def create_connection():
    connection = mysql.connector.connect(
            host="localhost",       # 根据你的数据库主机设置
            user="root",    # MySQL用户名
            password="daerwen",# MySQL密码
            database="findpartner"  # 数据库名称
        )

# 创建用户，无输入，返回user id
def create_user():
    id = 0
    return id

# 创建需求，无输入，返回notice id
def create_notice():
    id = 0
    return id

# 查看用户，输入用户id，返回用户类，没有查询到则返回None
def check_user_database(id: int)->User:
    user = User()
    return user

# 查看需求，输入需求id，返回需求类，没有查询到则返回None
def check_notice_database(id: int) -> Notice:
    notice = Notice()
    return notice

# 全字段检索需求，输入索内容，在全字段检索，返回检索结果（需求id列表）
def search_notice_content_database(notice_content:Notice)->list[int]:
    notice_list = []
    return notice_list

# 按照大类检索需求，输入搜索内容（某个大类Basic_Type，大类是是现在function_class.py的枚举型），返回需求id列表
def search_notice_type_database(notice_type:Basic_Type)->list[int]:
    notice_list = []
    return notice_list

# 按照大类和关键字检索，关键字在除大类以外的4个用户自定义字段（小类、时间、地点、活动描述）中检索，返回需求列表
def search_notice_all_database(notice_type:Basic_Type, notice_content:Notice)->list[int]:
    notice_list = []
    return notice_list

# 修改用户信息，输入用户id、用户修改后的内容，把该id下的非空内容全部用user_content的内容替换，返回是否修改成功
def change_user_database(user_id:int, user_content:User):
    if_success = 0
    return if_success


# 修改需求信息，基本同上
def change_notice_database(id:int, notice_content:Notice):
    if_success = 0
    return if_success
