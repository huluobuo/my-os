import os
import sys
import subprocess
import pkg_resources

def check_dependencies():
    print("正在检查第三方软件...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("依赖安装成功！")
    except subprocess.CalledProcessError as e:
        print(f"错误：依赖安装失败！\n{e}")
        sys.exit(1)

def start_application():
    os.system("python .\\os\\steer\\user\\main.py") if os.name == "nt" else os.system("python3 ./os/steer/user/main.py")

def main():
    print("欢迎使用OS\n\t请确保你的电脑有至少100MB的空余内存")
    check_dependencies()
    start_application()

if __name__ == "__main__":
    main()