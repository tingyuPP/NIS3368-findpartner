from function_class import *
import pymysql

# 创建python和MySQL连接
def create_connection():
    conn = pymysql.connect(
            host="localhost",       # 根据你的数据库主机设置
            user="root",    # MySQL用户名# 
            password="daerwen",# MySQL密码
            database="findpartner"  # 数据库名称
        )
    return conn

# 创建用户，输入用户名，返回user id 出问题返回None
def create_user(name): 
    id = 0
    conn = create_connection()
    cur = conn.cursor()

    sql_1 = '''
        SELECT user_name 
        FROM User_name
        WHERE user_name = (%s)
    '''
    val_1 = (name)
    rtn_1 = cur.execute(sql_1,val_1)
    if rtn_1 :
        return None
    
    sql_2 = '''
        INSERT INTO User_name (user_name)
        VALUES (%s)
    '''
    val_2 = (name)
    rtn_2 = cur.execute(sql_2,val_2)
    id = cur.lastrowid

    sql_3 = '''
        INSERT INTO Users (user_id,user_nickname,user_psword,user_sex,user_hobby,user_image,user_introduction)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    '''
    val_3 = (id,"nickname","psword",-1,"hobby","image","introduction")
    rtn_3 = cur.execute(sql_3,val_3)

    cur.close()
    conn.close()

    return id

# 创建需求，输入用户id，返回notice id
def create_notice(user_id: int):
    id = 0
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        INSERT INTO Notice (user_id,notice_image,notice_basic_type,notice_detail_type,notice_owner_contact,notice_time,notice_location,notice_description,notice_max_places,notice_current_places,notice_if_disabled)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    val = (user_id,"image",-1,"detail_type","owner_contact","time","location","description",2,0,-1)
    rtn = cur.execute(sql,val)
    id = cur.lastrowid

    cur.close()
    conn.close()

    return id

# 查看用户基本信息，输入用户id，返回用户类，没有查询到则返回None
# def check_user_database(id: int)->User:
#     user = User()
#     return user
def check_user_basic_database(id: int):
    user = User()
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM Users
        WHERE user_id = (%s)
    '''
    val = (id)
    rtn = cur.execute(sql,val)

    if cur.rowcount == 0:
        return None

    res = cur.fetclone()
    user.nickname = res[1]
    user.passwords = res[2]
    user.sex = res[3]
    user.hobby = res[4]
    user.image = res[5]
    user.introduction = res[6]

    cur.close()
    conn.close()

    return user

# 查看用户拥有的需求
def check_user_own_list(id:int)->list[int]:

# 查看用户申请的需求
def check_user_request_list(id:int)->list[int]:

# 查看某个request的应答状态
def check_request(user_id:int, notice_id:int)->int:

# 查看需求基本信息，输入需求id，返回需求类，没有查询到则返回None
# def check_notice_database(id: int) -> Notice:
#     notice = Notice()
#     return notice
def check_notice_basic_database(id: int):
    notice = Notice()
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM Notice
        WHERE notice_id = (%s)
    '''
    val = (id)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None

    res = cur.fetchone()
    notice.image = res[2]
    notice.basic_type = res[3]
    notice.detail_type = res[4]
    notice.owner_contact = res[5]
    notice.time = res[6]
    notice.location = res[7]
    notice.description = res[8]
    notice.max_places = res[9]
    notice.current_places = res[10]

    cur.close()
    conn.close()

    return notice

