import os
import datetime
import keyboard
import time
import art


class Bios():  # 想不出这么写~~~
    """BIOS"""
    def load_system(self):
        show = Show(System_commands())
        show.desktop()
        
    def load_bios(self):
        print('+--------------------------------------------------+')
        print('|                     OS 信息                      |')
        print('| 版本：V 1.8                                      |')
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
                os.system('cls' if os.name == 'nt' else 'clear')
                self.load_system()
            print(f'当前剩余时间： {int(3 - (time.time() - start_time))}', end='\r')


class System_commands():
    def __init__(self):
        self.where = os.getcwd()
        self.commands = {
            'ls': self.ls,
            'folder': self.folder,
            'file': self.file,
            'run': self.run,
            'clean': self.clean,
            'exit': self.exit,
            'get': self.get
        }

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def get(self):   # 默认获取时间 
        """
        获取XXX
        维修完毕！！！！！！！
        """
        print("""
                当前支持的可以获取的信息：
                \t\t时间 --- time
              """
        )
        get_thing_name = input('请输入要获取的信息：')
        if get_thing_name == 'time':
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print('\a获取失败，请检查输入是否正确')

    def ls(self):
        # 列出当前目录下files目录中的文件
        files = os.listdir(self.where)
        print(f'{self.where}下的文件有：')
        for file in files:
            print('\t' + file)
    
    def folder(self):
        # 目录操作
        while True:
            try:
                _class = int(input('1. 新建目录\n2. 删除目录\n3. 切换目录\n\n请输入操作（1/2/3）：'))
            except Exception as e:
                print(f'\a你的输入有误，错误代码：{e}，请重新输入！')
            else:
                if _class in [1, 2, 3]:
                    break
                else:
                    print('\a你的输入有误，请重新输入！')
        # 操作
        try:
            if _class == 1:  # 新建目录
                # 创建目录
                folder_name = input('请输入要创建的目录名：')
                try:
                    if os.name == 'nt' and ':\\' in folder_name:
                        # 检查目录是否存在
                        if os.path.exists(folder_name):
                            print('\a目录已存在')
                            pass
                        else:
                            os.mkdir(folder_name)
                            print('目录已创建')
                    else:
                        # 检查目录是否存在
                        if os.path.exists(self.where + '/' + folder_name):
                            print('\a目录已存在')
                            pass
                        else:
                            os.mkdir(self.where + '/' + folder_name)
                            print('目录已创建')
                except Exception as e:
                    print(f'\a发生未知错误，错误代码：{e}')
            elif _class == 2:  # 删除目录
                folder_name = input('请输入要删除的目录名：')
                if os.name == 'nt':
                    if not os.path.exists(folder_name):
                        print('\a目录不存在')
                        pass
                    else:
                        if input(f'\a确定要删除目录 {folder_name} 吗？(y/n): ') in ['y', 'Y']:
                            os.rmdir(folder_name)
                            print('目录已删除')
                else:
                    if not os.path.exists(self.where + '/' + folder_name):
                        print('\a目录不存在')
                        pass
                    else:
                        if input(f'\a确定要删除目录 {folder_name} 吗？(y/n): ') in ['y', 'Y']:
                            os.rmdir(self.where + '/' + folder_name)
                            print('目录已删除')
            else:    # 切换当前目录
                change_path = input('请输入要切换的目录：')
                if os.name == 'nt' and ':\\' in change_path:
                    os.chdir(change_path)
                    self.where = change_path  # 更新当前路径
                    print('目录已切换')
                else:
                    new_path = os.path.join(self.where, change_path)
                    if os.path.exists(new_path) and os.path.isdir(new_path):
                        os.chdir(new_path)
                        self.where = new_path
                        print('目录已切换')
                    else:
                        print('\a目录不存在或不是有效的目录')
        except EncodingWarning as e:
            print(f'\a发生未知错误：{e}')

    def file(self):
        # 修改或读取文件内容
        while True:
            try:
                _class = int(input('1. 清除所有文本并写入文本\n2. 在文件末尾插入文本\n3. 读取文件\n\n请输入操作（1/2/3）：'))
                _file = input('\n请输入文件名：')
            except Exception as e:
                print(f'\a你的输入有误，错误代码：{e}，请重新输入！')
            else:
                if _class in [1, 2, 3]:
                    break
                else:
                    print('\a你的输入有误，请重新输入！')
        # 操作
        try:
            if _class == 1:  # 清除并写入
                with open(_file, 'w', encoding='UTF-8') as f:
                    print('请输入文件内容，输入"#!!!#-sys-stop-input-#!!!#"以停止输入\n-----分界线-----')
                    write_list = []
                    line_number = 1  # 行数
                    running = True
                    while running:
                        input_text = input(f'| {str(line_number).ljust(5)} |')  # 这个够了吧~~~
                        if input_text == '#!!!#-sys-stop-input-#!!!#':
                            print('-----分界线-----')
                            running = False
                        else:
                            write_list.append(input_text + '\n')  # 之后就不需要了
                            line_number += 1
                    # 输入完毕，写入文件
                    line_number = 1
                    print('正在写入文本')
                    for write_text in write_list:
                        print(f'正在写入第| {str(line_number).ljust(5)} |行', end='\r')
                        f.write(write_text)
                        line_number += 1
                print('Done!')
            elif _class == 2:  # 在文件末尾插入
                with open(_file, 'r', encoding='UTF-8') as f:
                    print('文件内容：\n-----分界线-----')
                    line_number = 1
                    for read_text in f.read().split('\n'):
                        print(f'| {str(line_number).ljust(5)} |{read_text}')
                        line_number += 1
                    help_line_number = line_number
                    print('-----分界线-----')
                with open(_file, 'a', encoding='UTF-8') as f:  # 直接搬过来~~~~~~~~~~~~~~~~~~~
                    print('请输入文件内容，输入"#!!!#-sys-stop-input-#!!!#"以停止输入\n-----分界线-----')
                    write_list = []
                    running = True
                    while running:
                        input_text = input(f'| {str(line_number).ljust(5)} |')
                        if input_text == '#!!!#-sys-stop-input-#!!!#':
                            print('-----分界线-----')
                            running = False
                        else:
                            write_list.append(input_text + '\n')
                            line_number += 1
                    # 输入完毕，写入文件
                    line_number = help_line_number
                    print('正在写入文本')
                    for write_text in write_list:
                        print(f'正在写入第| {str(line_number).ljust(5)} |行', end='\r')
                        f.write(write_text)
                        line_number += 1
                print('Done!')
            else:
                with open(_file, 'r', encoding='UTF-8') as f:
                    print('文件内容：\n-----分界线-----')
                    line_number = 1
                    for read_text in f.read().split('\n'):
                        print(f'| {str(line_number).ljust(5)} |{read_text}')
                        line_number += 1
                    print('-----分界线-----')
                print('Done!')
        except FileNotFoundError:
            print('\a文件未找到')
        except EncodingWarning as e:
            print(f'\a发生未知错误：{e}')

    
    def run(self):
        # 在终端运行命令
        run_command = input('请输入要运行的命令：')
        return_num = os.system(run_command)
        print(f'运行结束，终止代码为：{return_num}')
    
    def clean(self):
        # 刷新系统
        os.system('cls' if os.name == 'nt' else 'clear')
        # 重新启动
        time.sleep(0.5)
        bios = Bios()
        bios.load_system()
    
    def exit(self):
        # 退出程序
        os.system('cls')
        print("\a" + art.text2art('Bye!'))
        time.sleep(3)
        exit(0)


