from cryptography.fernet import Fernet

def generate_key():
    """生成并保存密钥"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("密钥已生成并保存为 secret.key")

def load_key(key_path):
    """加载保存的密钥"""
    return open(key_path, "rb").read()

def encrypt_file(file_name, key_path):
    """加密文件"""
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"文件 {file_name} 已加密")

def decrypt_file(file_name, key_path):
    """解密文件"""
    key = load_key(key_path)
    fernet = Fernet(key)

    with open(file_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"文件 {file_name} 已解密")

def main():
    print("请选择操作模式：")
    print("1. 生成密钥")
    print("2. 加密文件")
    print("3. 解密文件")
    choice = input("输入选项 (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice in ["2", "3"]:
        file_name = input("请输入文件: ")
        key_path = input("请输入密钥文件: ")

        if choice == "2":
            encrypt_file(file_name, key_path)
        elif choice == "3":
            decrypt_file(file_name, key_path)
    else:
        print("无效选项，请重试。")

if __name__ == "__main__":
    main()