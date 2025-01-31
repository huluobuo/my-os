import os
import datetime
import pygame
import sys
import platform

# 我只用一个文件！！


class Functions():
    """
    辅助类，有些问题
    get 函数有问题
    是不是毫无必要？？？
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
                return self.get_time()
            else:
                return f'[WARNG] {self.get_time()} 命令 "{args[0]}" 不存在'
        else:
            return f'[WARNG] {self.get_time()} get 命令需要参数'

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
        result = [f'{self.where}下的文件有：']
        for file in files:
            result.append('\t' + file)
        return '\n'.join(result)

    def cd(self, args):
        # 切换当前目录
        if args:
            self.where = args[0]
            # 分析当前系统
            if os.name == 'nt':
                os.system('cd ' + self.where + '\\' + args[0])
            else:
                os.system('cd ' + self.where + '/' + args[0])
            return f'[INFO] {self.f.get_time()} 已切换到 {args[0]}'
        else:
            return f'[WARNG] {self.f.get_time()} cd命令需要参数'
    
    def mkdir(self, args):
        # 创建文件夹
        if args:
            try:
                os.mkdir(self.where + '/' + args[0])
                return f'[INFO] {self.f.get_time()} {args[0]}文件夹已创建'
            except:
                return f'[WARNG] {self.f.get_time()} {args[0]}文件夹已存在'
        else:
            return f'[WARNG] {self.f.get_time()} mkdir命令需要参数'

    def rmdir(self, args):
        # 删除文件夹
        if args:
            try:
                os.rmdir(self.where + '/' + args[0])
                return f'[INFO] {self.f.get_time()} {args[0]}文件夹已删除'
            except:
                return f'[WARNG] {self.f.get_time()} {args[0]}文件夹不存在'
        else:
            return f'[WARNG] {self.f.get_time()} rmdir命令需要参数'
    
    def touch(self, args):
        # 创建文件
        if args:
            if os.path.exists(self.where + '/' + args[0]):
                return f'[WARNG] {self.f.get_time()} {args[0]}文件已存在'
            else:
                with open(self.where + '/' + args[0], 'w') as f:
                    f.write('')
                return f'[INFO] {self.f.get_time()} {args[0]}文件已创建'
        return f'[WARNG] {self.f.get_time()} touch命令需要参数'
    
    def rm(self, args):
        # 删除文件
        if args:
            try:
                os.remove(self.where + '/' + args[0])
                return f'[INFO] {self.f.get_time()} {args[0]}文件已删除'
            except:
                return f'[WARNG] {self.f.get_time()} {args[0]}文件不存在'
        return f'[WARNG] {self.f.get_time()} rm命令需要参数'

    def cat(self, args):
        # 查看文件内容
        if args:
            try:
                with open(self.where + '/' + args[0], 'r') as f:
                    return f.read()
            except:
                return f'[WARNG] {self.f.get_time()} {args[0]}文件不存在'
        return f'[WARNG] {self.f.get_time()} cat命令需要参数'
    
    def echo(self, args):
        # 输出内容
        if args:
            return ' '.join(args)
        return f'[WARNG] {self.f.get_time()} echo命令需要参数'
    
    def run(self, args):
        # 在终端运行命令
        if args:
            run_text = ' '.join(args)
            try:
                output = os.popen(run_text).read()
                return output if output else f'[INFO] {self.f.get_time()} 命令执行完成'
            except Exception as e:
                return f'[ERROR] {self.f.get_time()} 命令执行失败: {e}'
        return f'[WARNG] {self.f.get_time()} run命令需要参数'

    def exit(self, args):
        # 退出程序
        exit(0)     # 那就不返回值了

    def help(self, args):
        return """
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


