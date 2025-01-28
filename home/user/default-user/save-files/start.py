import os
import datetime

# 我只用一个文件！！


class Functions():
    """
            辅助类，有些问题
            get 函数有问题
    """

    def get_time(self):
            return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def get(self, args=['time']):   # 默认获取时间 
        """
            获取XXX
            正在维修中！！！
        """
        if args[0] == 'time':
            print(self.f.get_time())
        else:
            print(f'[WARNG] {self.f.get_time()} get {args[0]}命令不存在')

class System_commands():
    def __init__(self):
        functions = Functions()
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
            'exit': self.exit,
            'help': self.help
            # 'get': functions.get   我干脆不用了！！
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
                with open(self.where + args[0], 'w') as f:
                    f.write('')
    
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

    def exit(self, args):
        # 退出程序
        print(f'[INFO] {self.f.get_time()} 程序已退出')
        exit(0)

    def help(self, args):
        print(
            '可用命令：\n'
            '\t-ls: 列出当前目录下files文件夹中的文件\n' +\
            '\t-cd: 切换当前目录（注意！由于技术问题，请在输入参数时以 .\\file\\xxx 的格式输入）\n' +\
            '\t-mkdir: 创建文件夹\n' +\
            '\t-mdir: 删除文件夹\n' +\
            '\t-touch: 创建文件\n' +\
            '\t-rm: 删除文件\n' +\
            '\t-cat: 查看文件内容\n' +\
            '\t-echo: 输出内容\n' +\
            '\t-exit: 退出程序\n' +\
            '\t-help: 查看帮助\n'
        )


def main():
    system_me = System_commands()
    functions = Functions()
    while True:
        try:
            command = input(f'{system_me.where} -+ ')
            command = command.split()
            if command[0] in system_me.commands:
                system_me.commands[command[0]](command[1:])
            else:
                print(f'[WARNG] {functions.get_time()} {command[0]}命令不存在')
        except Exception as e:
            print(f'[ERROR] {functions.get_time()} 程序发生错误，已恢复。---错误代码：{e}')


if __name__ == '__main__':
    try:
        functions = Functions()
        os.system("title My Os-V1.3")       # 就改了这点？
        os.system('color 0a')
        os.system('cls')
        print('MY OS - V1.3')
        print('版权所有  (C)   huluobuo 保留所有权利。')
        print('基于Windows的powershell，但好像缺了亿点点功能')
        print('我的GitHub：    https://github.com/huluobuo\n')
        print('注意！由于技术问题，请在输入参数时以完整路径或合理的的相对路径格式输入')
        print('输入help查看可用命令\n')
        main()
    except KeyboardInterrupt:
        print(f'\n[INFO] {functions.get_time()} 程序已退出')       # e
        exit(0)