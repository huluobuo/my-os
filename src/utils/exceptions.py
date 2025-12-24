"""
自定义异常类
"""


class OSException(Exception):
    """操作系统基础异常类"""
    
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
        self.message = message
    
    def __str__(self):
        if self.error_code:
            return f"[{self.error_code}] {self.message}"
        return self.message


class AuthenticationError(OSException):
    """认证异常"""
    
    def __init__(self, message="认证失败"):
        super().__init__(message, "AUTH_ERROR")


class FileSystemError(OSException):
    """文件系统异常"""
    
    def __init__(self, message="文件系统错误"):
        super().__init__(message, "FS_ERROR")


class PermissionError(OSException):
    """权限异常"""
    
    def __init__(self, message="权限不足"):
        super().__init__(message, "PERM_ERROR")


class CommandError(OSException):
    """命令执行异常"""
    
    def __init__(self, message="命令执行失败"):
        super().__init__(message, "CMD_ERROR")