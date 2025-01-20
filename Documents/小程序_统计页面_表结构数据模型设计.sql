

-------------  每日的生物年龄曲线   -------------------
CREATE TABLE dwd.dwd_BioAge_daily (
      cust_id              varchar(100)
     ,device_id            varchar(100)
     ,ymd                  DATE
     ,BioBoost             float
     ,BioAge               float
     ,sleepAge             float
     ,heartAge             float
     ,activityAge          float
     ,mentalAge            float
     ,fitnessAge           float
   ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd)
 );


-------------  睡眠主题表   -------------------
CREATE TABLE dwd.dwd_sleep_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            -- 2024-12-07  格式的日期
     ,sleepAge             float           --睡眠BioAge
     ,sleepBoost           float           --睡眠BioBoost
     ,lightSleep           float           --浅睡（秒）
     ,sleepTotalTime       float           --总睡眠时间（秒）
     ,sleepEyeTime         float           --快速眼动睡眠时间（秒）
     ,sleepEyeTarget       float           --快速眼动睡眠目标（秒）
     ,awakeTime            float           --清醒时间（秒）
     ,littleSleep          float           --小睡（秒）
     ,coreSleep            float           --核心睡眠时间(秒)
     ,beginDelaySleep      float           --睡眠开始延迟（秒）
     ,momentumSleep        float           --睡眠动量
     ,beginAwakeSleep      float           --睡眠开始后唤醒（秒）
     ,consistency          float           --昼夜节律一致性
     ,deepSleep            float           --深度睡眠（秒）
     ,disturb              float           --干扰(秒)
     ,periodSleep          float           --睡眠周期（秒）
     ,rest                 float           --休息（秒）
     ,recover              float           --睡眠恢复
     ,sleepLaw             float           --睡眠规律（秒）
     ,sleepEfficient       float           --睡眠效率
     ,quickEyeBeginSleep   float           --快速眼动起始潜伏期（秒）
   ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd)
 );



-------------  心率主题表   -------------------
CREATE TABLE dwd.dwd_heart_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            -- 2024-12-07  格式的日期
     ,hourTime             DATETIME        --日内时间
     ,heartAge             float           --心率BioAge
     ,heartBoost           float           --心率BioBoost
     ,restingHeart         float           --静息心率
     ,minHeart             float           --最低心率
     ,peakHeart            float           --峰值心率
     ,avgHeart             float           --平均心率
     ,SDNN                 float           --单位（毫秒）
     ,rMSSD                float           --单位（毫秒）
     ,LFHF                 float           --LF/HF
     ,heartStrength        float           --平均心肌力量
     ,totalBloodFlow       float           --总血流量
     ,stiffness            float           --平均大动脉僵硬度
   ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd, hourTime)
 );



-------------  活动主题表   -------------------
CREATE TABLE dwd.dwd_activity_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            --2024-12-07  格式的日期
     ,activityAge          float           --活动BioAge
     ,activityBoost        float           --活动BioBoost
     ,stepNum              float           --步数
     ,strengthMit          float           --强度分钟（秒）
     ,sitting              float           --久坐时间（秒）
     ,totalHeat            float           --总热量（千卡）
   ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd)
 );


-------------  健身主题表   -------------------
CREATE TABLE dwd.dwd_fitness_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            --2024-12-07  格式的日期
     ,fitnessAge           float           --健身BioAge
     ,fitnessBoost         float           --健身BioBoost
     ,totalTime            float           --总时长（秒）
     ,totalPeriod          float           --总时段
     ,totalHeat            float           --总健身热量（千卡）
   ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd)
 );



-------------  精神主题表   -------------------
CREATE TABLE dwd.dwd_mental_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            --2024-12-07  格式的日期
     ,hourTime             DATETIME        --日内时间
     ,mentalAge            float           --精神BioAge
     ,mentalBoost          float           --精神BioBoost
     ,pressureScore        float           --压力分（小时级别）
     ,pressureScoreDaily   float           --每日压力评分
     ,chronicStress        float           --慢性压力升高
     ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd, hourTime)
 );


-------------  设备主题表   -------------------
CREATE TABLE dwd.dwd_mental_daily (
      cust_id              varchar(100)    --客户id
     ,device_id            varchar(100)    --设备id
     ,ymd                  DATE            --2024-12-07  格式的日期
     ,activeTime           DATE            --设备时间
     ,UNIQUE KEY unique_industry_code (cust_id, device_id, ymd, hourTime)
 );









































