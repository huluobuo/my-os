# 初始化的玩意
import os
import time


# 开机动画
os.system("start .\\os\\startup\\start-hello.py" if os.name == "nt" else "python ./os/startup/start-hello.py")
os.system("start .\\os\\startup\\startup.py" if os.name == "nt" else "python ./os/startup/startup.py")
try:
    with open("./os/mos/systemstartwaittime.mos", "r") as f:
        waittime = int(f.read())
except:
    waittime = 3

time.sleep(waittime)

with open("./os/mos/systemisready.mos", "w") as f:
    f.write("True")