import time
import os

def check():
    try:
        with open("./os/wsh/systemisready.wsh", "r") as f:
            if f.read() == "True":
                return True
            else:
                return False
    except FileNotFoundError:
        return False



def startup():
    """
    启动函数，用于显示Windows的启动动画。

    """

    os.system('mode con: cols=30 lines=15')

    windows_logo = """
      _______   _______
     |       | |       |
     |       | |       |
     |_______| |_______|
      _______   _______
     |       | |       |
     |       | |       |
     |_______| |_______|

    """

    os.system('cls' if os.name == 'nt' else 'clear')
    spinner = [
    """
             ***
            * 
             *
    """,
    """
             ***
                *
        
    """,
    """ 
               *
                *
               *
    """,
    """
         
            
              **
    """,
    """
          
           
             ***
    """,
    """

            *
             ***
    """,
    """
             *
            *
              **
    """,
    """
             **
            * 
             *
    """

    ]

    # 模拟加载过程
    run = True
    while run:
        for spin in spinner:
            print_text = windows_logo + "\n" + spin
            print(print_text, end="\r")
            time.sleep(0.1)
            if check():
                run = False
                break

if __name__ == "__main__":
    startup()
    os.system('mode con: cols=10 lines=1')
    os.system("cls" if os.name == "nt" else "clear")
    print("正在等待一个终端任务...")
    time.sleep(1) # 怎么这么快
    with open("./os/wsh/systemisready.wsh", "w") as f:         #为了下一次
        f.write("False")