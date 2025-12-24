import os
from src.auth.user_manager import UserManager


class LoginManager:
    """登录管理器"""
    
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.current_user = None
    
    def show_login_screen(self, ui):
        """显示登录界面"""
        while True:
            user_list = self.user_manager.list_users()
            ui.show_login_screen(user_list)
            
            try:
                user_choice = input("请输入用户序号: ").strip()
                if not user_choice:
                    continue
                
                user_index = int(user_choice) - 1
                
                if 0 <= user_index < len(user_list):
                    username = user_list[user_index]
                    password = input("请输入密码: ").strip()
                    
                    if self.user_manager.authenticate_user(username, password):
                        self.current_user = username
                        home_directory = self.user_manager.get_user_home_directory(username)
                        
                        if home_directory and os.path.exists(home_directory):
                            os.chdir(home_directory)
                        
                        ui.clear_screen()
                        print(f"登录成功，欢迎 {username}!")
                        return True
                    else:
                        print("密码错误，请重新登录。")
                else:
                    print("用户序号错误，请重新输入。")
            except ValueError:
                print("请输入有效的数字序号。")
            except KeyboardInterrupt:
                print("\n退出登录。")
                return False
            except Exception as e:
                print(f"登录过程中发生错误: {e}")
    
    def get_current_user(self):
        """获取当前登录用户"""
        return self.current_user