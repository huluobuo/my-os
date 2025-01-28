# 初始化的玩意
import os
import time


# 开机动画
os.system("start .\\os\\startup\\start-hello.py" if os.name == "nt" else "python ./os/startup/start-hello.py")
os.system("start .\\os\\startup\\startup.py" if os.name == "nt" else "python ./os/startup/startup.py")
time.sleep(2)

with open("./os/wsh/systemisready.wsh", "w") as f:
    f.write("True")