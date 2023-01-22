import paramiko, time, socket, os, glob

time.sleep(10)
with paramiko.SSHClient() as client:

    HOSTNAME = '0.0.0.0'
    USERNAME = 'root'
    PASSWORD = 'hiyiir'
    LINUX_COMMAND = 'pwd'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOSTNAME, port=22, username=USERNAME, password=PASSWORD)

    stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)

    for line in stdout:
        print(line, end='')

    time.sleep(1)

    with open('/etc/share/result1.txt', 'w') as f:
        LINUX_COMMAND = 'uname -a'
        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
        for line in stdout:
            print(line, end='', file=f)


        time.sleep(1)
        LINUX_COMMAND = 'cat /etc/os-release'
        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
        for line in stdout:
            print(line, end='', file=f)


        time.sleep(1)
        LINUX_COMMAND = 'hostname'
        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
        for line in stdout:
            print(line, end='', file=f)


        time.sleep(1)
        LINUX_COMMAND = 'cat /proc/meminfo | grep MemTotal'
        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
        for line in stdout:
            print(line, end='', file=f)


        time.sleep(1)
        LINUX_COMMAND = 'cat /proc/cpuinfo | grep processor'
        stdin, stdout, stderr = client.exec_command(LINUX_COMMAND)
        for line in stdout:
            print(line, end='', file=f)


def result_exist():
    path = "./share/result.txt"
    is_file = os.path.isfile(path)
    print(is_file)
    files = glob.glob("./share/*")
    while True:
        for file in files:
            print(file)
        if is_file:
            is_size = os.path.getsize(path)
            if is_size != 0:
                os.system('cat ./share/result.txt')
                print("ファイルが作成されました。")
                break
            else:
                pass

        print("マージ元ファイルの待機中")
        time.sleep(5)

    filenames = ["./share/result1.txt", "./share/result.txt"]
    with open("./share/mg_result.txt", "w") as new_file:
        for name in filenames:
            with open(name) as f:
                for line in f:
                    new_file.write(line)

                new_file.write("\n")


result_exist()
