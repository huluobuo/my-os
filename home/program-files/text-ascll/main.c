#include <windows.h>
#include <stdio.h>
#include <string.h>  // 包含字符串处理函数

int main()
{
    system("cls");
    system("title ASCII码转换器");
    system("color 0A");                  // 豪看 qwq
    system("mode con cols=20 lines=20");
    char a[100];          // 存储用户输入
    int b, c;
    SetConsoleOutputCP(65001);  // 设置控制台输出为 UTF-8 编码
    printf("/------------------\\\n");
    printf("|   ASCII码转换器  |\n");
    printf("|  1.ASCII码转字符 |\n");
    printf("|  2.字符转ASCII码 |\n");
    printf("|  3.退出          |\n");
    printf("\\------------------/\n");
    printf("请输入选项：  ");
    scanf("%i", &b);
    getchar();  // 消除缓冲区中的换行符
    Sleep(10);  // 短暂延迟

    switch(b)
    {
        case 1:
            printf("请输入ASCII码：");
            scanf("%d", &c);  // 读取整数
            if (c >= 0 && c <= 255)  // ASCII 码范围
            {
                printf("ASCII码 %d \n对应的字符是: %c \n", c, (char)c);
            }
            else
            {
                printf("无效的ASCII码范围！\n");
            }
            break;

        case 2:
            printf("请输入字符：");
            scanf("%s", a);  // 读取字符串
            for (c = 0; c < strlen(a); c++)  // 遍历字符串
            {
                printf("字符 %c \n对应的ASCII码是: %d \n", a[c], (int)a[c]);
            }
            break;

        case 3:
            printf("已退出\n");
            break;

        default:
            printf("无效选项！\n");
    }

    Sleep(1000);  // 延迟1秒
    return 0;
}