import os
import time
import logging
from datetime import datetime
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
        # 动态获取项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在目录
        project_root = os.path.dirname(current_dir)  # 项目根目录
        # 构建 JSONExample/demo 目录的路径
        self.root_dir = os.path.join(project_root, "JSONExample", "demo")

        # 二级目录列表
        self.sub_dirs = ["daily_summary", "near_real_time", "notification_message", "sle_bioage"]

        # 上次打印监控日志的时间
        self.last_monitor_log_time = time.time()

        # 上次发现新文件的时间
        self.last_new_file_time = None

    def scan_directory(self):
        """扫描目录并记录 JSON 文件信息"""
        while True:
            try:
                # 获取数据库连接
                conn = db_pool.get_connection()
                cursor = conn.cursor()

                # 遍历二级目录
                new_files_found = False  # 标记是否发现新文件
                for sub_dir in self.sub_dirs:
                    sub_dir_path = os.path.join(self.root_dir, sub_dir)
                    if not os.path.exists(sub_dir_path):
                        logging.warning(f"Sub directory not found: {sub_dir_path}")
                        continue

                    # 遍历三级目录（日期目录）
                    for date_dir in os.listdir(sub_dir_path):
                        date_dir_path = os.path.join(sub_dir_path, date_dir)
                        if not os.path.isdir(date_dir_path):
                            continue

                        # 遍历四级目录（device_id 目录）
                        for device_id in os.listdir(date_dir_path):
                            device_dir_path = os.path.join(date_dir_path, device_id)
                            if not os.path.isdir(device_dir_path):
                                continue

                            # 遍历 JSON 文件
                            for filename in os.listdir(device_dir_path):
                                if filename.startswith("file_") and filename.endswith(".json"):
                                    file_path = os.path.join(device_dir_path, filename)

                                    # 检查文件是否已记录
                                    cursor.execute(
                                        """
                                        SELECT id FROM scan_json_data 
                                        WHERE sub_dir = %s AND date_dir = %s AND device_id = %s AND file_name = %s
                                        """,
                                        (sub_dir, date_dir, device_id, filename)
                                    )
                                    if not cursor.fetchone():
                                        # 插入新记录
                                        cursor.execute(
                                            """
                                            INSERT INTO scan_json_data 
                                            (file_path, sub_dir, date_dir, device_id, file_name) 
                                            VALUES (%s, %s, %s, %s, %s)
                                            """,
                                            (file_path, sub_dir, date_dir, device_id, filename)
                                        )
                                        conn.commit()
                                        logging.info(f"Scanned new file: {file_path}")
                                        new_files_found = True  # 标记发现新文件
                                        self.last_new_file_time = time.time()  # 更新上次发现新文件的时间

                # 关闭数据库连接
                cursor.close()
                conn.close()

                # 如果没有发现新文件，并且距离上次打印监控日志已经超过 5 分钟
                current_time = time.time()
                if not new_files_found and current_time - self.last_monitor_log_time >= 30:  # 300 秒 = 5 分钟
                    # 计算时间区间
                    start_time = datetime.fromtimestamp(self.last_monitor_log_time).strftime("%Y-%m-%d %H:%M:%S")
                    end_time = datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S")
                    logging.info(f"正在持续监控中，{start_time} - {end_time} 之间无新文件...........")
                    self.last_monitor_log_time = current_time  # 更新上次打印监控日志的时间

                # 等待一段时间后再次扫描
                time.sleep(10)
            except Error as e:
                logging.error(f"Database error: {e}")
            except Exception as e:
                logging.error(f"Error in scan_directory: {e}")
                time.sleep(10)  # 避免频繁报错

    def setup(self):
        """启动扫描"""
        self.scan_directory()


if __name__ == "__main__":
    scan_json = Scan_JSON()
    scan_json.setup()