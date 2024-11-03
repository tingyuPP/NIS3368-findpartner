from app01.function_class import *
import pymysql


# 创建python和MySQL连接
def create_connection():
    conn = pymysql.connect(
        host="localhost",  # 根据你的数据库主机设置
        user="root",  # MySQL用户名#
        # password="daerwen",# MySQL密码
        # password="123456",
        password = "Cyf20040629",
        database="findpartner",  # 数据库名称
    )
    return conn


# 创建用户 输入用户名 返回user_id 用户名已存在返回None
def create_user(name):
    id = 0
    conn = create_connection()
    cur = conn.cursor()

    sql_1 = """
        SELECT user_name
        FROM Users
        WHERE user_name = (%s)
    """
    val_1 = name
    rtn_1 = cur.execute(sql_1, val_1)
    if cur.rowcount:
        cur.close()
        conn.close()
        return None

    sql_2 = """
        INSERT INTO Users (user_name, user_nickname, user_psword, user_sex, user_hobby, user_image, user_introduction)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    val_2 = (name, name, "psword", "unknown", "hobby", "image", "introduction")
    rtn_2 = cur.execute(sql_2, val_2)
    conn.commit()
    id = cur.lastrowid

    cur.close()
    conn.close()

    return id


# 创建需求，输入用户id 返回notice_id 未创建成功返回None
def create_notice(user_id: int):
    id = 0
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO Notice (user_id, notice_image, notice_basic_type, notice_title, notice_owner_contact, notice_time, notice_tag, notice_description, notice_if_disabled)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    val = (
        user_id,
        "image",
        -1,
        "unknown_title",
        "unknown_owner_contact",
        "unknown_time",
        "unknown_tag",
        "unknown_description",
        0,
    )
    rtn = cur.execute(sql, val)
    conn.commit()

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    id = cur.lastrowid

    cur.close()
    conn.close()

    return id


# 查看用户基本信息 输入用户id 返回用户类 没有查询到则返回None
def check_user_basic_database(id: int):
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT *
        FROM Users
        WHERE user_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    res = cur.fetchone()
    user = User(id, res[1], res[3])
    user.nickname = res[2]
    user.sex = res[4]
    user.hobby = res[5]
    user.image = res[6]
    user.introduction = res[7]

    cur.close()
    conn.close()

    return user


# 查看用户拥有的需求 返回一个list 未查询到返回None
def check_user_own_list(id: int):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT notice_id
        FROM Notice
        WHERE user_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    i = 0
    for line in cur.fetchall():
        notice_list.append(line[0])

    cur.close()
    conn.close()

    return notice_list

def check_notice_request_list(id: int):
    request_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT user_id
        FROM Requests
        WHERE notice_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    i = 0
    for line in cur.fetchall():
        request_list.append(line[0])

    cur.close()
    conn.close()

    return request_list


# 查看用户申请的需求 返回一个list 未查询到返回None
def check_user_request_list(id: int):
    request_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT notice_id
        FROM Requests
        WHERE user_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    i = 0
    for line in cur.fetchall():
        request_list.append(line[0])

    cur.close()
    conn.close()

    return request_list


# 查看某个request的应答状态 返回应答状态 未查询到返回None
def check_request(user_id: int, notice_id: int):
    ans = 0
    # 申请状态 0-未知 1-通过 2-未通过
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT answer_state
        FROM Requests
        WHERE user_id = (%s) AND notice_id = (%s)
    """
    val = (user_id, notice_id)
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    ans = cur.fetchone()
    cur.close()
    conn.close()

    return ans


# 查看需求基本信息 输入需求id 返回需求类 没有查询到则返回None
def check_notice_basic_database(id: int):
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT *
        FROM Notice
        WHERE notice_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    res = cur.fetchone()
    notice = Notice(id, res[1], res[5], res[4], res[3])
    notice.image = res[2]
    notice.time = res[6]
    notice.tag = res[7].split("$")
    notice.description = res[8]
    notice.if_disabled = res[9]

    cur.close()
    conn.close()

    return notice


# 返回所有需求
def check_all_notice_database():
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT *
        FROM Notice
        WHERE notice_if_disabled = 0
    """
    rtn = cur.execute(sql)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    for row in cur.fetchall():
        notice_list.append(row[0])

    cur.close()
    conn.close()
    return notice_list


# 全字段检索需求 输入搜索内容，在全字段检索 返回list(需求id列表) 未查询到返回None
def search_notice_content_database(notice_content):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT notice_id
        FROM Notice
        WHERE CONCAT(notice_title, notice_time, notice_tag, notice_description) like (%s)
    """
    notice_content = "%" + notice_content + "%"
    val = notice_content
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    for row in cur.fetchall():
        notice_list.append(row[0])

    cur.close()
    conn.close()

    return notice_list


