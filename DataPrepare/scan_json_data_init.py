import os
import time
import logging
from mysql.connector import Error
from mysql.connector import pooling

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("scan.log"), logging.StreamHandler()],
)

# 数据库连接池配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "lanq",
    "pool_name": "scan_pool",
    "pool_size": 5
}

# 初始化数据库连接池
db_pool = pooling.MySQLConnectionPool(**db_config)



class Scan_JSON:

    def __init__(self):

        # root_directory = "/root/lanq"
        self.root_dir = r"F:\LifeQ\LifeDataProject\JSONExample"

    def get_device_id(self, file_path):
        """从文件路径中解析设备 ID"""
        parts = file_path.split(os.sep)
        for part in parts:
            if len(part) == 36 and "-" in part:  # UUID 格式
                return part
        return None

    def scan_directory(self):
        """扫描目录并记录 JSON 文件信息"""
        while True:
            try:
                # 获取数据库连接
                conn = db_pool.get_connection()
                cursor = conn.cursor()

                # 遍历目录
                for dirpath, dirnames, filenames in os.walk(self.root_dir):
                    for filename in filenames:
                        if filename.startswith("file_") and filename.endswith(".json"):
                            file_path = os.path.join(dirpath, filename)
                            device_id = self.get_device_id(file_path)

                            # 检查文件是否已记录
                            cursor.execute("SELECT file_path FROM scan_json_data WHERE file_path = %s", (file_path,))
                            if not cursor.fetchone():
                                # 插入新记录
                                cursor.execute(
                                    "INSERT INTO scan_json_data (file_path, device_id, file_name) VALUES (%s, %s, %s)",
                                    (file_path, device_id, filename)
                                )
                                conn.commit()
                                logging.info(f"Scanned new file: {file_path}")

                # 关闭数据库连接
                cursor.close()
                conn.close()

                # 等待一段时间后再次扫描
                time.sleep(10)
            except Error as e:
                logging.error(f"Database error: {e}")
            except Exception as e:
                logging.error(f"Error in scan_directory: {e}")
                time.sleep(10)  # 避免频繁报错


    def setup(self):
        self.scan_directory()



if __name__ == "__main__":
    scan_json = Scan_JSON()
    scan_json.setup()


















