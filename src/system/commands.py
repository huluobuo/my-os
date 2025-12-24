import os
import datetime
import shutil


class SystemCommands:
    """系统命令处理器"""
    
    def __init__(self):
        self.current_directory = os.getcwd()
        self.commands = {
            'help': self.show_help,
            'ls': self.list_files,
            'cd': self.change_directory,
            'mkdir': self.make_directory,
            'rmdir': self.remove_directory,
            'touch': self.create_file,
            'rm': self.remove_file,
            'cat': self.show_file_content,
            'clear': self.clear_screen,
            'pwd': self.show_current_directory,
            'date': self.show_date,
            'time': self.show_time,
            'cp': self.copy_file,
            'mv': self.move_file
        }
    
    def execute(self, command):
        """执行命令"""
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd in self.commands:
            self.commands[cmd](*args)
        else:
            print(f"未知命令: {cmd}")
    
    def show_help(self):
        """显示帮助信息"""
        print("可用命令:")
        print("  help     - 显示此帮助信息")
        print("  ls       - 列出当前目录文件")
        print("  cd <dir> - 切换目录")
        print("  mkdir <dir> - 创建目录")
        print("  rmdir <dir> - 删除目录")
        print("  touch <file> - 创建文件")
        print("  rm <file> - 删除文件")
        print("  cat <file> - 显示文件内容")
        print("  clear    - 清屏")
        print("  pwd      - 显示当前目录")
        print("  date     - 显示日期")
        print("  time     - 显示时间")
        print("  cp <src> <dst> - 复制文件")
        print("  mv <src> <dst> - 移动文件")
        print("  exit     - 退出系统")
    
    def list_files(self):
        """列出文件"""
        try:
            files = os.listdir(self.current_directory)
            for file in files:
                file_path = os.path.join(self.current_directory, file)
                if os.path.isdir(file_path):
                    print(f"[DIR]  {file}")
                else:
                    print(f"[FILE] {file}")
        except Exception as e:
            print(f"错误: {e}")
    
    def change_directory(self, directory=None):
        """切换目录"""
        if not directory:
            print("用法: cd <目录名>")
            return
        
        try:
            if os.path.isabs(directory):
                new_dir = directory
            else:
                new_dir = os.path.join(self.current_directory, directory)
            
            if os.path.exists(new_dir) and os.path.isdir(new_dir):
                os.chdir(new_dir)
                self.current_directory = new_dir
                print(f"切换到: {new_dir}")
            else:
                print(f"目录不存在: {directory}")
        except Exception as e:
            print(f"错误: {e}")
    
    def make_directory(self, directory=None):
        """创建目录"""
        if not directory:
            print("用法: mkdir <目录名>")
            return
        
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"目录已创建: {directory}")
        except Exception as e:
            print(f"错误: {e}")
    
    def remove_directory(self, directory=None):
        """删除目录"""
        if not directory:
            print("用法: rmdir <目录名>")
            return
        
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"目录已删除: {directory}")
            else:
                print(f"目录不存在: {directory}")
        except Exception as e:
            print(f"错误: {e}")
    
    def create_file(self, filename=None):
        """创建文件"""
        if not filename:
            print("用法: touch <文件名>")
            return
        
        try:
            with open(filename, 'w') as f:
                pass
            print(f"文件已创建: {filename}")
        except Exception as e:
            print(f"错误: {e}")
    
    def remove_file(self, filename=None):
        """删除文件"""
        if not filename:
            print("用法: rm <文件名>")
            return
        
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"文件已删除: {filename}")
            else:
                print(f"文件不存在: {filename}")
        except Exception as e:
            print(f"错误: {e}")
    
    def show_file_content(self, filename=None):
        """显示文件内容"""
        if not filename:
            print("用法: cat <文件名>")
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"错误: {e}")
    
    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_current_directory(self):
        """显示当前目录"""
        print(self.current_directory)
    
    def show_date(self):
        """显示日期"""
        print(datetime.datetime.now().strftime('%Y-%m-%d'))
    
    def show_time(self):
        """显示时间"""
        print(datetime.datetime.now().strftime('%H:%M:%S'))
    
    def copy_file(self, source=None, destination=None):
        """复制文件"""
        if not source or not destination:
            print("用法: cp <源文件> <目标文件>")
            return
        
        try:
            shutil.copy2(source, destination)
            print(f"文件已复制: {source} -> {destination}")
        except Exception as e:
            print(f"错误: {e}")
    
    def move_file(self, source=None, destination=None):
        """移动文件"""
        if not source or not destination:
            print("用法: mv <源文件> <目标文件>")
            return
        
        try:
            shutil.move(source, destination)
            print(f"文件已移动: {source} -> {destination}")
        except Exception as e:
            print(f"错误: {e}")