from enum import Enum

# 定义需求的大类：体育，学习，吃饭，游戏，出行，情感
class Basic_Type(Enum):
    sport = 0
    study = 1
    food = 2
    game = 3
    travel = 4
    emotion = 5

class Request:
    def __init__(self, user_request_id, contact, answer_state = 0):
        self.id = user_request_id           # 申请人的id，不可缺省且唯一
        self.contact = contact              # 申请人的联系方式，不可缺省
        self.answer_state = answer_state    # 申请是否被通过{0:未知, 1:通过, 2:不通过}

class User:
    def __init__(self, user_id, user_name, passwords, nickname = "unknown", image = None, sex = "unknown", hobby = "unknown", introduction = "unknown", my_notice_id_list = None,  request_notice_id_list = None):
        self.id = user_id                   # 用户id，不能缺省且唯一
        self.user_name = user_name          # 用户名，不能缺省且唯一
        self.passwords = passwords          # 用户密码，不能缺省

        # 用户个人信息
        self.nickname = user_name          # 用户昵称，缺省值为user_name
        self.image = "https://gss0.bdstatic.com/6LZ1dD3d1sgCo2Kml5_Y_D3/sys/portraith/item/tb.1.bead35fc.MtiwdXhDXbnsPJ6EQHv6kg"       # 用户头像，为图片url，缺省值为空
        self.sex = sex                      # 性别，缺省值为“unknown”
        self.hobby = hobby                  # 爱好，缺省值为“unknown”
        self.introduction = introduction    # 签名，缺省值为“unknown”

        # # 用户拥有的需求id表
        # if my_notice_id_list:
        #     self.my_notice_id_list = my_notice_id_list    # 使用传入的数组（list）
        # else:
        #     self.my_notice_id_list = []        # 如果缺省就创建空数组（list）
        #
        # # 用户申请的需求id表
        # if request_notice_id_list:
        #     self.request_notice_id_list = request_notice_id_list    # 使用传入的数组（list）
        # else:
        #     self.request_notice_id_list = []        # 如果缺省就创建空数组（list）


class Notice:
    def __init__(self, notice_id, owner_id, owner_contact, title = "unknown",  basic_type = 0, image = None, tag_list = None, time = "unknown", description = "unknown", current_places = "1", max_places = "2", if_disabled = False, request_n = 0, request_list = None):
        self.id = notice_id                 # 需求id，不能缺省且唯一
        self.owner_id = owner_id            # 需求所有者的用户id，不能缺省
        self.owner_contact = owner_contact  # 需求所有者的联系方式，不能缺省

        # 需求的基本信息
        self.title = title                  # 标题
        self.description = description      # 具体内容
        self.basic_type = basic_type        # 大类（这里应当传入一个Basic_Type类的参数，但是并未做检查）
        self.tag = tag_list                 # tag
        self.time = time                    # 时间
        self.image = image                  # 需求图片


        # # 控制人数
        # self.max_places = max_places        # 最大人数，包含需求所有者自己，所以缺省值为“2”
        # self.current_places = current_places    # 当前人数，包含需求者自己，所以缺省值为“1”

        # 状态
        self.if_disabled = if_disabled      # 表示是否挂起（True表示挂起）
        #
        # # 申请该需求的列表
        # self.request_n = request_n          # 申请总数
        # # 这里的request_list应是一个Request类型的数组
        # if request_list:
        #     self.request_list = request_list    # 使用传入的数组（list）
        # else:
        #     self.request_list = []          # 创建空数组（list）