# 全字段检索需求，输入搜索内容，在全字段检索，返回检索结果（需求id列表）, 未查询到返回None
# def search_notice_content_database(notice_content:Notice)->list[int]:
#     notice_list = []
#     return notice_list
def search_notice_content_database(notice_content:Notice):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM Notice
        WHERE CONCART(notice_detail_type, notice_time, notice_location, notice_description) like '%(%s)%'
    '''
    val = (notice_content)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None
    
    i = 0
    for row in cur.fetchall():
        notice_list[i] = row[0] 
        i = i + 1

    cur.close()
    conn.close()

    return notice_list

# 按照大类检索需求，输入搜索内容（某个大类Basic_Type，大类是是现在function_class.py的枚举型），返回需求id列表, 未查询到返回None
# def search_notice_type_database(notice_type:Basic_Type)->list[int]:
#     notice_list = []
#     return notice_list
def search_notice_type_database(notice_type:Basic_Type):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM Notice
        WHERE notice_basic_type = (%s)
    '''
    val = (notice_type)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None

    i = 0
    for row in cur.fetchall():
        notice_list[i] = row[0] 
        i = i + 1

    cur.close()
    conn.close()

    return notice_list

# 按照大类和关键字检索，关键字在除大类以外的4个用户自定义字段（小类、时间、地点、活动描述）中检索，返回需求列表, 未查询到返回None
# def search_notice_all_database(notice_type:Basic_Type, notice_content:Notice)->list[int]:
#     notice_list = []
#     return notice_list
def search_notice_all_database(notice_type:Basic_Type, notice_content:Notice):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM Notice
        WHERE notice_basic_type = (%s) AND CONCART(notice_detail_type, notice_time, notice_location, notice_description) like '%(%s)%'
    '''
    val = (notice_type, notice_content)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None

    i = 0
    for row in cur.fetchall():
        notice_list[i] = row[0] 
        i = i + 1

    cur.close()
    conn.close()

    return notice_list

# 修改用户基本信息，输入用户id、用户修改后的内容，把该id下的非空内容全部用user_content的内容替换，返回是否修改成功
# def change_user_database(user_id:int, user_content:User):
#     if_success = 0
#     return if_success
def change_user_basic_database(user_content : User):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        UPDATE User
        SET user_nickname = (%s), user_psword = (%s), user_sex = (%s), user_hobby = (%s), user_image = (%s), user_introduction = (%s)
        WHERE user_id = (%s)
    '''
    val = (user_content.nickname, user_content.passwords, user_content.sex, user_content.hobby, user_content.image, user_content.introduction, user_content.id)
    rtn = cur.execute(sql, val)
    if cur.rowcount:
        if_success = True
    
    cur.close()
    conn.close()

    return if_success

# 修改需求基本信息，基本同上
# def change_notice_database(id:int, notice_content:Notice):
#     if_success = 0
#     return if_success
def change_notice_basic_database(notice_content:Notice):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()
    sql = '''
        UPDATE Notice
        SET notice_image = (%s), notice_basic_type = (%s), notice_detail_type = (%s), notice_owner_contact = (%s), notice_time = (%s), notice_location = (%s), notice_description = (%s), notice_max_places = (%s), notice_current_places = (%s), notice_if_disabled = (%s) 
        WHERE notice_id = (%s);
    '''
    val = (notice_content.image, notice_content.basic_type, notice_content.detail_type, notice_content.owner_contact, notice_content.time, notice_content.location, notice_content.description, notice_content.max_places, notice_content.current_places, notice_content.if_disabled, notice_content.id)
    rtn = cur.execute(sql, val)
    if cur.rowcount:
        if_success = True
    
    cur.close()
    conn.close()

    return if_success

# 增加request
def add_request(notice_id:int, request_to_add:Request):

# 删除request
def delete_request(notice_id:int, user_id:int):

# 更改reqeust状态
def change_request_state(notice_id:int, request_to_change:Request):

# 根据用户id查找用户名 找不到返回 None
def user_id_to_name(id: int):
    name = None
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM User_name
        WHERE user_id = (%s)
    '''
    val = (id)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None

    res = cur.fetchone()
    name = res[1]

    return name

# 根据用户名查找用户id 找不到返回 None
def user_name_to_id(name):
    id = None
    conn = create_connection()
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM User_name
        WHERE user_name = (%s)
    '''
    val = (name)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        return None

    res = cur.fetchone()
    id = res[0]

    return id