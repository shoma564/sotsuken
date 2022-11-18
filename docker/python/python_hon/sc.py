import paramiko
import time
import paramiko
import socket


with paramiko.SSHClient() as client:

    HOSTNAME = '172.24.20.125'
    USERNAME = 'shoma'
    PASSWORD = 'hiyiir'
    LINUX_COMMAND = 'pwd'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)
    # 2. 公開鍵認証方式
    #client.connect(hostname=HOSTNAME, port=22, username=USERNAME, key_filename=KEY_FILENAME)
    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
    for line in stdout:
        print(line, end='')

    time.sleep(1)
    LINUX_COMMAND = 'uname -a'
    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
    for line in stdout:
        print(line, end='')


    time.sleep(1)
    LINUX_COMMAND = 'cat /etc/os-release'
    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
    for line in stdout:
        print(line, end='')


    time.sleep(1)
    LINUX_COMMAND = 'hostname'
    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
    for line in stdout:
        print(line, end='')



for port in range(1,1023):
    #target_host のポート番号portに接続を試行
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((HOSTNAME, port))
    sock.close()
    #socket.connect_ex は成功すると0を返す
    if result == 0:
        print("Port %d open!" % (port))
