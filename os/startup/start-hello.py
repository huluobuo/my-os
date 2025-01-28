import os
import time


class Startup:
    """
        加载完后的欢迎界面
    """

    def __init__(self) -> None:
        """
            啥也不是
        """
        pass

    def check(self) -> bool:
        """
            检查是否准备就绪
        """
        try:
            with open("./os/wsh/systemisready.wsh", "r") as f:
                if f.read() == "True":
                    return True
                else:
                    return False
        except FileNotFoundError:
            return False
    
    def show(self) -> None:
        """
            显示欢迎界面
        """
        os.system("cls")
        os.system("mode con: cols=90 lines=25")
        print("+------------------------------------------------+")
        print("|                     Windows11                  |")
        print("|                  files checking...             |")
        print("|                              (C)huluobuo       |")
        print("+-----------------------------------------------+")

        print()
        print("Checking files ...")   # 打印当前文件夹中的所有文件
        for root, dirs, files in os.walk(".\\"):
            for file in files:
                print(root + "-" + file)
        
        print()
        print("Loading...  Done!")
    
    def startup(self) -> None:
        """
            启动
        """
        running = True
        while running:
            if self.check():
                self.show()
                running = False
            else:
                time.sleep(0.5)
                os.system("cls")

if __name__ == "__main__":
    startup = Startup()
    startup.startup()
    time.sleep(1)