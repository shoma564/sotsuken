import time, paramiko
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
hostip = ""
mysqluser = ""
mysqlname = ""
mysqlpass = ""



print("検出サービスの整理中")

for number in range(6):
	time.sleep(0.5)
	print(".")
print("\n\n")

#================================== サービスの検出 =========================================
def check_mysql():
    with open('./share/mg_result.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'mysql' in line:
            return True
    return False


def check_nginx():
    with open('./share/mg_result.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'nginx' in line:
            return True
    return False


def check_apache():
    with open('./share/mg_result.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'apache' in line:
            return True
    return False


#==================================== サービスの移行 =======================================================
def syu():
    global HOSTNAME, USERNAME, PASSWORD

    print("移行先の情報を収集します。")
    print("移行先ホストのIPアドレスを入力")
    HOSTNAME = input(">>> ")
    print("移行先ホストのユーザー名")
    USERNAME = input(">>> ")
    print("パスワードの入力")
    PASSWORD = input(">>> ")


def mysql():
    global HOSTNAME, USERNAME, PASSWORD, hostip, mysqluser, mysqlname, mysqlpass
    print("mysqlの移行を開始します。")
    print("mysqlが動いているIPアドレス")
    hostip = input(">>> ")
    print("mysqlデータベースのユーザー名")
    mysqluser = input(">>> ")
    print("移行するデータベース名")
    mysqlname = input(">>> ")
    print("パスワードを入力する")
    mysqlpass = input(">>> ")
    mycommand1 = "mysqldump -u" + str(mysqluser) + " -p" + str(mysqlpass) + " -r" + str(mysqlname) + " -h" + str(hostip) + " --single-transaction " + str(mysqlname)
    print(mycommand1)

    with paramiko.SSHClient() as client:

        LINUX_COMMAND = "apt -y update && apt -y install mysql-server && apt -y install mysql-client-core-8.0"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(100)

    with paramiko.SSHClient() as client:

        LINUX_COMMAND = mycommand1

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)

    with paramiko.SSHClient() as client:

        LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -h " + str(HOSTNAME) + "-e create database " + str(mysqlname) 

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')


    with paramiko.SSHClient() as client:

        LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -h " + str(HOSTNAME) + " < " + str(mysqlname)
        print(LINUX_COMMAND)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')




#======================================= main ===============================================================
syu()
check_mysql()
check_nginx()
check_apache()



if check_mysql():
    print('Mysql_True')
    mysql()
else:
    print('Mysql_False')

if check_nginx():
    print('nginx_True')
    nginx()
else:
    print('nginx_False')

if check_apache():
    print('apache_True')
    apache()
else:
    print('apache_False')