class GUI:
    def __init__(self, size_choice=1):
        pygame.init()
        
        # 根据用户选择设置窗口大小
        if size_choice == 1:
            self.width = 800
            self.height = 600
            self.screen = pygame.display.set_mode((self.width, self.height))
        elif size_choice == 2:
            self.width = 1800
            self.height = 900
            self.screen = pygame.display.set_mode((self.width, self.height))
        elif size_choice == 3:
            screen_info = pygame.display.Info()
            self.width = screen_info.current_w
            self.height = screen_info.current_h
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        
        pygame.display.set_caption("MY OS V1.5")
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (50, 50, 50)  # 更深的灰色作为背景
        self.SILVER = (192, 192, 192)  # 银灰色用于分隔线
        
        # Font
        try:
            self.font = pygame.font.Font("./os/fonts/SimHei.ttf", 16)
        except:
            print("未找到中文字体，使用默认字体")
            self.font = pygame.font.Font(None, 24)
        
        # 布局设置
        self.right_panel_width = int(self.width * 0.3)  # 右侧面板宽度为窗口宽度的30%
        self.graph_height = 80  # 每个图表的高度
        self.graph_spacing = 40  # 图表之间的间距
        self.info_spacing = 30  # 信息文本之间的间距
        self.graph_history = {'cpu': [], 'memory': []}
        self.max_history = self.right_panel_width - 40
        
        # 命令行区域宽度
        self.terminal_width = self.width - self.right_panel_width
        
        # 初始化所有需要的属性
        self.command_history = []
        self.input_text = ""
        self.cursor_visible = True
        self.cursor_timer = 0
        self.command_history_index = -1
        self.current_input = ""
        self.command_memory = []
        
        self.system_commands = System_commands()
        self.functions = Functions()

    def get_system_info(self):
        import psutil
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        # 更新历史数据
        self.graph_history['cpu'].append(cpu_percent)
        self.graph_history['memory'].append(memory_percent)
        
        # 保持固定长度
        if len(self.graph_history['cpu']) > self.max_history:
            self.graph_history['cpu'].pop(0)
        if len(self.graph_history['memory']) > self.max_history:
            self.graph_history['memory'].pop(0)
        
        return {
            'memory_used': f"{memory.used / (1024**3):.1f}",
            'memory_total': f"{memory.total / (1024**3):.1f}",
            'os': platform.system(),
            'os_version': platform.version(),
            'cpu_model': platform.processor() or "Unknown CPU"
        }

    def draw_graph(self, data, rect, color):
        if not data:
            return
            
        # 绘制背景
        pygame.draw.rect(self.screen, self.GRAY, rect)
        
        # 绘制图表
        points = []
        for i, value in enumerate(data):
            x = rect[0] + (i * rect[2] / len(data))
            y = rect[1] + rect[3] - (value * rect[3] / 100)
            points.append((x, y))
            
        if len(points) > 1:
            pygame.draw.lines(self.screen, color, False, points, 1)

    def draw(self):
        self.screen.fill(self.BLACK)
        
        # 获取系统信息
        sys_info = self.get_system_info()
        
        # 绘制右侧面板背景
        right_panel = pygame.Rect(self.terminal_width, 0, self.right_panel_width, self.height)
        pygame.draw.rect(self.screen, self.GRAY, right_panel)
        
        # 绘制CPU使用率图表
        cpu_y = 20  # 增加顶部边距
        cpu_rect = (self.terminal_width + 10, cpu_y, 
                   self.right_panel_width - 20, self.graph_height)
        self.draw_graph(self.graph_history['cpu'], cpu_rect, self.GREEN)
        
        # 绘制第一条分隔线
        line1_y = cpu_y + self.graph_height + self.graph_spacing/2
        pygame.draw.line(self.screen, self.SILVER,
                        (self.terminal_width + 5, line1_y),
                        (self.width - 5, line1_y))
        
        # 绘制内存使用率图表
        mem_y = cpu_y + self.graph_height + self.graph_spacing
        mem_rect = (self.terminal_width + 10, mem_y,
                   self.right_panel_width - 20, self.graph_height)
        self.draw_graph(self.graph_history['memory'], mem_rect, self.BLUE)
        
        # 绘制第二条分隔线
        line2_y = mem_y + self.graph_height + self.graph_spacing/2
        pygame.draw.line(self.screen, self.SILVER,
                        (self.terminal_width + 5, line2_y),
                        (self.width - 5, line2_y))
        
        # 绘制系统信息
        info_start_y = mem_y + self.graph_height + self.graph_spacing
        info_texts = [
            f"当前内存使用情况：",
            f"{sys_info['memory_used']} / {sys_info['memory_total']} GB",
            "",  # 添加空行增加间距
            f"当前操作系统：",
            f"{sys_info['os']}",
            "",  # 添加空行增加间距
            f"当前操作系统版本：",
            f"{sys_info['os_version']}",
            "",  # 添加空行增加间距
            f"CPU型号：",
            f"{sys_info['cpu_model']}"
        ]
        
        for i, text in enumerate(info_texts):
            text_surface = self.font.render(text, True, self.GREEN)
            self.screen.blit(text_surface, 
                           (self.terminal_width + 10, info_start_y + i * self.info_spacing))
        
        # 绘制命令历史（在左侧区域）
        visible_lines = (self.height - 50) // 20
        visible_history = self.command_history[-visible_lines:]
        
        y = 10
        for cmd in visible_history:
            try:
                if isinstance(cmd, bytes):
                    cmd = cmd.decode('utf-8')
                text = self.font.render(str(cmd), True, self.GREEN)
                # 确保文本不会超出左侧区域
                if text.get_width() > self.terminal_width - 20:
                    # 如果文本太长，截断显示
                    text = self.font.render(str(cmd)[:50] + "...", True, self.GREEN)
                self.screen.blit(text, (10, y))
            except Exception:
                try:
                    text = self.font.render(str(cmd).encode('ascii', 'replace').decode(), True, self.GREEN)
                    self.screen.blit(text, (10, y))
                except:
                    pass
            y += 20
        
        # 绘制输入行（在左侧区域底部）
        prompt = f"{self.system_commands.where} ==+ "
        try:
            prompt_text = self.font.render(prompt, True, self.GREEN)
            input_surface = self.font.render(self.input_text, True, self.GREEN)
        except:
            prompt_text = self.font.render(prompt.encode('ascii', 'replace').decode(), True, self.GREEN)
            input_surface = self.font.render(self.input_text.encode('ascii', 'replace').decode(), True, self.GREEN)
        
        self.screen.blit(prompt_text, (10, self.height - 40))
        self.screen.blit(input_surface, (prompt_text.get_width() + 10, self.height - 40))
        
        if self.cursor_visible:
            cursor_pos = prompt_text.get_width() + input_surface.get_width() + 12
            pygame.draw.line(self.screen, self.GREEN,
                           (cursor_pos, self.height - 40),
                           (cursor_pos, self.height - 15))
        
        pygame.display.flip()

    def execute_command(self, command_text):
        try:
            # 确保命令文本使用UTF-8编码
            if isinstance(command_text, bytes):
                command_text = command_text.decode('utf-8')
            
            self.command_history.append(f"{self.system_commands.where} ==+ {command_text}")
            command = command_text.split()
            if command[0] in self.system_commands.commands:
                result = self.system_commands.commands[command[0]](command[1:])
                if result:  # 如果命令有输出结果
                    # 处理多行输出
                    for line in result.split('\n'):
                        if line.strip():  # 忽略空行
                            self.command_history.append(line)
            else:
                self.command_history.append(
                    f'[WARNG] {self.functions.get_time()} 命令 "{command[0]}" 不存在'
                )
        except Exception as e:
            self.command_history.append(
                f'[ERROR] {self.functions.get_time()} 程序发生错误，已恢复。---错误代码：{e}'
            )

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.input_text:
                            self.execute_command(self.input_text)
                            self.command_memory.append(self.input_text)
                            self.command_history_index = -1
                            self.current_input = ""
                            self.input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    elif event.key == pygame.K_UP:
                        if len(self.command_memory) > 0:
                            if self.command_history_index == -1:
                                self.current_input = self.input_text
                            self.command_history_index = min(self.command_history_index + 1, len(self.command_memory) - 1)
                            self.input_text = self.command_memory[-(self.command_history_index + 1)]
                    elif event.key == pygame.K_DOWN:
                        if self.command_history_index > -1:
                            self.command_history_index -= 1
                            if self.command_history_index == -1:
                                self.input_text = self.current_input
                            else:
                                self.input_text = self.command_memory[-(self.command_history_index + 1)]
                elif event.type == pygame.TEXTINPUT:
                    # 使用 TEXTINPUT 事件处理文本输入，包括中文
                    self.input_text += event.text
            
            # Cursor blinking
            self.cursor_timer += 1
            if self.cursor_timer >= 30:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0
            
            self.draw()
            clock.tick(60)


def main():
    # 显示窗口大小选项
    print("请选择窗口大小：")
    print("1. 800x600")
    print("2. 1800x900")
    print("3. 全屏")
    
    while True:
        try:
            choice = int(input("请输入选项 (1-3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("无效选项，请重新输入")
        except ValueError:
            print("请输入数字 1-3")
    
    gui = GUI(choice)
    gui.command_history.extend([
        'MY OS - V1.5',
        '版权所有  (C)   huluobuo 保留所有权利。',
        '基于Pygame的GUI界面',
        '我的GitHub：    https://github.com/huluobuo',
        '',
        '注意！由于技术问题，请在输入参数时以完整路径或合理的的相对路径格式输入',
        '输入help查看可用命令',
        ''
    ])
    gui.run()


if __name__ == '__main__':
    main()


################################################################################################################
#    制作者：huluobuo
#    制作时间：2025年1月31日
#    版权所有：  (C) huluobuo 保留所有权利。
#    注：
#        1.在制作时，使用了通灵代码 和 claude 3.5 模型。
#        2.本程序仅供学习、参考和装逼用途，请勿用于其他 非法用途。
#################################################################################################################