import os
import time
import keyboard
import platform
import psutil
from src.ui.console import ConsoleUI
from src.system.commands import SystemCommands
from src.utils.logger import logger


class BIOS:
    """增强型BIOS系统引导程序"""
    
    def __init__(self):
        self.version = "V1.9"
        self.author = "huluobuo"
        self.ui = ConsoleUI()
        self.boot_devices = ["Hard Drive", "USB Drive", "CD-ROM", "Network"]
        self.selected_boot_device = 0
        self.ram_size = self._get_ram_size()
        self.cpu_info = self._get_cpu_info()
    
    def _get_ram_size(self):
        """获取系统内存大小"""
        try:
            return f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
        except Exception:
            return "Unknown"
    
    def _get_cpu_info(self):
        """获取CPU信息"""
        try:
            return f"{platform.processor()} ({psutil.cpu_count(logical=False)}C/{psutil.cpu_count(logical=True)}T)"
        except Exception:
            return "Unknown"
    
    def load_system(self):
        """加载操作系统"""
        logger.info("从BIOS加载操作系统")
        print("\n正在加载操作系统...")
        print("初始化系统内核...")
        time.sleep(0.5)
        print("加载系统服务...")
        time.sleep(0.5)
        print("启动用户界面...")
        time.sleep(0.5)
        
        system_commands = SystemCommands()
        self.ui.show_desktop(system_commands)
    
    def show_bios_menu(self):
        """显示BIOS主菜单"""
        while True:
            self.ui.clear_screen()
            print('+--------------------------------------------------+')
            print('|                   BIOS SETUP                    |')
            print('+--------------------------------------------------+')
            print('| 1. 系统信息                                      |')
            print('| 2. 启动设备顺序                                  |')
            print('| 3. 系统配置                                      |')
            print('| 4. 保存并退出                                    |')
            print('| 5. 直接启动系统                                  |')
            print('+--------------------------------------------------+')
            
            try:
                choice = input('请输入选择 (1-5): ').strip()
                
                if choice == '1':
                    self.show_system_info()
                elif choice == '2':
                    self.show_boot_order()
                elif choice == '3':
                    self.show_system_config()
                elif choice == '4':
                    print('保存配置...')
                    time.sleep(0.5)
                    print('退出BIOS...')
                    time.sleep(0.5)
                    return
                elif choice == '5':
                    self.load_system()
                    return
                else:
                    print('无效选择，请重新输入。')
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                return
    
    def show_system_info(self):
        """显示系统信息"""
        self.ui.clear_screen()
        print('+--------------------------------------------------+')
        print('|                   系统信息                       |')
        print('+--------------------------------------------------+')
        print(f'| BIOS版本：        {self.version:<25} |')
        print(f'| 作者：            {self.author:<25} |')
        print(f'| CPU：             {self.cpu_info:<25} |')
        print(f'| 内存：            {self.ram_size:<25} |')
        print(f'| 系统类型：        {platform.system()} {platform.architecture()[0]:<17} |')
        print(f'| 日期：            {time.strftime("%Y-%m-%d %H:%M:%S"):<25} |')
        print('+--------------------------------------------------+')
        input('按回车键返回...')
    
    def show_boot_order(self):
        """显示启动设备顺序"""
        self.ui.clear_screen()
        print('+--------------------------------------------------+')
        print('|                   启动设备顺序                   |')
        print('+--------------------------------------------------+')
        
        for i, device in enumerate(self.boot_devices):
            marker = "=> " if i == self.selected_boot_device else "   "
            print(f'| {marker}{i+1}. {device:<34} |')
        
        print('+--------------------------------------------------+')
        print('| 使用 ↑/↓ 键选择设备，Enter键确认，Esc键返回      |')
        print('+--------------------------------------------------+')
        
        # 简单的按键处理
        input('按回车键返回...')
    
    def show_system_config(self):
        """显示系统配置"""
        self.ui.clear_screen()
        print('+--------------------------------------------------+')
        print('|                   系统配置                       |')
        print('+--------------------------------------------------+')
        print('| 1. 启动超时：     3秒                           |')
        print('| 2. 键盘模式：     Enhanced                      |')
        print('| 3. 安全启动：     Disabled                      |')
        print('| 4. UEFI模式：     Enabled                       |')
        print('+--------------------------------------------------+')
        input('按回车键返回...')
    
    def show_splash_screen(self):
        """显示启动画面"""
        self.ui.clear_screen()
        print('+--------------------------------------------------+')
        print('|                                                  |')
        print('|                  My OS 系统                       |')
        print('|                                                  |')
        print(f'|           BIOS Version: {self.version}               |')
        print('|                                                  |')
        print('|                                                  |')
        print('|            Press DEL to enter BIOS               |')
        print('|                                                  |')
        print('+--------------------------------------------------+')
        print('检测硬件...')
        time.sleep(0.5)
        print('初始化内存...')
        time.sleep(0.5)
        print('检测启动设备...')
        time.sleep(0.5)
    
    def main_boot_sequence(self):
        """增强型主引导序列"""
        logger.info("启动BIOS引导序列")
        
        # 显示启动画面
        self.show_splash_screen()
        
        # 引导倒计时
        self.ui.clear_screen()
        print('+--------------------------------------------------+')
        print('|                  My OS 系统                       |')
        print('+--------------------------------------------------+')
        print('|                                                  |')
        print('|            Press DEL to enter BIOS               |')
        print('|            Loading OS in: 3 seconds              |')
        print('|                                                  |')
        print('+--------------------------------------------------+')
        
        start_time = time.time()
        boot_timeout = 3
        
        while True:
            elapsed = time.time() - start_time
            remaining = max(0, int(boot_timeout - elapsed))
            
            # 更新倒计时
            print(f'\r加载操作系统中... {remaining}秒', end='')
            
            # 检查按键
            if keyboard.is_pressed('delete') or keyboard.is_pressed('del'):
                logger.info("用户进入BIOS设置")
                self.show_bios_menu()
                break
            
            # 超时，加载系统
            if elapsed >= boot_timeout:
                self.load_system()
                break
            
            time.sleep(0.1)
        
        logger.info("BIOS引导序列完成")