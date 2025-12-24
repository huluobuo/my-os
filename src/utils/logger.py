import os
import logging
from datetime import datetime


class SystemLogger:
    """系统日志记录器"""
    
    def __init__(self, log_dir="./logs", log_level=logging.INFO):
        # 确保日志目录存在
        os.makedirs(log_dir, exist_ok=True)
        
        # 设置日志文件名
        log_file = os.path.join(log_dir, f"system_{datetime.now().strftime('%Y%m%d')}.log")
        
        # 配置日志
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('MyOS')
    
    def info(self, message):
        """记录信息日志"""
        self.logger.info(message)
    
    def warning(self, message):
        """记录警告日志"""
        self.logger.warning(message)
    
    def error(self, message):
        """记录错误日志"""
        self.logger.error(message)
    
    def debug(self, message):
        """记录调试日志"""
        self.logger.debug(message)


# 全局日志实例
logger = SystemLogger()