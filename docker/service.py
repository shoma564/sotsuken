import time, paramiko, scp
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
hostip = ""
mysqluser = ""
mysqlname = ""
mysqlpass = ""
aphostip = ""
appass = "" 
apuser = ""


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

    print("\n\n\nmysqlの移行を開始します。")
    print("mysqlが動いているIPアドレス")
    hostip = input(">>> ")
    print("mysqlデータベースのユーザー名")
    mysqluser = input(">>> ")
    print("移行するデータベース名")
    mysqlname = input(">>> ")
    print("パスワードを入力する")
    mysqlpass = input(">>> ")
    mycommand1 = "mysqldump -u" + str(mysqluser) + " -p" + str(mysqlpass) + " -r/etc/" + str(mysqlname) + " -h" + str(hostip) + " --single-transaction " + str(mysqlname)
    print(mycommand1)

    with paramiko.SSHClient() as client:

        LINUX_COMMAND = "apt -y update && apt -y install mysql-server && apt -y install mysql-client-core-8.0"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)

    with paramiko.SSHClient() as client:

        LINUX_COMMAND = LINUX_COMMAND = "wget https://raw.githubusercontent.com/shoma564/sotsuken/main/docker/template/app/mysqld.cnf?token=GHSAT0AAAAAAB3B4MU7PCHQFSUEF7YOEPHMY6LU6LQ -O /etc/mysql/mysql.conf.d/mysqld.cnf && sleep 1 && service mysql restart"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)



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

        #LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -h " + str(HOSTNAME) + " -e create database " + str(mysqlname)
        if mysqluser == "root" or mysqlpass == "":
            LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -e \"create database " + str(mysqlname) + "\""
        else:
            LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -e \"create database " + str(mysqlname) + "\""

        print(LINUX_COMMAND)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)

    with paramiko.SSHClient() as client:

        #LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -h " + str(HOSTNAME) + " < " + str(mysqlname)
        if mysqluser == "root" or mysqlpass == "":
            LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -D " + str(mysqlname) + " < /etc/" + str(mysqlname)
        else:
            LINUX_COMMAND = "mysql -u " + str(mysqluser) + " -p " + str(mysqlpass) + " -h " + str(HOSTNAME) + "-D " + str(mysqlname) + " < " + "/etc/" + str(mysqlname)
        print(LINUX_COMMAND)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)


def apache():
    global HOSTNAME, USERNAME, PASSWORD, aphostip, appass, apuser

    print("apacheの移行を開始します。")
    print("apacheが動いているIPアドレス")
    aphostip = input(">>> ")
    print("apacheが動いているホストのユーザー")
    apuser = input(">>>")
    print("apacheが動いているホストのパスワード")
    appass = input(">>> ")

        with paramiko.SSHClient() as client:
        LINUX_COMMAND = "apt -y update && apt -y install ufw apache2 && sleep3 && ufw allow 'Apache' && systemctl restart apache2"
        print(LINUX_COMMAND)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)

        with paramiko.SSHClient() as client:
        LINUX_COMMAND = "zip -r /var/www.zip /var/www"
        print(LINUX_COMMAND)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=aphostip, port=22, username=apuser, password=appass)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)


        with paramiko.SSHClient() as client:
        LINUX_COMMAND = "zip -r /etc/apache2/sites.zip /etc/apache2/sites-available/"
        print(LINUX_COMMAND)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=aphostip, port=22, username=apuser, password=appass)

        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)




#======================================= main ===============================================================
syu()
check_mysql()
check_nginx()
check_apache()



if check_mysql():
    print('Mysql_True:Mysqlが検出されました')
    mysql()
else:
    print('Mysql_False:Mysqlが検出されませんでした')

if check_nginx():
    print('nginx_True:nginxが検出されました')
    nginx()
else:
    print('nginx_False:nginxが検出されませんでした')

if check_apache():
    print('apache_True:Apacheが検出されました')
    apache()
else:
    print('apache_False:Apacheが検出されませんでした')
