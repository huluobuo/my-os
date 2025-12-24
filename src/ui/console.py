import os
import datetime
import art


class ConsoleUI:
    """控制台用户界面"""
    
    def __init__(self):
        self.title = "OS Console"
    
    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def set_window_size(self, cols=80, lines=25):
        """设置窗口大小"""
        if os.name == 'nt':
            os.system(f'mode con: cols={cols} lines={lines}')
    
    def set_title(self, title):
        """设置窗口标题"""
        if os.name == 'nt':
            os.system(f'title {title}')
    
    def show_login_screen(self, user_list):
        """显示登录界面"""
        self.set_title("登录")
        self.set_window_size(60, 15)
        self.clear_screen()
        
        print("+----------------------------------------------------------+")
        print("|                            登录                          |")
        print("|----------------------------------------------------------|")
        print("|                           用户列表                       |")
        
        for i, user_name in enumerate(user_list, 1):
            print(f"| {str(i).ljust(3)} | {user_name.ljust(50)} |")
        
        print("+----------------------------------------------------------+")
    
    def show_desktop(self, system_commands):
        """显示桌面界面"""
        self.clear_screen()
        print("欢迎使用OS桌面系统")
        print("输入 'help' 查看可用命令")
        
        while True:
            try:
                command = input(f"{system_commands.current_directory} > ").strip()
                if command:
                    if command.lower() == 'exit':
                        break
                    system_commands.execute(command)
            except KeyboardInterrupt:
                print("\n再见!")
                break
            except Exception as e:
                print(f"错误: {e}")
    
    def show_banner(self):
        """显示启动横幅"""
        banner = art.text2art("My OS", font="small")
        print(banner)
        print("基于Python的操作系统模拟器")
        print("版本 1.8 | 作者: huluobuo")
        print("-" * 50)