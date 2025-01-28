import time
import os
import json
import sys

sys.path.append("./home/program-files/key-helper")
from key_helper import decrypt_file, encrypt_file  # type: ignore # 这么麻烦！！！




class Steer():
    """
        进行用户引导
    """

    def __init__(self) -> None:
        self.user_name = []
        self.user_path = []
        self.user_password = []
        self.system_key = "./os/mos/systemkey.key"


    def load_users_information(self) -> None:
        """
            加载用户信息
        """
        
        # 获取用户信息
        with open("./home/user/userlist.json", "r") as f:
            user_list = json.load(f)       # 出错就出错吧
        
        for user_name in user_list:
            self.user_name.append(user_name)
            self.user_path.append(user_list[user_name][0])
            decrypt_file(user_list[user_name][1], self.system_key)
            with open(user_list[user_name][1], "r") as f:
                self.user_password.append(f.read())
            encrypt_file(user_list[user_name][1], self.system_key)
    
    def shower(self):
        self.load_users_information()
        os.system("title 登录")
        os.system("cls" if os.name == "nt" else "clear")
        os.system("color D1")
        os.system("mode con: cols=60 lines=15")
        print("+----------------------------------------------------------+")
        print("|                            登录                          |")
        print("|----------------------------------------------------------|")
        print("|                           用户列表                       |")
        number = 1
        for user_name in self.user_name:
            print("| " + str(number).ljust(3) + " | " + user_name.ljust(50) + " |")
            number += 1
        print("+----------------------------------------------------------+")
        login_flag = False
        while not login_flag:
            number = int(input("请输入用户序号：   "))
            password = input("请输入密码：       ")
            if number > len(self.user_name):
                print("用户序号错误，请重新输入。")
            elif number < 1:
                print("用户序号错误，请重新输入。")
            else:
                if self.user_password[number - 1] == password:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("登录成功，即将启动。")
                    login_flag = True
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("登录失败，请重新登录。")
        
        print("正在引导启动")
        os.system("cd " + self.user_path[number - 1])
        os.system(("start .\\home\\user\\" + self.user_name[number - 1] + "\\save-files\\start.py") if os.name == "nt" else "python3 " + "./home/user/" + self.user_name[number - 1] + "/save-files/start.py")

if __name__ == "__main__":
    steer = Steer()
    steer.shower()