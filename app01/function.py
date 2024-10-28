# from function_class import *
from django.db.models.expressions import result

from app01.database import *
from Crypto.Cipher import AES
import base64


# 注册函数，输入用户名、密码，创建新账户，返回是否修改成功{0：成功，1：失败}
def register(user_name, passwords):
    user_id = create_user(user_name)
    if not user_id:
        return 1
    passwords = encrypt_oracle(passwords)
    user = User(user_id, user_name, passwords)
    if_success = change_user_basic_database(user)
    if if_success:
        if_success = 0
    return if_success


# 登陆函数，输入用户id和密码，返回是否成功登录{0：登录成功，1：密码错误，-1：id不存在}
def login(user_name, passwords):
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
        if user.passwords == encrypt_oracle(passwords):
            if_success = 0  # 登录成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = -1  # user不存在
    return if_success


# 更改账号密码，输入用户id、当前密码和新密码，返回修改是否成功{0：修改成功，1：当前密码错误，-1：id不存在}
def change_password(user_name, password, new_passwords):
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
        if user.passwords == encrypt_oracle(password):  # 用户存在且密码正确
            user.passwords = encrypt_oracle(new_passwords)
            change_user_basic_database(user)
            if_success = 0  # 更改密码成功
        else:
            if_success = 1  # 密码错误
    else:
        if_success = -1  # user不存在
    return if_success


# 查看个人信息，输入用户id，返回用户类{-1：用户不存在，user类：正常返回}
def check_user(user_name) -> User:
    user_id = user_name_to_id(user_name)
    if user_id:
        user = check_user_basic_database(user_id)
    else:
        return -1  # user不存在
    return user


# 查看所有需求
def check_all_notice() -> list[Notice]:
    notice_list = []
    notice_id_list = check_all_notice_database()
    if not notice_id_list:
        return None
    else:
        for i in notice_id_list:
            notice_list.append(check_notice_basic_database(i))
    return notice_list


# 查看拥有需求，输入用户id，返回需求列表{-1：用户不存在，notice类list：正常返回}
def check_my_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        if notice_list:
            for i in notice_list:
                my_notice.append(check_notice_basic_database(i))
        else:
            return None
    else:
        return -1  # user不存在
    return my_notice  # 没有则返回None


# 查看拥有的处于唤醒态的需求，输入用户id，返回需求列表{-1：用户不存在，notice类list：正常返回}
def check_my_enabled_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        if notice_list:
            for i in notice_list:
                notice = check_notice_basic_database(i)
                if not notice.if_disabled:  # 如果处于唤醒态
                    my_notice.append(notice)
        else:
            return None
    else:
        return -1  # user不存在
    return my_notice


# 查看拥有的处于挂起态的需求，输入用户id，返回需求列表{-1：用户不存在，notice类list：正常返回}
def check_my_disabled_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_own_list(user_id)
        my_notice = []
        if notice_list:
            for i in notice_list:
                notice = check_notice_basic_database(i)
                if notice.if_disabled:  # 如果处于挂起态
                    my_notice.append(notice)
        else:
            return None
    else:
        return -1  # user不存在
    return my_notice


# 查看申请需求，输入用户id，返回申请的需求（所有状态的）{-1：用户不存在，request类list：正常返回}
def check_request_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        if notice_list:
            for i in notice_list:
                notice = check_notice_basic_database(i)
                result_request_notice.append(notice)
        else:
            return None
    else:
        return -1  # user不存在
    return result_request_notice


# 查看通过的申请需求，输入用户id，返回通过的申请需求（所有状态）{-1：用户不存在，request类list：正常返回}
def check_request_answered_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        if notice_list:
            for i in notice_list:
                answer_state = check_request(user_id, i)
                if answer_state[0] == 1:  # 如果处于被通过态
                    result_request_notice.append(check_notice_basic_database(i))
        else:
            return None
    else:
        return -1  # user不存在
    return result_request_notice


# 查看被拒绝的申请需求，输入用户id，返回被拒绝的申请需求（所有状态）{-1：用户不存在，request类list：正常返回}
def check_request_refused_notice(user_name) -> list[Notice]:
    user_id = user_name_to_id(user_name)
    if user_id:
        notice_list = check_user_request_list(user_id)
        result_request_notice = []
        if notice_list:
            for i in notice_list:
                answer_state = check_request(user_id, i)
                if answer_state[0] == 2:  # 如果处于被拒绝态
                    result_request_notice.append(check_notice_basic_database(i))
        else:
            return None
    else:
        return -1  # user不存在
    return result_request_notice


# 更改用户信息，输入更改过后的全部用户信息（包括id）（应该是一个User类），返回是否成功{0：修改成功，-1：用户不存在}
def change_user_info(new_user_info: User):
    user_name = new_user_info.user_name
    user_id = name_to_id(user_name)
    if user_id:
        change_user_basic_database(new_user_info)
        if_success = 0
    else:
        return -1  # user不存在
    return if_success


# 发布需求，输入发布者id（需求内容可以调用change_notice）{-1；用户不存在，正整数：notice_id}
def add_notice(user_name: str):
    user_id = user_name_to_id(user_name)
    notice_id = None
    if user_id:
        notice_id = create_notice(user_id)
    else:
        return -1  # user不存在
    return notice_id


# 根据notice_id获得notice的内容（不存在则返回空值）
def check_notice(notice_id: int) -> Notice:
    notice = check_notice_basic_database(notice_id)
    if notice:
        return notice
    else:
        return None


