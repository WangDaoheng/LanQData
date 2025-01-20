import os
import json
import time
import logging
from mysql.connector import Error
from mysql.connector import pooling

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("deal.log"), logging.StreamHandler()],
)

# 数据库连接池配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "file_monitor",
    "pool_name": "deal_pool",
    "pool_size": 5
}

# 初始化数据库连接池
db_pool = pooling.MySQLConnectionPool(**db_config)

def process_json_file(file_path):
    """处理 JSON 文件"""
    try:
        # 在这里实现你的 JSON 文件处理逻辑
        logging.info(f"Processing file: {file_path}")
        # 示例：打印文件内容
        with open(file_path, "r") as file:
            data = json.load(file)
            logging.info(f"File content: {data}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")

def deal_json_data():
    """处理未处理的 JSON 文件"""
    while True:
        try:
            # 获取数据库连接
            conn = db_pool.get_connection()
            cursor = conn.cursor()

            # 查找未处理的文件
            cursor.execute("""
                SELECT s.file_path, s.file_name, s.device_id 
                FROM scan_json_data s 
                LEFT JOIN processed_json_data p ON s.file_path = p.file_path 
                WHERE p.file_path IS NULL
            """)
            unprocessed_files = cursor.fetchall()

            # 处理未处理的文件
            for file_path, file_name, device_id in unprocessed_files:
                process_json_file(file_path)
                # 记录已处理的文件
                cursor.execute(
                    "INSERT INTO processed_json_data (file_path, file_name, device_id) VALUES (%s, %s, %s)",
                    (file_path, file_name, device_id)
                )
                conn.commit()
                logging.info(f"Processed file: {file_path}")

            # 关闭数据库连接
            cursor.close()
            conn.close()

            # 等待一段时间后再次检查
            time.sleep(10)
        except Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Error in deal_json_data: {e}")
            time.sleep(10)  # 避免频繁报错

if __name__ == "__main__":
    deal_json_data()