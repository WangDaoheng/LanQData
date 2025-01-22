
-- CREATE TABLE lanq.scan_json_data (
--     id INT AUTO_INCREMENT PRIMARY KEY,              -- 自增主键
--     file_path VARCHAR(512) NOT NULL UNIQUE,         -- 文件路径（唯一）
--     scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 扫描时间
--     device_id VARCHAR(36),                          -- 设备 ID（特定标识）
--     file_name VARCHAR(255)                          -- 文件名
-- );


CREATE TABLE scan_json_data (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- 自增主键
    file_path VARCHAR(512) NOT NULL,         -- 文件路径
    sub_dir VARCHAR(50),                     -- 二级目录名（如 daily_summary）
    date_dir DATE,                           -- 三级目录名（如 2025-01-21）
    device_id VARCHAR(36),                   -- 设备 ID（四级目录名）
    file_name VARCHAR(255),                  -- 文件名
    scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 扫描时间
);
-- 添加唯一约束，确保 (sub_dir, date_dir, device_id, file_name) 组合唯一
ALTER TABLE scan_json_data
ADD CONSTRAINT unique_file_record UNIQUE (sub_dir, date_dir, device_id, file_name);



CREATE TABLE lanq.processed_json_data (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- 自增主键
    file_path VARCHAR(512) NOT NULL UNIQUE,  -- 文件路径（唯一）
    file_name VARCHAR(255),                  -- 文件名
    device_id VARCHAR(36),                   -- 设备 ID（特定标识）
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 处理时间
);









