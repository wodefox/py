import os
import subprocess
import socket
import json
import requests
import shutil
import sys
import time
import datetime
import zipfile
import sqlite3
import logging
import signal
import platform
import psutil
import wx
import paramiko
import http.server
import socketserver
from flask import Flask


class CoreModule:
    def __init__(self):
        pass

    # 文件操作
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            print(f"Error reading file: {e}")
            return None

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return True
        except IOError as e:
            print(f"Error writing file: {e}")
            return False

    def copy_file(self, src, dst):
        try:
            shutil.copy(src, dst)
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False

    def move_file(self, src, dst):
        try:
            shutil.move(src, dst)
            return True
        except Exception as e:
            print(f"Error moving file: {e}")
            return False

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

    # 系统信息
    def get_system_info(self):
        info = {
            'platform': platform.system(),
            'python_version': sys.version,
            'os_release': platform.release(),
            'cpu_count': os.cpu_count(),
            'memory_info': psutil.virtual_memory()._asdict()
        }
        return info

    # 进程管理
    def kill_process(self, process_id):
        try:
            process = psutil.Process(process_id)
            process.terminate()
        except Exception as e:
            print(f"Error killing process: {e}")

    # 网络工具
    def list_directory(self, path):
        try:
            return os.listdir(path)
        except Exception as e:
            print(f"Error listing directory: {e}")
            return None

    # 时间与日期
    def get_current_datetime(self):
        return datetime.datetime.now()

    # 压缩与解压缩
    def zip_directory(self, src, dst):
        try:
            with zipfile.ZipFile(dst, 'w') as zipf:
                for root, dirs, files in os.walk(src):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(src, '..')))
            return True
        except Exception as e:
            print(f"Error zipping directory: {e}")
            return False

    def unzip_file(self, src, dst):
        try:
            with zipfile.ZipFile(src, 'r') as zipf:
                zipf.extractall(dst)
            return True
        except Exception as e:
            print(f"Error unzipping file: {e}")
            return False

    # 数据库操作
    def create_sqlite_db(self, db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT)")
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating SQLite database: {e}")
            return False

    # HTTP客户端
    def send_network_request(self, url, method='GET', data=None):
        try:
            if method.upper() == 'GET':
                response = requests.get(url)
            elif method.upper() == 'POST':
                response = requests.post(url, data=data)
            else:
                raise ValueError("Unsupported HTTP method")
            return response.text
        except Exception as e:
            print(f"Error sending network request: {e}")
            return None

    # 命令行工具
    def execute_command(self, command):
        try:
            return subprocess.check_output(command, shell=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None
    #ssh
    def ssh_connect(self, hostname, port, username, password):
        """建立SSH连接并返回SSH客户端对象"""
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port, username, password)
            return client
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except paramiko.SSHException as sshException:
            print(f"Could not establish SSH connection: {sshException}")
        except Exception as e:
            print(f"Error connecting to host {hostname}: {e}")
        return None

    def ssh_execute_command(self, ssh_client, command):
        """在远程主机上执行命令"""
        if ssh_client is None:
            print("SSH client is not connected.")
            return None

        try:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            result = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            if result:
                print("Command output:")
                print(result)
            if error:
                print("Error output:")
                print(error)
            return result
        except Exception as e:
            print(f"Error executing command: {e}")
            return None

    def ssh_disconnect(self, ssh_client):
        """关闭SSH连接"""
        if ssh_client is not None:
            ssh_client.close()
    #web
    def start_http_server(self, port=8000):
        """启动一个简单的HTTP服务器监听指定端口"""
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()

    def start_flask_app(self, port=8000):
        """启动一个Flask应用监听指定端口"""
        app = Flask(__name__)

        @app.route('/')
        def index():
            return 'Hello, World!'

        app.run(host='0.0.0.0', port=port)
   # ...（此处省略其他方法）

# ...（此处省略其他原有代码）
