"""
系统配置文件
"""

import os

# 系统基本信息
SYSTEM_NAME = "My OS"
SYSTEM_VERSION = "1.8"
SYSTEM_AUTHOR = "huluobuo"

# 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
HOME_DIR = os.path.join(BASE_DIR, "home")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 用户配置
DEFAULT_USER = "default"
DEFAULT_PASSWORD = "123456"

# 安全配置
ENCRYPTION_KEY_FILE = os.path.join(DATA_DIR, "system.key")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

# 系统配置
MAX_LOGIN_ATTEMPTS = 3
SESSION_TIMEOUT = 3600  # 1小时

# UI配置
CONSOLE_WIDTH = 80
CONSOLE_HEIGHT = 25
LOGIN_SCREEN_WIDTH = 60
LOGIN_SCREEN_HEIGHT = 15

# 确保目录存在
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(HOME_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)