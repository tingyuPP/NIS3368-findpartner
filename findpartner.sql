use findpartner;

-- 创建用户表
CREATE TABLE Users (
	-- 用户id
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    -- 用户名 
    user_name VARCHAR(100) UNIQUE,
    -- 用户昵称
    user_nickname VARCHAR(100),
    -- 用户密码
    user_psword VARCHAR(100),
    -- 用户信息
    user_sex INT,
    -- 用户喜好
    user_hobby VARCHAR(255),
    -- 用户头像url
    user_image TEXT,
    -- 用户签名
    user_introduction TEXT,
    -- 用户创建时间戳
    user_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建需求表
CREATE TABLE Notice (
	-- 需求id
    notice_id INT AUTO_INCREMENT PRIMARY KEY,
    -- 需求是由谁创建的
    user_id INT NOT NULL,
    -- 需求图片url
    notice_image VARCHAR(255),
    -- 需求类型 大类 
    -- 0-体育 1-学习 2-吃饭 3-游戏 4-出行
    notice_basic_type INT,
    -- 需求备注 小类
    notice_detail_type VARCHAR(255),
    -- 需求发布人联系方式
    notice_owner_contact TEXT,
    -- 需求主体执行时间
	notice_time TEXT,
    -- 需求主体执行地点
	notice_location TEXT,
    -- 需求描述
	notice_description TEXT,
    -- 名额
    notice_max_places INT,
    -- 当前名额 缺省为 2
    notice_current_places INT,
    -- 需求状态 1-挂起/..
	notice_if_disabled INT,
    -- 需求创建时间戳
    notice_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 创建申请表
CREATE TABLE Requests (
	-- 申请id
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    -- 申请人id
    user_id INT,
    -- 申请的需求id
    notice_id INT,
    -- 申请人联系方式
    request_contact TEXT,
    -- 申请状态 0-未知 1-通过 2-未通过
    answer_state INT NOT NULL,
    -- 申请时间戳
    request_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (notice_id) REFERENCES Notice(notice_id)
);

