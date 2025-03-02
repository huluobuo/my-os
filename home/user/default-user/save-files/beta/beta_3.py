import os
import datetime
import keyboard
import time
from art import text2art


class Bios():  # 想不出这么写~~~
    """BIOS"""
    def load_system(self):
            print('正在启动系统核心程序········',  end='')
            system = System_commands()
            print('done\n正在启动用户界面········',  end='')
            show = Show(system)
            print('done\n开启用户端界面········')
            time.sleep(0.5)
            show.desktop()
        
    def load_bios(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('+--------------------------------------------------+')
        print('|                     OS 信息                      |')
        print('| 版本：V1.7(beta)                                 |')
        print('| 作者：huluobuo                                   |')
        print('| 版权所有 (C)  huluobuo 保留所有权利。            |')
        print('+--------------------------------------------------+')
        input('按回车键退出...')
        exit()
    
    def main_show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('按下Delete键进入BIOS，不操作3秒后进入系统')
        print('当前剩余时间： 3', end='\r')
        time.sleep(0.5)
        start_time = time.time()  # 用于计算时间
        while True:
            if keyboard.is_pressed('delete'):
                self.load_bios()
            elif time.time() - start_time >= 3:
                self.load_system()
            print(f'当前剩余时间： {int(3 - (time.time() - start_time))}', end='\r')


class Functions():
    def __init__(self):
        """没用的玩意"""
        pass

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def get(self):   # 默认获取时间 
        """
        获取XXX
        维修完毕！！！！！！！
        """
        print(
"""
当前支持的可以获取的信息：
\t\t时间 --- time
"""
        )
        get_thing_name = input('请输入要获取的信息：')
        if get_thing_name == 'time':
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print('获取失败，请检查输入是否正确')

class System_commands():
    def __init__(self):
        self.f = Functions()
        self.where = os.getcwd()
        self.commands = {
            'ls': self.ls,
            'cd': self.cd,
            'mkdir': self.mkdir,
            'rmdir': self.rmdir,
            'touch': self.touch,
            'rm': self.rm,
            'cat': self.cat,
            "get": self.f.get,
            'run': self.run,
            'new_run': self.new_run,
            'old_run': self.old_run,
            'exit': self.exit

        }
    

    def ls(self):
        # 列出当前目录下files文件夹中的文件
        files = os.listdir(self.where)
        print(f'{self.where}下的文件有：')
        for file in files:
            print('\t' + file)

    def cd(self):
        # 切换当前目录
        change_path = input('请输入要切换的目录：')
        try:
            if os.name == 'nt' and ':\\' in change_path:     # 检测是否为完整路径·····Linux和MacOS暂不支持
                os.chdir(change_path)
                print('目录已切换')
            else:
                self.where = self.where + '/' + change_path
                print('目录已切换')
        except Exception as e:
            print(f'发生未知错误，错误代码：{e}')
    
    def mkdir(self):
        # 创建文件夹
        folder_name = input('请输入要创建的文件夹名：')
        try:
            if os.name == 'nt' and ':\\' in folder_name:
                os.mkdir(folder_name)
                print('文件夹已创建')
            else:
                os.mkdir(self.where + '/' + folder_name)
                print('文件夹已创建')
        except Exception as e:
            print(f'发生未知错误，错误代码：{e}')

    def rmdir(self):
        # 删除文件夹
        folder_name = input('请输入要删除的文件夹名：')
        try:
            if os.name == 'nt' and ':\\' in folder_name:
                os.rmdir(folder_name)
                print('文件夹已删除')
            else:
                os.rmdir(self.where + '/' + folder_name)
                print('文件夹已删除')
        except Exception as e:
            print(f'发生未知错误，错误代码：{e}')
    
    def touch(self):
        # 创建文件
        file_name = input('请输入要创建的文件名：')
        try:
            if os.name == 'nt' and ':\\' in file_name:
                with open(file_name, 'a', encoding='UTF-8') as f:           # 尽量不要是 "w" 模式，否则会清空文件
                    f.write('')
                    print('文件已创建')
            else:
                with open(self.where + '/' + file_name, 'a', encoding='UTF-8') as f:
                    f.write('')
                    print('文件已创建')
        except Exception as e:
            print(f'发生未知错误，错误代码：{e}')
    
    def rm(self):
        # 删除文件
        file_name = input('请输入要删除的文件名：')
        try:
            if os.name == 'nt' and ':\\' in file_name:
                os.remove(file_name)
                print('文件已删除')
            else:
                os.remove(self.where + '/' + file_name)
                print('文件已删除')
        except FileNotFoundError:
            print(f'错误！文件不存在，请检查文件名是否正确')
        except Exception as e:
            print(f'发生未知错误，错误代码：{e}')

    def cat(self):
        # 查看文件内容
        file_name = input('请输入要查看的文件名：')
        try:
            if os.name == 'nt' and ':\\' in file_name:
                with open(file_name, 'r', encoding='UTF-8') as f:
                    print(f.read())
            else:
                with open(self.where + '/' + file_name, 'r', encoding='UTF-8') as f:
                    print(f.read())
        except FileNotFoundError:
            print(f'错误！文件不存在，请检查文件名是否正确')
        except Exception as e:
                print(f'发生未知错误，错误代码：{e}')
    
    
    def run(self):
        # 在终端运行命令
        run_command = input('请输入要运行的命令：')
        return_num = os.system(run_command)
        print(f'运行结束，终止代码为：{return_num}')
    
    def new_run(self):
        os.system('python .\\home\\user\\default-user\\save-files\\beta\\start.py' if os.name == 'nt' else 'python3 ./home/user/default-user/save-files/beta/start.py')  # 我就写一下，能不能运行，取决于你

    def old_run(self):
        os.system('python .\\home\\user\\default-user\\save-files\\old-ui\\start.py' if os.name == 'nt' else 'python3 ./home/user/default-user/save-files/old-ui/start.py')  # 我就写一下，能不能运行，取决于你
    def exit(self):
        # 退出程序
        os.system('cls')
        print(text2art("Thanks for using", font='small'))
        exit(0)


class Show():
    """UI"""
    def __init__(self, system):
        self.system = system
        self.choosing = 0  # 当前所选功能
        self.show_start = False

    def run_command(self):
        """运行对应命令"""
        #a = input()   # 说实话，Keyboard 让人头疼~
        os.system('cls')
        self.system.commands[list(self.system.commands.keys())[self.choosing]]()
        time.sleep(1)
        print('\n按回车键继续...', end='')
        a = input()
        time.sleep(0.3)
        self.desktop()


    def update_ui(self):
        """刷新界面，显示当前所选功能，在按下左右按键时执行"""
        time.sleep(0.1)
        os.system('cls')
        self.desktop()


    def desktop(self):
        """主界面"""
        os.system('cls')
        print_text = (f"""
                                             __  __           ___   ____
                                            |  \/  | _   _   / _ \ / ___|
                                            | |\/| || | | | | | | |\___ \\
                                            | |  | || |_| | | |_| | ___) |
                                            |_|  |_| \__, |  \___/ |____/
                                                     |___/

                    - 当前位置： {self.system.where}
                    - 当前版本： V1.7(beta)
        """)
        
        # 获取所有命令并格式化显示
        print_text += "\n"
        commands = ["查看所有文件", "切换目录", "创建文件夹", "删除文件夹 ", "创建文件", "删除文件", "查看文件内容", "获取信息", "运行命令", "新式终端", "老式终端"]
        for i, command in enumerate(commands):
            if i == self.choosing:
                print_text += f"> {command.ljust(15)}  |"
            else:
                print_text += f"  {command.ljust(15)}  |"
            if (i + 1) % 5 == 0:
                print_text += '\n'
        print_text += "\n\n使用左右箭头键切换选项，按回车键执行。按 Q 退出。"
        if not self.show_start:
            for pt in print_text:  # 是不是很6？
                print(pt, end='', flush=True)
                time.sleep(0.01)
            self.show_start = True
        else:
            print(print_text, end='')
        
        # 捕获键盘输入以切换选项或执行命令
        while True:
            try:
                if keyboard.is_pressed('right'):
                    self.choosing = (self.choosing + 1) % len(commands)  # 切换到下一个选项，在到头时回到第一个选项
                    self.update_ui()
                    break
                elif keyboard.is_pressed('left'):
                    self.choosing = (self.choosing - 1) % len(commands)
                    self.update_ui()
                    break
                elif keyboard.is_pressed('up'):
                    self.choosing = (self.choosing - 5) % len(commands)
                    self.update_ui()
                    break
                elif keyboard.is_pressed('down'):
                    self.choosing = (self.choosing + 5) % len(commands)
                    self.update_ui()
                    break
                elif keyboard.is_pressed('enter'):
                    a = input()
                    self.run_command()
                    break
                elif keyboard.is_pressed('q'):
                    self.system.commands['exit']()
                    break
            except KeyboardInterrupt:
                self.system.commands['exit']()
                break
            except Exception as e:
                print(f"发生错误：{e}")
                break # 以防万一


def main():
    os = Bios()
    os.main_show()
    

if __name__ == '__main__':
    main()