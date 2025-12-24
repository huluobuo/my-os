from cryptography.fernet import Fernet
import os


class FileEncryption:
    """文件加密工具"""
    
    def __init__(self):
        self.key_cache = {}
    
    def generate_key(self, key_path="secret.key"):
        """生成并保存密钥"""
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        print(f"密钥已生成并保存为 {key_path}")
        return key
    
    def load_key(self, key_path):
        """加载密钥"""
        if key_path in self.key_cache:
            return self.key_cache[key_path]
        
        if not os.path.exists(key_path):
            raise FileNotFoundError(f"密钥文件不存在: {key_path}")
        
        key = open(key_path, "rb").read()
        self.key_cache[key_path] = key
        return key
    
    def encrypt_file(self, file_path, key_path):
        """加密文件"""
        try:
            key = self.load_key(key_path)
            fernet = Fernet(key)
            
            with open(file_path, "rb") as file:
                original_data = file.read()
            
            encrypted_data = fernet.encrypt(original_data)
            
            with open(file_path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            
            print(f"文件已加密: {file_path}")
            return True
        except Exception as e:
            print(f"加密文件失败: {e}")
            return False
    
    def decrypt_file(self, file_path, key_path):
        """解密文件"""
        try:
            key = self.load_key(key_path)
            fernet = Fernet(key)
            
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
            
            decrypted_data = fernet.decrypt(encrypted_data)
            
            with open(file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
            
            print(f"文件已解密: {file_path}")
            return True
        except Exception as e:
            print(f"解密文件失败: {e}")
            return False
    
    def encrypt_string(self, text, key_path):
        """加密字符串"""
        try:
            key = self.load_key(key_path)
            fernet = Fernet(key)
            encrypted_text = fernet.encrypt(text.encode())
            return encrypted_text
        except Exception as e:
            print(f"加密字符串失败: {e}")
            return None
    
    def decrypt_string(self, encrypted_text, key_path):
        """解密字符串"""
        try:
            key = self.load_key(key_path)
            fernet = Fernet(key)
            decrypted_text = fernet.decrypt(encrypted_text).decode()
            return decrypted_text
        except Exception as e:
            print(f"解密字符串失败: {e}")
            return None