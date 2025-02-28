#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <signal.h>
#include <windows.h>  // 解决编码问题

#define MAX_COMMAND_LENGTH 1024
#define MAX_PATH_LENGTH 1024

char current_path[MAX_PATH_LENGTH];

// 获取当前时间
char* get_time() {
    time_t raw_time;
    struct tm* time_info;
    char* buffer = malloc(20 * sizeof(char));
    time(&raw_time);
    time_info = localtime(&raw_time);
    strftime(buffer, 20, "%Y-%m-%d %H:%M:%S", time_info);
    return buffer;
}

// 打印当前时间
void print_time() {
    char* time_str = get_time();
    printf("%s\n", time_str);
    free(time_str);
}

// 初始化系统命令
void init_system_commands() {
    getcwd(current_path, MAX_PATH_LENGTH);
}

// 打印帮助信息
void print_help() {
    printf("\n可用命令：\n");
    printf("\tls: 列出当前目录下的文件\n");
    printf("\tcd <路径>: 切换当前目录\n");
    printf("\tmkdir <文件夹名>: 创建文件夹\n");
    printf("\trmdir <文件夹名>: 删除文件夹\n");
    printf("\ttouch <文件名>: 创建文件\n");
    printf("\trm <文件名>: 删除文件\n");
    printf("\tcat <文件名>: 查看文件内容\n");
    printf("\techo <内容>: 输出内容\n");
    printf("\trun <命令>: 在终端运行命令\n");
    printf("\tget <参数>: 获取系统信息\n");
    printf("\t\tget time: 获取当前时间\n");
    printf("\texit: 退出程序\n");
    printf("\thelp: 查看帮助\n");
}

// 列出当前目录下的文件
void list_files() {
    DIR* dir;
    struct dirent* entry;
    printf("%s下的文件有：\n", current_path);
    if ((dir = opendir(current_path)) != NULL) {
        while ((entry = readdir(dir)) != NULL) {
            printf("\t%s\n", entry->d_name);
        }
        closedir(dir);
    } else {
        printf("[WARNG] %s 无法打开目录\n", get_time());
    }
}

// 切换当前目录
void change_directory(char* path) {
    if (chdir(path) == 0) {
        getcwd(current_path, MAX_PATH_LENGTH);
    } else {
        printf("[WARNG] %s cd命令需要参数\n", get_time());
    }
}

// 创建文件夹
void make_directory(char* dirname) {
    if (mkdir(dirname) == 0) {
        printf("[INFO] %s 文件夹已创建\n", get_time());
    } else {
        printf("[WARNG] %s 文件夹已存在\n", get_time());
    }
}

// 删除文件夹
void remove_directory(char* dirname) {
    if (rmdir(dirname) == 0) {
        printf("[INFO] %s 文件夹已删除\n", get_time());
    } else {
        printf("[WARNG] %s 文件夹不存在\n", get_time());
    }
}

// 创建文件
void create_file(char* filename) {
    FILE* file = fopen(filename, "w");
    if (file != NULL) {
        fclose(file);
        printf("[INFO] %s 文件已创建\n", get_time());
    } else {
        printf("[WARNG] %s 文件已存在\n", get_time());
    }
}

// 删除文件
void remove_file(char* filename) {
    if (remove(filename) == 0) {
        printf("[INFO] %s 文件已删除\n", get_time());
    } else {
        printf("[WARNG] %s 文件不存在\n", get_time());
    }
}

// 查看文件内容
void cat_file(char* filename) {
    FILE* file = fopen(filename, "r");
    if (file != NULL) {
        char buffer[1024];
        while (fgets(buffer, sizeof(buffer), file)) {
            printf("%s", buffer);
        }
        fclose(file);
    } else {
        printf("[WARNG] %s 文件不存在\n", get_time());
    }
}

// 输出内容
void echo_command(char* args[]) {
    for (int i = 1; args[i] != NULL; i++) {
        printf("%s ", args[i]);
    }
    printf("\n");
}

// 在终端运行命令
void run_command(char* args[]) {
    char command[MAX_COMMAND_LENGTH];
    command[0] = '\0';
    for (int i = 1; args[i] != NULL; i++) {
        strcat(command, args[i]);
        strcat(command, " ");
    }
    system(command);
}

// 处理用户输入的命令
void handle_command(char* command, char* args[]) {
    if (strcmp(command, "ls") == 0) {
        list_files();
    } else if (strcmp(command, "cd") == 0) {
        if (args[1] != NULL) {
            change_directory(args[1]);
        } else {
            printf("[WARNG] %s cd命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "mkdir") == 0) {
        if (args[1] != NULL) {
            make_directory(args[1]);
        } else {
            printf("[WARNG] %s mkdir命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "rmdir") == 0) {
        if (args[1] != NULL) {
            remove_directory(args[1]);
        } else {
            printf("[WARNG] %s rmdir命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "touch") == 0) {
        if (args[1] != NULL) {
            create_file(args[1]);
        } else {
            printf("[WARNG] %s touch命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "rm") == 0) {
        if (args[1] != NULL) {
            remove_file(args[1]);
        } else {
            printf("[WARNG] %s rm命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "cat") == 0) {
        if (args[1] != NULL) {
            cat_file(args[1]);
        } else {
            printf("[WARNG] %s cat命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "echo") == 0) {
        echo_command(args);
    } else if (strcmp(command, "run") == 0) {
        run_command(args);
    } else if (strcmp(command, "get") == 0) {
        if (args[1] != NULL) {
            if (strcmp(args[1], "time") == 0) {
                print_time();
            } else {
                printf("[WARNG] %s 命令 \"%s\" 不存在\n", get_time(), args[1]);
            }
        } else {
            printf("[WARNG] %s get命令需要参数\n", get_time());
        }
    } else if (strcmp(command, "exit") == 0) {
        printf("[INFO] %s 程序已退出\n", get_time());
        exit(0);
    } else if (strcmp(command, "help") == 0) {
        print_help();
    } else {
        printf("[WARNG] %s 命令 \"%s\" 不存在\n", get_time(), command);
    }
}

// 主函数
int main() {
    SetConsoleOutputCP(65001);
    init_system_commands();
    char input[MAX_COMMAND_LENGTH];
    char* args[MAX_COMMAND_LENGTH / 2];
    printf("MY OS - V1.4\n");
    printf("版权所有 (C) huluobuo 保留所有权利。\n");
    printf("基于Unix的终端，但好像缺了亿点点功能\n");
    printf("我的GitHub：https://github.com/huluobuo\n");
    printf("注意！由于技术问题，请在输入参数时以完整路径或合理的相对路径格式输入\n");
    printf("输入help查看可用命令\n");

    while (1) {
        printf("%s ==+ ", current_path);
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0; // Remove newline character
        int arg_count = 0;
        char* token = strtok(input, " ");
        while (token != NULL) {
            args[arg_count++] = token;
            token = strtok(NULL, " ");
        }
        args[arg_count] = NULL;
        if (arg_count > 0) {
            handle_command(args[0], args);
        }
    }
    return 0;
}