import time

print("検出サービスの整理中")

for number in range(6):
	time.sleep(0.5)
	print(".")
print("\n\n")

==================================サービスの検出=========================================
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


====================================サービスの移行=======================================================
def mysql():
    print("mysqlの移行を開始します。")
    print("mysqlデータベースのユーザー名")
    mysqluser = input()
    print("移行するデータベース名")
    mysqlname = input()
    print("パスワードを入力する")
    mysqlpass = input()

======================================================================================================

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
