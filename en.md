My OS 2025 (C) huluobuo          | [中文简体](./README.md "中文简体") |   | [English](./en.md "English") |

# My OS

![My OS Logo](os/img/logo.jpg)

This is a simple operating system simulator developed in Python, providing basic system functions and a user interface. The system emulates the core functions of a real operating system, including a file system.

## Features

### User System
- Multi-user support
- User login interface
- Password encryption storage
- User permission management

### System Functions
- File management system
- System security mechanism

### User Interface
- Command-line interface
- Interactive operations
- User-friendly prompt messages

## System Requirements

### Hardware Requirements
- CPU: 1GHz or higher
- Memory: At least 100MB of available memory
- Hard disk space: At least 50MB of available space

### Software Requirements
- Python 3.6 or higher (Developed with Python 3.10 + Python 3.11)
- Windows 7 or higher, or Linux operating system (Developed with Windows 10 X64 + Windows 11 X64)

## Usage
1. Run the following command in the project root directory:
   ```bash
   python run.py
   ```

2. The program will automatically check and install the required dependencies.
3. After startup, you will see the login interface:
   - Select a user account (default: default_user)
   - Enter the password (default: 123456)
   - After successful login, you can use the system functions.

## System Architecture

### Directory Structure
```
my-os/
├── os/                   # Operating system core code
│   ├── mos/              # System core module
│   ├── steer/            # User guidance module
│   └── fonts/            # System font files
├── home/                 # User directory
│   └── program-files/    # System program files
├── run.py                # Main program entry
└── requirements.txt      # Project dependencies
```

## Dependencies
- cryptography==42.0.5   # For password encryption
- art==6.1               # For ASCII art display
- pygame==2.5.2          # For the graphical interface (V1.5)
- psutil==5.9.8          # For system resource monitoring
- keyboard==0.13.5       # For keyboard input processing

## Security Features
- User password encryption storage
- System key management
- Secure user authentication mechanism

## Notes
- The required dependencies will be automatically installed on the first run.
- If you encounter any issues, please check:
  - Whether the Python version meets the requirements.
  - Whether the dependency packages are installed successfully.
  - Whether the system permissions are sufficient (usually no additional permissions are required).

## Development Plan
- [ ] Add more system tools.
- [ ] Optimize the user interface.
- [ ] Add network functionality.
- [ ] Add more security features.

## License
This project is licensed under the MIT License.

MIT License

Copyright (c) 2025 huluobuo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
