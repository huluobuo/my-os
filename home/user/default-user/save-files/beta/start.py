import os
import json


def main():         # 一样~~~
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('./home/user/default-user/save-files/beta/new.json', 'r', encoding='UTF-8') as f:
        new = json.load(f)
    print("当前新版本有：")
    number = 1
    verions = {}
    for i in new:
        print(f'{number}. {i}')
        verions[str(number)] = i
        number += 1
    system = input('请输入要运行的系统：')
    os.system("python " + new[verions[system]][0] if os.name == 'nt' else "python " + old[verions[system]][1])

if __name__ == '__main__':
    main()