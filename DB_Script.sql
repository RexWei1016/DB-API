-- 使用者基本資訊表
CREATE TABLE AppUser (
    ID VARCHAR(50) PRIMARY KEY,      -- 使用者帳號 (主鍵)
    pwd VARCHAR(50) NOT NULL,        -- 使用者密碼
    birth DATE,                      -- 出生年月日
    Sex VARCHAR(10),                 -- 性別
    name VARCHAR(100),               -- 英文姓名
    cname VARCHAR(100),              -- 中文姓名
    use VARCHAR(50),                 -- 用途
    number VARCHAR(50)               -- 編號
);

-- 使用者聯絡電話表，允許一個使用者有多個電話
CREATE TABLE UserPhone (
    phone_id SERIAL PRIMARY KEY,     -- 電話編號 (自增主鍵)
    ID VARCHAR(50) REFERENCES User(ID), -- 使用者帳號，外鍵參照 User 表
    phone VARCHAR(20) NOT NULL,      -- 聯絡電話
    phone_type VARCHAR(20)           -- 電話類型 (例如：家庭、行動、辦公室)
);

-- 教練基本資訊表
CREATE TABLE Coach (
    cID SERIAL PRIMARY KEY,          -- 教練編號 (自增主鍵)
    pwd VARCHAR(50) NOT NULL,        -- 教練密碼
    onboarding DATE,                 -- 入職時間
    exp TEXT                         -- 個人專長
);

-- 諮詢記錄表，連接教練和使用者的諮詢紀錄
CREATE TABLE Consultation (
    cID INT REFERENCES Coach(cID),   -- 教練編號，外鍵參照 Coach 表
    ID VARCHAR(50) REFERENCES User(ID), -- 使用者帳號，外鍵參照 User 表
    con_time TIMESTAMP NOT NULL,     -- 諮詢日期和時間
    content TEXT,                    -- 評估內容
    PRIMARY KEY (cID, ID, con_time)  -- 複合主鍵 (cID, ID, con_time) 確保唯一性
);

-- 使用者日常監控紀錄表
CREATE TABLE DailyMonitor (
    m_date DATE NOT NULL,            -- 記錄日期
    ID VARCHAR(50) REFERENCES User(ID), -- 使用者帳號，外鍵參照 User 表
    weight DECIMAL(5, 2),            -- 體重 (公斤)
    height DECIMAL(5, 2),            -- 身高 (公分)
    b_pressure VARCHAR(20),          -- 血壓
    sleep_dt DATE,                   -- 睡眠日期
    sleep_duration INTERVAL,         -- 睡眠時長
    sleep_quality VARCHAR(20),       -- 睡眠品質
    PRIMARY KEY (m_date, ID)         -- 複合主鍵 (m_date, ID)
);

-- 使用者運動記錄表
CREATE TABLE ExerciseRecord (
    exe_date DATE NOT NULL,          -- 運動日期
    ID VARCHAR(50) REFERENCES User(ID), -- 使用者帳號，外鍵參照 User 表
    exe_type VARCHAR(100),           -- 運動類型
    calories DECIMAL(8, 2),          -- 消耗卡路里
    PRIMARY KEY (exe_date, ID)       -- 複合主鍵 (exe_date, ID)
);

-- 食物資訊表
CREATE TABLE Food (
    fID SERIAL PRIMARY KEY,          -- 食物編號 (自增主鍵)
    food_type VARCHAR(100),          -- 食物類型
    food_calories DECIMAL(8, 2)      -- 食物所含卡路里
);

-- 使用者飲食記錄表
CREATE TABLE FoodRecord (
    eat_date DATE NOT NULL,          -- 記錄日期
    ID VARCHAR(50) REFERENCES User(ID), -- 使用者帳號，外鍵參照 User 表
    fID INT REFERENCES Food(fID),    -- 食物編號，外鍵參照 Food 表
    food_num INT,                    -- 食物份量
    calories DECIMAL(8, 2),          -- 總卡路里
    PRIMARY KEY (eat_date, ID, fID)  -- 複合主鍵 (eat_date, ID, fID)
);
