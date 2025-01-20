
CREATE TABLE scan_json_data (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- 自增主键
    file_path VARCHAR(512) NOT NULL UNIQUE,  -- 文件路径（唯一）
    scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 扫描时间
    device_id VARCHAR(36),                   -- 设备 ID（特定标识）
    file_name VARCHAR(255)                   -- 文件名
);


CREATE TABLE processed_json_data (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- 自增主键
    file_path VARCHAR(512) NOT NULL UNIQUE,  -- 文件路径（唯一）
    file_name VARCHAR(255),                  -- 文件名
    device_id VARCHAR(36),                   -- 设备 ID（特定标识）
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 处理时间
);