# 根据notice_id获取用户的信息
def check_notice_owner(notice_id: int) -> User:
    notice = check_notice_basic_database(notice_id)
    user_id = notice.owner_id
    user = check_user_basic_database(user_id)
    return user


# 更改需求内容，输入更改后的需求（包括id，应为Notice类），返回是否成功{0：成功，-1：需求不存在}
def change_notice(notice_content: Notice):
    if check_notice_basic_database(notice_content.id):
        if_success = change_notice_basic_database(notice_content)
        if if_success:
            if_success = 0
    else:
        if_success = -1
    return if_success


# 检索需求，输入大类，检测的内容（应该是一个字符串），返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_all(notice_type: Basic_Type, notice_content: str) -> list[Notice]:
    result_id = search_notice_all_database(notice_type, notice_content)
    print(result_id)
    result_notice = []
    for i in result_id:
        notice = check_notice_basic_database(i)
        if not notice.if_disabled:  # 如果需求处于唤醒态
            result_notice.append(notice)
    return result_notice


# 按照大类检索需求，输入大类，返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_type(notice_type: Basic_Type) -> list[Notice]:
    result_id = search_notice_type_database(notice_type)
    result_notice = []
    for i in result_id:
        notice = check_notice_basic_database(i)
        if not notice.if_disabled:  # 如果需求处于唤醒态
            result_notice.append(notice)
    return result_notice


# # 按照内容检索需求，输入具体内容（应该是一个字符串），返回检索到的需求列表（唤醒的）（没有则为空）
def search_notice_content(notice_content: str) -> list[Notice]:
    result_id = search_notice_content_database(notice_content)
    result_notice = []
    if result_id:
        for i in result_id:
            notice = check_notice_basic_database(i)
            if not notice.if_disabled:  # 如果需求处于唤醒态
                result_notice.append(notice)
    else:
        return None
    return result_notice


# 对某个需求发起请求，输入需求id、申请人id、申请人联系方式，返回是否成功{0：成功，-1：用户不存在，-2：需求不存在}
def request_notice(notice_id: int, user_name: str, contact: str):
    user_id = user_name_to_id(user_name)
    if_success = False
    if user_id:
        if check_notice_basic_database(notice_id):
            request = Request(user_id, contact, 0)
            if_success = add_request(notice_id, request)
            if if_success:
                if_success = 0
        else:
            if_success = -2  # notice不存在
    else:
        if_success = -1  # user不存在
    return if_success


# 应答某个需求的请求，输入需求id，申请人id，是否接收{1：接收，2：拒绝}，返回是否成功{0：成功，-1：用户不存在，-2：需求不存在}
def answer_request(notice_id, user_name, if_answer):
    user_id = user_name_to_id(user_name)
    if_success = False
    if user_id:
        if check_notice_basic_database(notice_id):
            request = Request(user_id, None, if_answer)
            if_success = change_request_state(notice_id, request)
            if if_success:
                if_success = 0
        else:
            if_success = -2
    else:
        if_success = -1  # user不存在
    return if_success


# 挂起需求，输入需求id，返回是否成功{0：成功，-1：需求不存在}
def disable_notice(notice_id):
    notice = check_notice_basic_database(notice_id)
    if_success = -1
    if notice:
        notice.if_disabled = 1  # 挂起
        change_notice_basic_database(notice)
        if_success = 0
    return if_success


# 唤醒需求，输入需求id，返回是否成功{0：成功，-1：需求不存在}
def enable_notice(notice_id):
    notice = check_notice_basic_database(notice_id)
    if_success = -1
    if notice:
        notice.if_disabled = 0  # 唤醒
        change_notice_basic_database(notice)
        if_success = 0
    return if_success


# 判断是否本人需求，输入用户id和需求id，返回是否为user拥有的需求{0：是，1：否，-1：用户不存在，-2：需求不存在}
def is_my_notice(user_name, notice_id):
    user_id = user_name_to_id(user_name)
    if user_id:
        if check_notice_basic_database(notice_id):
            user_notice_list = check_user_own_list(user_id)
            if_own = 1  # 否
            for i in user_notice_list:
                if i == notice_id:
                    if_own = 0  # 是
                    break
        else:
            if_own = -2  # 需求不存在
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


#################以下为一些工具函数##########################
# 补全函数，确保字符串长度是16的倍数
def add_to_16(value):
    if isinstance(value, str):  # 如果是字符串，继续处理
        while len(value) % 16 != 0:
            value += "\0"
        return value.encode("utf-8")  # 最终返回字节类型
    elif isinstance(value, bytes):  # 如果是字节类型，直接处理
        while len(value) % 16 != 0:
            value += b"\0"
        return value
    else:
        raise TypeError("The value must be a str or bytes")


# 加密方法
def encrypt_oracle(text):
    # 秘钥
    key = "123456"
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行AES加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = str(
        base64.encodebytes(encrypt_aes), encoding="utf-8"
    )  # 执行加密并转码返回bytes
    return encrypted_text


# 解密方法
def decrypt_oracle(text):
    # 秘钥
    key = "123456"
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding="utf-8"))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding="utf-8").replace(
        "\0", ""
    )
    return decrypted_text


def serialize_notice(obj):
    owner_username = id_to_name(obj.owner_id)
    owner_info = check_user(owner_username)
    return {
        "id": obj.id,
        "owner_id": obj.owner_id,
        "owner_contact": obj.owner_contact,
        "owner_nickname": owner_info.nickname,
        "owner_avatar": owner_info.image,
        "title": obj.title,
        "description": obj.description,
        "basic_type": obj.basic_type,
        "time": obj.time,
        "image": obj.image,
        "if_disabled": obj.if_disabled,
    }
