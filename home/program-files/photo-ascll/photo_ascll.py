from tkinter import Tk, Label, Entry, Button, filedialog, Text, Scrollbar, END         # 这么久了，才想起来TK
from PIL import Image
import numpy as np

# 定义ASCII字符集
ASCII_CHARS = "@%#*+=-:. "
# ASCII_CHARS = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"
# ASCII_CHARS = "█▒░㍿ヅ々﹟₪ "


def resize_image(image, new_width=100):
    """调整图像大小"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)  # 调整高度比例以适应ASCII字符的宽高比
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """将图像转换为灰度图"""
    return image.convert("L")

def pixels_to_ascii(image):
    """将像素转换为ASCII字符"""
    pixels = np.array(image)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel // 32]  # 将像素值映射到ASCII字符集
        ascii_str += "\n"
    return ascii_str

def open_image():
    """打开图片并显示ASCII艺术"""
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        image = Image.open(file_path)
        new_width = int(width_entry.get()) if width_entry.get().isdigit() else 100
        image = resize_image(image, new_width)
        image = grayscale_image(image)
        ascii_art = pixels_to_ascii(image)
        ascii_text.delete(1.0, END)
        ascii_text.insert(END, ascii_art)
    except Exception as e:
        ascii_text.delete(1.0, END)
        ascii_text.insert(END, f"无法打开图片：{e}")

# 创建主窗口
root = Tk()
root.title("图片转ASCII艺术")

# 创建标签和输入框
Label(root, text="图片宽度：").grid(row=0, column=0, padx=10, pady=10)
width_entry = Entry(root)
width_entry.grid(row=0, column=1, padx=10, pady=10)
width_entry.insert(0, "100")  # 默认值

Label(root, text="图片位置：").grid(row=1, column=0, padx=10, pady=10)
file_path_entry = Entry(root)
file_path_entry.grid(row=1, column=1, padx=10, pady=10)

open_button = Button(root, text="打开", command=open_image)
open_button.grid(row=1, column=2, padx=10, pady=10)

# 创建文本框用于显示ASCII艺术
ascii_text = Text(root, wrap="none")
ascii_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# 添加滚动条
scrollbar = Scrollbar(root, command=ascii_text.yview)
scrollbar.grid(row=2, column=3, sticky="ns")
ascii_text.config(yscrollcommand=scrollbar.set)

# 设置窗口的最小大小
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)
root.geometry("500x400")

# 运行主循环
root.mainloop()