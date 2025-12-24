import os
import json
from src.security.encryption import FileEncryption


class UserManager:
    """用户管理器"""
    
    def __init__(self, users_file_path=None, system_key_path=None):
        # 设置默认路径
        if users_file_path is None:
            users_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "users.json")
        if system_key_path is None:
            system_key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "system.key")
        
        self.users_file_path = users_file_path
        self.system_key_path = system_key_path
        self.encryption = FileEncryption()
        self.users = {}
        
        # 确保数据目录存在
        os.makedirs(os.path.dirname(users_file_path), exist_ok=True)
        os.makedirs(os.path.dirname(system_key_path), exist_ok=True)
    
    def load_users(self):
        """加载用户列表"""
        try:
            if os.path.exists(self.users_file_path):
                with open(self.users_file_path, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
            else:
                # 创建默认用户
                self.create_default_user()
        except Exception as e:
            print(f"加载用户列表失败: {e}")
            self.users = {}
    
    def create_default_user(self):
        """创建默认用户"""
        # 计算正确的用户主目录路径
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        home_directory = os.path.join(project_root, "home", "default")
        
        default_user = {
            "username": "default",
            "password": "123456",  # 默认密码
            "home_directory": home_directory,
            "permissions": ["read", "write", "execute"]
        }
        
        self.users["default"] = default_user
        self.save_users()
        
        # 创建用户主目录
        os.makedirs(home_directory, exist_ok=True)
    
    def save_users(self):
        """保存用户列表"""
        try:
            with open(self.users_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存用户列表失败: {e}")
    
    def authenticate_user(self, username, password):
        """用户认证"""
        if username in self.users:
            user = self.users[username]
            return user["password"] == password
        return False
    
    def get_user_home_directory(self, username):
        """获取用户主目录"""
        if username in self.users:
            return self.users[username]["home_directory"]
        return None
    
    def create_user(self, username, password, home_directory=None):
        """创建新用户"""
        if username in self.users:
            return False, "用户已存在"
        
        # 计算正确的用户主目录路径
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        if not home_directory:
            home_directory = os.path.join(project_root, "home", username)
        
        new_user = {
            "username": username,
            "password": password,
            "home_directory": home_directory,
            "permissions": ["read", "write", "execute"]
        }
        
        self.users[username] = new_user
        self.save_users()
        
        # 创建用户主目录
        os.makedirs(home_directory, exist_ok=True)
        
        return True, "用户创建成功"
    
    def delete_user(self, username):
        """删除用户"""
        if username not in self.users:
            return False, "用户不存在"
        
        if username == "default":
            return False, "不能删除默认用户"
        
        del self.users[username]
        self.save_users()
        
        return True, "用户删除成功"
    
    def list_users(self):
        """列出所有用户"""
        return list(self.users.keys())