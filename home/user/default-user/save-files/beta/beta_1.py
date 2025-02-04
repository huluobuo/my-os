import tkinter as tk
from tkinter import ttk, messagebox, simpledialog  # 导入simpledialog模块
import os
import datetime


"""

    注：此程序存在问题


"""


class FileManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Manager")
        self.geometry("800x600")

        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel - File list
        left_panel = tk.Frame(main_frame, width=200, height=600)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)

        # 添加文件列表框
        self.file_listbox = tk.Listbox(left_panel)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)
        self.file_listbox.bind('<<ListboxSelect>>', self.on_file_select)

        # Right panel - Operations and Info
        right_panel = tk.Frame(main_frame, width=600, height=600)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Top section - Path and operations
        top_section = tk.Frame(right_panel)
        top_section.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Path label and entry
        path_label = tk.Label(top_section, text="当前路径：")
        path_label.pack(side=tk.LEFT, padx=5)
        self.path_entry = tk.Entry(top_section, width=50)
        self.path_entry.pack(side=tk.LEFT, padx=5)

        # Operation buttons
        operation_frame = tk.Frame(top_section)
        operation_frame.pack(side=tk.LEFT, padx=5)

        create_folder_button = tk.Button(operation_frame, text="创建文件夹", command=self.create_folder)
        create_folder_button.pack(side=tk.TOP, pady=5)

        create_file_button = tk.Button(operation_frame, text="创建文件", command=self.create_file)
        create_file_button.pack(side=tk.TOP, pady=5)

        delete_folder_button = tk.Button(operation_frame, text="删除所选文件夹", command=self.delete_folder)
        delete_folder_button.pack(side=tk.TOP, pady=5)

        delete_file_button = tk.Button(operation_frame, text="删除所选文件", command=self.delete_file)
        delete_file_button.pack(side=tk.TOP, pady=5)

        # Middle section - Information panel
        middle_section = tk.Frame(right_panel)
        middle_section.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # System info labels
        system_info_frame = tk.Frame(middle_section)
        system_info_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        current_time_label = tk.Label(system_info_frame, text="当前时间：")
        current_time_label.pack(side=tk.TOP, pady=5)
        self.current_time_value = tk.Label(system_info_frame, text="")
        self.current_time_value.pack(side=tk.TOP, pady=5)

        cpu_usage_label = tk.Label(system_info_frame, text="CPU使用率：")
        cpu_usage_label.pack(side=tk.TOP, pady=5)
        self.cpu_usage_value = tk.Label(system_info_frame, text="")
        self.cpu_usage_value.pack(side=tk.TOP, pady=5)

        memory_usage_label = tk.Label(system_info_frame, text="内存使用率：")
        memory_usage_label.pack(side=tk.TOP, pady=5)
        self.memory_usage_value = tk.Label(system_info_frame, text="")
        self.memory_usage_value.pack(side=tk.TOP, pady=5)

        # Bottom section - File content viewer
        bottom_section = tk.Frame(right_panel)
        bottom_section.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        file_content_text = tk.Text(bottom_section, wrap=tk.WORD, height=10)
        file_content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        scrollbar = tk.Scrollbar(bottom_section)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=file_content_text.yview)
        file_content_text.config(yscrollcommand=scrollbar.set)

        # Initialize system info
        self.update_system_info()

        # 初始化文件列表
        self.load_file_list()

    def load_file_list(self):
        path = self.path_entry.get() or os.getcwd()
        try:
            self.file_listbox.delete(0, tk.END)
            for item in os.listdir(path):
                self.file_listbox.insert(tk.END, item)
        except Exception as e:
            messagebox.showerror("Error", f"加载文件列表失败: {e}")

    def on_file_select(self, event):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.file_listbox.get(selected_index)
            path = os.path.join(self.path_entry.get() or os.getcwd(), selected_file)
            if os.path.isfile(path):
                with open(path, 'r') as file:
                    content = file.read()
                    self.file_content_text.delete(1.0, tk.END)
                    self.file_content_text.insert(tk.END, content)

    def update_system_info(self):
        # Update current time
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.current_time_value.config(text=current_time)

        # Update CPU usage (placeholder)
        cpu_usage = "50%"  # Placeholder value
        self.cpu_usage_value.config(text=cpu_usage)

        # Update memory usage (placeholder)
        memory_usage = "30%"  # Placeholder value
        self.memory_usage_value.config(text=memory_usage)

        # Schedule next update
        self.after(1000, self.update_system_info)

    def create_folder(self):
        folder_name = tk.simpledialog.askstring("Create Folder", "请输入文件夹名称:")
        if folder_name:
            try:
                os.mkdir(os.path.join(self.path_entry.get() or os.getcwd(), folder_name))
                messagebox.showinfo("Success", f"文件夹 '{folder_name}' 已创建")
                self.load_file_list()  # 重新加载文件列表
            except Exception as e:
                messagebox.showerror("Error", f"创建文件夹失败: {e}")

    def create_file(self):
        file_name = simpledialog.askstring("Create File", "请输入文件名称:")  # 使用simpledialog.askstring
        if file_name:
            try:
                with open(os.path.join(self.path_entry.get() or os.getcwd(), file_name), 'w') as f:
                    f.write('')
                messagebox.showinfo("Success", f"文件 '{file_name}' 已创建")
                self.load_file_list()  # 重新加载文件列表
            except Exception as e:
                messagebox.showerror("Error", f"创建文件失败: {e}")

    def delete_folder(self):
        folder_name = tk.simpledialog.askstring("Delete Folder", "请输入要删除的文件夹名称:")
        if folder_name:
            try:
                os.rmdir(os.path.join(self.path_entry.get() or os.getcwd(), folder_name))
                messagebox.showinfo("Success", f"文件夹 '{folder_name}' 已删除")
                self.load_file_list()  # 重新加载文件列表
            except Exception as e:
                messagebox.showerror("Error", f"删除文件夹失败: {e}")

    def delete_file(self):
        file_name = tk.simpledialog.askstring("Delete File", "请输入要删除的文件名称:")
        if file_name:
            try:
                os.remove(os.path.join(self.path_entry.get() or os.getcwd(), file_name))
                messagebox.showinfo("Success", f"文件 '{file_name}' 已删除")
                self.load_file_list()  # 重新加载文件列表
            except Exception as e:
                messagebox.showerror("Error", f"删除文件失败: {e}")

if __name__ == "__main__":
    app = FileManager()
    app.mainloop()