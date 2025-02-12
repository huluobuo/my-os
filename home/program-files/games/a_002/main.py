from os import system
from random import randint


class Game():
    """
        一款出题游戏，有三种难度，
        简单：1-100 加减法
        中等：1-100 加减 + 1~10 乘除
        困难：1-1000 加减 + 1~100 乘除
        不是，这还是游戏吗？？？
    """

    def __init__(self):
        """初始化""" # 一定不要忘了注释！！！
        self.topic_level = 0  # 0-简单 1-中等 2-困难
        self.topic_type = [[False, 1, 100], [True, 1, 100, 1, 10], [True, 1, 1000, 1, 100]]  # [是否存在乘除(True/False), 1, 100, 1, 10]
        self.topic_num = 0  # 题目数量
        self.topic_list = []  # 题目列表
        self.topic_right_answer = []  # 题目答案列表
        self.user_right_answer_num = 0  # 用户答对题目数量
        self.user_wrong_answer_num = 0  # 用户答错题目数量  (是不是有点多余~~~但少了一个减法)
        self.user_error_answer_num = 0  # 用户输入非法字符的数量

    def start(self):
        """输出使用指南"""
        print("""
        简单：1-100 加减法
        中等：1-100 加减 + 1~10 乘除
        困难：1-1000 加减 + 1~100 乘除
        """)
    
    def set_topic_level_and_topi_num(self):
        """设置题目难度和题目数量"""
        try:
            self.topic_level = int(input("请输入题目难度（0-简单 1-中等 2-困难）："))     # 这样设置在之后操作列表时会方便一些
            # 判断输入是否合法
            if self.topic_level not in [0, 1, 2]:
                print("输入错误，请重新输入！")
                self.set_topic_level_and_topi_num()
            self.topic_num = int(input("请输入题目数量："))
        except ValueError:
            print("输入错误，请重新输入！")
            self.set_topic_level_and_topi_num()
        except KeyboardInterrupt:
            print("退出程序！")
            exit()
    
    def make_topic(self):
        """生成题目（有点费脑子）"""
        topic = ''
        rightt_answer = 0 
        for num in range(0, self.topic_num, 1):
            if self.topic_type[self.topic_level][0]:      # 存在乘除
                if randint(0, 1) == 0:  # 生成加减
                    a = randint(self.topic_type[self.topic_level][1], self.topic_type[self.topic_level][2])
                    b = randint(self.topic_type[self.topic_level][1], self.topic_type[self.topic_level][2])
                    if randint(0, 1) == 0:  # +
                        topic = str(a) + ' + ' + str(b) + ' = ?  '
                        rightt_answer = a + b
                    else:                   # -
                        topic = str(a) + ' - ' + str(b) + ' = ?  '
                        rightt_answer = a - b

                else:  # 生成乘除
                    a = randint(self.topic_type[self.topic_level][1], self.topic_type[self.topic_level][2])
                    b = randint(self.topic_type[self.topic_level][3], self.topic_type[self.topic_level][4])
                    if randint(0, 1) == 0:  # *
                        topic = str(a) + ' * ' + str(b) + ' = ?  '
                        rightt_answer = a * b
                    else:                   # /
                        while True:        # 避免除数为0,且结果为整数
                            a = randint(self.topic_type[self.topic_level][3], self.topic_type[self.topic_level][4])
                            b = randint(self.topic_type[self.topic_level][3], self.topic_type[self.topic_level][4])
                            if b != 0 and a % b == 0:
                                break
                        topic = str(a) + ' / ' + str(b) + ' = ?  '
                        rightt_answer = a / b
            else:  # 不存在乘除
                a = randint(self.topic_type[self.topic_level][1], self.topic_type[self.topic_level][2])
                b = randint(self.topic_type[self.topic_level][1], self.topic_type[self.topic_level][2])
                if randint(0, 1) == 0:        # +
                    topic = str(a) + ' + ' + str(b) + ' = ?  '
                    rightt_answer = a + b
                else:                         # -
                    topic = str(a) + ' - ' + str(b) + ' = ?  '
                    rightt_answer = a - b
            # 添加到列表中
            self.topic_list.append(topic)
            self.topic_right_answer.append(rightt_answer)
        
    def get_answer(self):
        """获取用户答案"""
        for num in range(0, self.topic_num, 1):
            print(f"当前第{num + 1}题， 题目： {self.topic_list[num]}")
            try:
                user_answer = int(input("请输入你的答案："))
                if user_answer == self.topic_right_answer[num]:
                    print("正确！")
                    self.user_right_answer_num += 1
                else:
                    print("错误！")
                    self.user_wrong_answer_num += 1
            except ValueError:
                print("输入错误")
                self.user_error_answer_num += 1
            except KeyboardInterrupt:
                print("退出程序！")
                exit()
    
    def show_result(self):
        """显示结果"""
        print(f"统计：\n\t你答对了{self.user_right_answer_num}题，答错了{self.user_wrong_answer_num}题，输入错误{self.user_error_answer_num}次")
    
    def run(self):
        """运行游戏"""
        system('cls')
        self.start()
        self.set_topic_level_and_topi_num()
        self.make_topic()
        self.get_answer()
        self.show_result()

if __name__ == '__main__':
    game = Game()
    game.run()