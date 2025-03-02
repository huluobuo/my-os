import os
import json


def main():         # 怎么和坨屎一样？ 这有点像屎山~~~
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('./home/user/default-user/save-files/old-ui/old.json', 'r', encoding='UTF-8') as f:
        old = json.load(f)
    print("当前老版本有：")
    number = 1
    verions = {}
    for i in old:
        print(f'{number}. {i}')
        verions[str(number)] = i
        number += 1
    system = input('请输入要运行的系统：')
    os.system("python " + old[verions[system]][0] if os.name == 'nt' else "python " + old[verions[system]][1])

if __name__ == '__main__':
    main()