import os
import datetime

# 我只用一个文件！！


class Functions():
    """
    辅助类，有些问题
    get 函数有问题
    """

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
            'get': functions.get,
            'try_new': self.try_new
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
                with open(self.where + '/' + args[0], 'r') as f:
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

    def try_new(self, args):
        os.system("python .\\home\\user\\default-user\\save-files\\new-ui\\start.py" if os.name == 'nt' else "python ./home/user/default-user/save-files/new-ui/start.py")

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
            \ttry_new: 尝试新UI
            \texit: 退出程序
            \thelp: 查看帮助
        """)


def main():
    system_me = System_commands()
    functions = Functions()
    while True:
        try:
            command = input(f'{system_me.where} ==+ ')
            command = command.split()
            if command[0] in system_me.commands:
                system_me.commands[command[0]](command[1:])
            else:
                print(f'[WARNG] {functions.get_time()} 命令 "{command[0]}" 不存在')
        except Exception as e:
            print(f'[ERROR] {functions.get_time()} 程序发生错误，已恢复。---错误代码：{e}')


if __name__ == '__main__':
    try:
        functions = Functions()
        os.system("title My Os-V1.4")       # 就改了这点？
        os.system('color 0a')
        os.system('cls')
        print('MY OS - V1.4')
        print('版权所有  (C)   huluobuo 保留所有权利。')
        print('基于Windows的powershell，但好像缺了亿点点功能')
        print('我的GitHub：    https://github.com/huluobuo\n')
        print('注意！由于技术问题，请在输入参数时以完整路径或合理的的相对路径格式输入')
        print('输入try_new尝试新UI（MyyOs-V1.5）')
        print('输入help查看可用命令\n')
        main()
    except KeyboardInterrupt:
        print(f'\n[INFO] {functions.get_time()} 程序已退出')       # e
        exit(0)