# 按照大类检索需求 输入搜索内容(某个大类Basic_Type(自定义枚举类型)) 返回list(需求id列表) 未查询到返回None
def search_notice_type_database(notice_type: int):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT notice_id
        FROM Notice
        WHERE notice_basic_type = (%s)
    """
    # notice_type_int = notice_type.value
    val = notice_type
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    for row in cur.fetchall():
        notice_list.append(row[0])

    cur.close()
    conn.close()

    return notice_list


# 按照大类和关键字检索 关键字在除大类以外的4个用户自定义字段(小类、时间、地点、活动描述)中检索 返回list(需求id列表) 未查询到返回None
def search_notice_all_database(notice_type: int, notice_content):
    notice_list = []
    conn = create_connection()
    cur = conn.cursor()

    notice_content = "%" + notice_content + "%"
    sql = """
        SELECT notice_id
        FROM Notice
        WHERE notice_basic_type = (%s) AND CONCAT(notice_title, notice_time, notice_tag, notice_description) like (%s)
    """
    # notice_type = notice_type.value
    val = (notice_type, notice_content)
    cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    for row in cur.fetchall():
        notice_list.append(row[0])

    cur.close()
    conn.close()

    return notice_list


# 修改用户基本信息 输入用户修改后的内容 把该id下的非空内容全部用user_content的内容替换 返回是否修改成功
def change_user_basic_database(user_content: User):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        UPDATE Users
        SET user_name = (%s), user_nickname = (%s), user_psword = (%s), user_sex = (%s), user_hobby = (%s), user_image = (%s), user_introduction = (%s)
        WHERE user_id = (%s);
    """
    val = (
        user_content.user_name,
        user_content.nickname,
        user_content.passwords,
        user_content.sex,
        user_content.hobby,
        user_content.image,
        user_content.introduction,
        user_content.id,
    )
    rtn = cur.execute(sql, val)
    conn.commit()

    if cur.rowcount:
        if_success = True

    cur.close()
    conn.close()

    return if_success


# 修改需求基本信息 基本同上
def change_notice_basic_database(notice_content: Notice):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        UPDATE Notice
        SET notice_image = (%s), notice_basic_type = (%s), notice_title = (%s), notice_owner_contact = (%s), notice_time = (%s), notice_tag = (%s), notice_description = (%s), notice_if_disabled = (%s) 
        WHERE notice_id = (%s);
    """
    # notice_type = int(notice_content.basic_type.value)
    tag_str = "$".join(notice_content.tag)
    val = (
        notice_content.image,
        notice_content.basic_type,
        notice_content.title,
        notice_content.owner_contact,
        notice_content.time,
        tag_str,
        notice_content.description,
        notice_content.if_disabled,
        notice_content.id,
    )
    rtn = cur.execute(sql, val)

    if cur.rowcount:
        conn.commit()
        if_success = True

    cur.close()
    conn.close()

    return if_success


# 增加request 输入被申请的notice_id和申请类(包括申请人user_id 申请人联系方式和应答状态) 返回是否成功 若该申请人已经申请过返回False
def add_request(notice_id: int, request_to_add: Request):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql_1 = """
        SELECT *
        FROM Requests
        WHERE user_id = (%s) AND notice_id = (%s)
    """
    val_1 = (request_to_add.id, notice_id)
    rtn_1 = cur.execute(sql_1, val_1)
    if cur.rowcount:
        cur.close()
        conn.close()
        return if_success

    sql_2 = """
        INSERT INTO Requests (user_id, notice_id, request_contact, answer_state)
        VALUES (%s, %s, %s, %s)
    """
    val_2 = (
        request_to_add.id,
        notice_id,
        request_to_add.contact,
        request_to_add.answer_state,
    )
    rtn_2 = cur.execute(sql_2, val_2)

    if cur.rowcount:
        conn.commit()
        if_success = True

    cur.close()
    conn.close()
    return if_success


# 删除request 输入被申请的notice_id和 申请人user_id 返回是否成功 若该申请不存在返回False
def delete_request(notice_id: int, user_id: int):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql_1 = """
        SELECT *
        FROM Requests
        WHERE user_id = (%s) AND notice_id = (%s)
    """
    val_1 = (user_id, notice_id)
    rtn_1 = cur.execute(sql_1, val_1)
    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return if_success

    sql_2 = """
        DELETE
        FROM Requests
        WHERE user_id = (%s) AND notice_id = (%s)
    """
    val_2 = (user_id, notice_id)
    rtn_2 = cur.execute(sql_2, val_2)

    if cur.rowcount:
        conn.commit()
        if_success = True

    cur.close()
    conn.close()
    return if_success


# 更改reqeust状态 输入被申请的notice_id和申请类(包括申请人user_id 申请人联系方式和应答状态) 返回是否成功
def change_request_state(notice_id: int, request_to_change: Request):
    if_success = False
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        UPDATE Requests
        SET request_contact = (%s), answer_state = (%s)
        WHERE user_id = (%s) AND notice_id = (%s);
    """
    val = (
        request_to_change.contact,
        request_to_change.answer_state,
        request_to_change.id,
        notice_id,
    )
    rtn = cur.execute(sql, val)

    if cur.rowcount:
        conn.commit()
        if_success = True

    cur.close()
    conn.close()

    return if_success


# 根据用户id查找用户名 找不到返回 None
def user_id_to_name(id: int):
    name = None
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT user_name
        FROM Users
        WHERE user_id = (%s)
    """
    val = id
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    res = cur.fetchone()
    name = res[0]

    cur.close()
    conn.close()

    return name


# 根据用户名查找用户id 找不到返回 None
def user_name_to_id(name):
    id = None
    conn = create_connection()
    cur = conn.cursor()

    sql = """
        SELECT user_id
        FROM Users
        WHERE user_name = (%s)
    """
    val = name
    rtn = cur.execute(sql, val)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return None

    res = cur.fetchone()
    id = res[0]

    cur.close()
    conn.close()

    return id
