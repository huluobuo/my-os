import os

print("欢迎使用OS\n\t请确保你的电脑有至少100MB的空余内存")
print("Checking the third-party software...")
os.system("python -m pip install -r requirements.txt")
os.system("start .\\os\\startup\\start-run.py" if os.name == "nt" else "python ./os/startup/start-run.py")