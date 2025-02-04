import os
import random



class Game():
    def __init__(self):
        """
            一个简易的数字炸弹游戏
        """
        # 初始化变量
        self.player_win_num = 0 # 玩家胜利次数
        self.computer_win_num = 0 # 电脑胜利次数
        self.game_num = 1 # 游戏次数
        self.player_num = 0  # 玩家数字
        self.computer_num = 0  # 电脑数字
        self.player_win_num = 0  # 玩家胜利次数
        self.computer_win_num = 0  # 电脑胜利次数
        self.boom_max = 100  # 炸弹最大数字
        self.boom_min = 0  # 炸弹最小数字
        self.boom_num_max = 100  # 当前游戏中显示的炸弹数字最大数字
        self.boom_num_min = 0  # 当前游戏中显示的炸弹数字最小数字
        self.boom_num = 0   # 炸弹数字
    
    def start(self):
        """
            开始游戏的欢迎界面
        """
        # 是不是有点难看 我最开始想用art text2art
        # 但是某
        print(\
"""
 ___   _        _  _          _       _                 _
|   \ (_) __ _ (_)| |_  __ _ | |     | |__  ___  _ __  | |__  ___
| |) || |/ _` || ||  _|/ _` || |     | '_ \/ _ \| '  \ | '_ \(_-<
|___/ |_|\__, ||_| \__|\__,_||_|     |_.__/\___/|_|_|_||_.__//__/
         |___/
                            数字炸弹游戏 (C)huluobuo 2025 V1.1.8
""")
    
    def set_boom_max_and_min(self):
        """
            设置炸弹最大最小值
        """
        try:
            self.boom_max = int(input('请输入炸弹最大值：'))
            self.boom_min = int(input('请输入炸弹最小值：'))
            if self.boom_max < self.boom_min:
                print('最大值不能小于最小值，请重新输入！')
                self.set_boom_max_and_min()
            else:
                self.set_boom_num()
            if self.boom_max - self.boom_min < 2:
                print('最大值和最小值差距不能小于2，请重新输入！')
                self.set_boom_max_and_min()
        except ValueError:
            print('输入错误，请重新输入！')
            self.set_boom_max_and_min()
    
    def set_boom_num(self):
        """
            设置炸弹数字
        """
        self.boom_num = random.randint(self.boom_min + 1, self.boom_max - 1)
        self.boom_num_max = self.boom_max
        self.boom_num_min = self.boom_min


    def set_player_num(self):
        """
            玩家数字
        """
        answer = input('请输入数字（输入q退出，输入a自动输入）： ')
        if answer == 'a':
            self.player_num = random.randint(self.boom_num_min + 1, self.boom_num_max - 1)
            self.check_number('player')
        elif answer == 'q':
            print('退出游戏！')
            exit()
        else:
            try:
                self.player_num = int(answer)
                if self.player_num >= self.boom_num_max or self.player_num <= self.boom_num_min:
                    print('输入错误，请重新输入！')
                    self.set_player_num()
                else:
                    self.check_number('player')
            except ValueError:
                print('输入错误，请重新输入！')
                self.set_player_num()

    def set_computer_num(self):
        """
            电脑数字
        """
        self.computer_num = random.randint(self.boom_num_min + 1, self.boom_num_max - 1)
        self.check_number('computer')
    
    def restart(self):
        """
            重新开始游戏

        """   # 怎么看着眼晕
        max_num = self.boom_max
        min_num = self.boom_min
        game_num = self.game_num + 1
        plaer_win_num = self.player_win_num
        comuter_win_num = self.computer_win_num
        self.__init__()
        self.boom_num_max = max_num
        self.boom_num_min = min_num
        self.boom_max = max_num
        self.boom_min = min_num
        self.game_num = game_num
        self.player_win_num = plaer_win_num
        self.computer_win_num = comuter_win_num
        self.start_game()


    def check_number(self, name):           # 怎么看着更眼晕
        """
            检查是否为炸弹数字
        """
        if name == 'player':
            if self.player_num == self.boom_num:
                print(f'你输了，炸弹数字为{self.boom_num}，你猜的数字为{self.player_num}')
                self.computer_win_num += 1
                self.restart()
            else:
                if self.player_num > self.boom_num:
                    self.boom_num_max = self.player_num
                else:
                    self.boom_num_min = self.player_num
                print(f'你猜的数字为{self.player_num}，当前炸弹数字最大值为{self.boom_num_max}，最小值为{self.boom_num_min}')
                self.set_computer_num()
        else:
            if self.computer_num == self.boom_num:
                print(f'你赢了，炸弹数字为{self.boom_num}，电脑猜的数字为{self.computer_num}')
                self.player_win_num += 1
                self.restart()
            else:
                if self.computer_num > self.boom_num:
                    self.boom_num_max = self.computer_num
                else:
                    self.boom_num_min = self.computer_num
                print(f'电脑猜的数字为{self.computer_num}，当前炸弹数字最大值为{self.boom_num_max}，最小值为{self.boom_num_min}')
                self.set_player_num()

    def start_game(self):
        """
            开始游戏
        """
        self.set_boom_num()
        print(f'炸弹数字最大值为{self.boom_max}，最小值为{self.boom_min}。\n当前第{self.game_num}局，玩家胜利{self.player_win_num}局，电脑胜利{self.computer_win_num}局。')
        if random.randint(0, 1) == 0:
            self.set_player_num()
        else:
            self.set_computer_num()
    
    def run(self):
        """
            运行游戏
        """
        self.start()
        self.set_boom_max_and_min()
        self.start_game()


def main():
    os.system('cls')
    game = Game()
    game.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n游戏结束！')
        exit()
    except Exception as e:
        print("ERROR: " + e)
        exit()