class Show():
    """UI"""
    def __init__(self, system):
        self.system = system
        self.choosing = 0  # 当前所选功能
        self.show_start = False
        self.commands = ["文件列表", "目录操作", "文件编辑", "命令执行", "刷新系统"]

    def run_command(self):
        """运行对应命令"""
        os.system('cls')
        self.system.commands[list(self.system.commands.keys())[self.choosing]]()
        time.sleep(1)
        print('\n按回车键继续...', end='')
        input()
        time.sleep(0.3)
        self.show_desktop()

    def show_desktop(self):
        """显示主界面"""
        print_text = (f"""
                  当前位置： {self.system.where.ljust(30)}
                  当前版本： V 1.8
                    系统功能菜单：
                        """)
        
        # 获取所有命令并格式化显示
        print_text += "\n"
        # 修改菜单布局逻辑
        menu_items = []
        for i, command in enumerate(self.commands):
            item = f"-[{command}]-".center(20) if i == self.choosing else f" {command} ".center(20)
            menu_items.append(item)
        
        # 每行显示4个菜单项
        row_length = 4
        for i in range(0, len(menu_items), row_length):
            print_text += ' '.join(menu_items[i:i+row_length]) + '\n\n'
        
        print_text += "\n" + "="*80 + "\n"
        print_text += "操作说明:".center(80) + "\n"
        print_text += "← → ↑ ↓ : 切换选项   |   Enter : 执行   |   Q : 退出系统".center(80)
        print_text += "\n" + "="*80

        # 使用\033[H将光标移到开头,而不是清屏
        print('\033[H', end='')
        
        print(print_text, end='')

    def desktop(self):
        """主界面"""
        self.show_desktop()
        
        # 捕获键盘输入以切换选项或执行命令
        while True:
            try:
                if keyboard.is_pressed('right'):
                    self.choosing = (self.choosing + 1) % len(self.commands)
                    self.show_desktop()
                    time.sleep(0.1)
                elif keyboard.is_pressed('left'):
                    self.choosing = (self.choosing - 1) % len(self.commands)
                    self.show_desktop()
                    time.sleep(0.1)
                elif keyboard.is_pressed('up'):
                    self.choosing = (self.choosing - 4) % len(self.commands)
                    self.show_desktop()
                    time.sleep(0.1)
                elif keyboard.is_pressed('down'):
                    self.choosing = (self.choosing + 4) % len(self.commands)
                    self.show_desktop()
                    time.sleep(0.1)
                elif keyboard.is_pressed('enter'):
                    a = input()
                    self.run_command()
                    break
                elif keyboard.is_pressed('q'):
                    self.system.commands['exit']()
                    break
            except Exception as e:
                print(f"发生错误：{e}")
                exit()
def main():
    os = Bios()
    os.main_show()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        System_commands().exit()
    except Exception as e:
        print(f'\a发生未知错误，错误代码：{e}')
        exit()