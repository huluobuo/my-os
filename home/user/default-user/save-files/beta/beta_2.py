import os
import datetime
import time

# 直接搬过来

class Functions():
    def __init__(self):
        """没用的玩意"""
        pass

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def get(self, args):   # 默认获取时间 
        """
        获取XXX
        维修完毕！！！！！！！
        """
        if args:
            if args[0] == 'time':
                print(self.get_time())
            else:
                print(f'[WARNG] {self.get_time()} 命令 "{args[0]}" 不存在')
        else:
            print(f'[WARNG] {self.get_time()} get 命令需要参数')

class System_commands():
    def __init__(self):
        functions = Functions()
        self.f = functions
        self.where = os.getcwd()
        self.commands = {
            'ls': self.ls,
            'cd': self.cd,
            'mkdir': self.mkdir,
            'rmdir': self.rmdir,
            'touch': self.touch,
            'rm': self.rm,
            'cat': self.cat,
            'echo': self.echo,
            'run': self.run,
            'exit': self.exit,
            'help': self.help,
            'get': functions.get
        }
    


    def where(self):
        return self.where

    def ls(self, args):
        # 列出当前目录下files文件夹中的文件
        files = os.listdir(self.where)
        print(f'{self.where}下的文件有：')
        for file in files:
            print('\t' + file)

    def cd(self, args):
        # 切换当前目录
        if args:
            self.where = args[0]
            # 分析当前系统
            if os.name == 'nt':
                os.system('cd ' + self.where + '\\' + args[0])
            else:
                os.system('cd ' + self.where + '/' + args[0])
            os.system('cd ' + self.where + '\\' + args[0])
        else:
            print(f'[WARNG] {self.f.get_time()} cd命令需要参数')
    
    def mkdir(self, args):
        # 创建文件夹
        if args:
            if os.mkdir(self.where + '/' + args[0]) == None:
                print(f'[INFO] {self.f.get_time()} {args[0]}文件夹已创建')
            else:
                print(f'[WARNG] {self.f.get_time()} {args[0]}文件夹已存在')
        else:
            print(f'[WARNG] {self.f.get_time()} mkdir命令需要参数')

    def rmdir(self, args):
        # 删除文件夹
        if args:
            if os.rmdir(self.where + '/' + args[0]) == None:
                print(f'[INFO] {self.f.get_time()} {args[0]}文件夹已删除')
            else:
                print(f'[WARNG] {self.f.get_time()} {args[0]}文件夹不存在')
        else:
            print(f'[WARNG] {self.f.get_time()} rmdir命令需要参数')
    
    def touch(self, args):
        # 创建文件
        if args:
            if os.path.exists(self.where + '/' + args[0]) == True:
                print(f'[WARNG] {self.f.get_time()} {args[0]}文件已存在')
            else:
                with open(self.where + '/' + args[0], 'w') as f:
                    f.write('')
                print(f'[INFO] {self.f.get_time()} {args[0]}文件已创建')
    
    def rm(self, args):
        # 删除文件
        if args:
            if os.remove(self.where + '/' + args[0]) == None:
                print(f'[INFO] {self.f.get_time()} {args[0]}文件已删除')
            else:
                print(f'[WARNG] {self.f.get_time()} {args[0]}文件不存在')
        else:
            print(f'[WARNG] {self.f.get_time()} rm命令需要参数')

    def cat(self, args):
        # 查看文件内容
        if args:
            try:
                with open(self.where + '/' + args[0], 'r', encoding="UTF-8") as f:
                    print(f.read())
            except:
                print(f'[WARNG] {self.f.get_time()} {args[0]}文件不存在')
        else:
            print(f'[WARNG] {self.f.get_time()} cat命令需要参数')
    
    def echo(self, args):
        # 输出内容
        if args:
            print(' '.join(args))
        else:
            print(f'[WARNG] {self.f.get_time()} echo命令需要参数')
    
    def run(self, args):
        # 在终端运行命令
        if args:
            run_text = ' '.join(args)
            os.system(run_text)
        else:
            print(f'[WARNG] {self.f.get_time()} run命令需要参数')

    def exit(self, args):
        # 退出程序
        print(f'[INFO] {self.f.get_time()} 程序已退出')
        exit(0)

    def help(self, args):
        print("""
            可用命令：
            \tls: 列出当前目录下的文件
            \tcd <路径>: 切换当前目录
            \tmkdir <文件夹名>: 创建文件夹
            \trmdir <文件夹名>: 删除文件夹
            \ttouch <文件名>: 创建文件
            \trm <文件名>: 删除文件
            \tcat <文件名>: 查看文件内容
            \techo <内容>: 输出内容
            \trun <命令>: 在终端运行命令
            \tget <参数>: 获取系统信息
            \t\tget time: 获取当前时间
            \texit: 退出程序
            \thelp: 查看帮助
        """)
        return"""
            可用命令：
            \tls: 列出当前目录下的文件
            \tcd <路径>: 切换当前目录
            \tmkdir <文件夹名>: 创建文件夹
            \trmdir <文件夹名>: 删除文件夹
            \ttouch <文件名>: 创建文件
            \trm <文件名>: 删除文件
            \tcat <文件名>: 查看文件内容
            \techo <内容>: 输出内容
            \trun <命令>: 在终端运行命令
            \tget <参数>: 获取系统信息
            \t\tget time: 获取当前时间
            \texit: 退出程序
            \thelp: 查看帮助
        """

class UI():

    """UI"""

    def __init__(self):
        """没思路。。。"""
    
    def desktop(self):
        """桌面"""
        print(
f"""\r
+--------------------------------------------------------------------+
{System_commands().help([])}
            当前目录：  {System_commands().where}
            当前时间：  {Functions().get_time()}
+--------------------------------------------------------------------+
""")
    
    def draw(self):
        os.system('mode con: cols=70 lines=22')
        while True:
            os.system('cls')
            self.desktop()
            command = input(f'{System_commands().where} --+> ')
            if command == '':
                continue
            else:
                command = command.split(' ')
                if command[0] in System_commands().commands:
                    os.system('cls')
                    print(f'[INFO] {Functions().get_time()} 正在执行命令 "{command[0]}"')
                    System_commands().commands[command[0]](command[1:])
                else:
                    print(f'[WARNG] {Functions().get_time()} 命令 "{command[0]}" 不存在')
            a = input('dress the enter key to continue...')





UI().draw()