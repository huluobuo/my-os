import os

print("欢迎使用OS")
print("Checking the third-party software...")
os.system("python -m pip install -r requirements.txt")
os.system("python .\\os\\startup\\start-run.py" if os.name == "nt" else "python ./os/startup/start-run.py")