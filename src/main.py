#!/usr/bin/env python3
"""
My OS - 基于Python的操作系统模拟器
主程序入口
"""

import os
import sys
import subprocess
import traceback

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.core.bios import BIOS
from src.auth.user_manager import UserManager
from src.ui.login import LoginManager
from src.ui.console import ConsoleUI
from src.utils.logger import logger
from src.utils.exceptions import OSException


def check_dependencies():
    """检查并安装依赖"""
    logger.info("正在检查第三方软件...")
    try:
        requirements_path = os.path.join(project_root, "requirements.txt")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        logger.info("依赖安装成功！")
    except subprocess.CalledProcessError as e:
        logger.error(f"依赖安装失败: {e}")
        sys.exit(1)


def main():
    """主程序入口"""
    try:
        logger.info("启动My OS系统")
        print("欢迎使用My OS")
        print("请确保你的电脑有至少100MB的空余内存")
        
        # 检查依赖
        check_dependencies()
        
        # 初始化组件
        ui = ConsoleUI()
        user_manager = UserManager()
        login_manager = LoginManager(user_manager)
        
        # 加载用户数据
        user_manager.load_users()
        
        # 显示启动横幅
        ui.show_banner()
        
        # 用户登录
        if not login_manager.show_login_screen(ui):
            logger.warning("用户登录失败，程序退出")
            print("登录失败，程序退出。")
            return
        
        logger.info(f"用户 {login_manager.get_current_user()} 登录成功")
        
        # 启动BIOS引导
        bios = BIOS()
        bios.main_boot_sequence()
        
    except KeyboardInterrupt:
        logger.info("用户中断程序执行")
        print("\n程序已退出")
    except OSException as e:
        logger.error(f"系统异常: {e}")
        print(f"系统错误: {e}")
    except Exception as e:
        logger.error(f"未预期的错误: {e}")
        logger.debug(traceback.format_exc())
        print(f"发生未预期的错误: {e}")
        print("详细信息请查看日志文件")
    finally:
        logger.info("My OS系统关闭")


if __name__ == "__main__":
    main()