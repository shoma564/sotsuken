import os, shutil, time, glob

def shoki():
	os.system('./template/reset.sh')
	print("初期化を終えました。情報を入力してください\n\n")


def install():
	docker = shutil.which("docker")
	docker = str(docker)
	if docker == "None":
		os.system('apt -y update')
		os.system('apt -y install docker')

	dockerc = shutil.which("docker-compose")
	dockerc = str(dockerc)
	if dockerc == "None":
		os.system('apt -y update')
		os.system('apt -y install docker-compose')

def scan():
	file_name = "./ubuntunmap/sh/script.sh"
	while True:
		print("スキャンの対象は複数ホストですか？yes or no")
		kai = input(">>> ")
		if kai == "yes":
			print("マルチノードのスキャンを行います。スキャン対象のネットワークアドレスを入力してください。CIDR形式でサブネットの入力をしてください。")
			scanip = input(">>>")
			with open(file_name, encoding="cp931") as f:
                                data_lines = f.read()
			data_lines = data_lines.replace("0.0.0.0", scanip)
			with open(file_name, mode="w", encoding="cp932") as f:
				f.write(data_lines)
			break

		elif kai == "no":
			print("シングルノードのスキャンを行います。スキャン対象のIPアドレスを入力してください。サブネットの入力は必要ありません。")
			scanip = input(">>>")
			with open(file_name, encoding="cp932") as f:
				data_lines = f.read()
			data_lines = data_lines.replace("0.0.0.0", scanip)
			with open(file_name, mode="w", encoding="cp932") as f:
				f.write(data_lines)

			print("User名の入力")
			sshuser = input(">>>")

			with open("./ubpy/python_hon/sc.py") as f:
				data_lines = f.read()
				data_lines = data_lines.replace("qwertyuser", sshuser)

			with open("./ubpy/python_hon/sc.py", mode="w", encoding="utf-8") as f:
				f.write(data_lines)

			print("Passwordの入力")
			sshpass = input(">>>")

			with open("./ubpy/python_hon/sc.py") as f:
				data_lines = f.read()
				data_lines = data_lines.replace("qwertypass", sshpass)

			with open("./ubpy/python_hon/sc.py", mode="w", encoding="utf-8") as f:
				f.write(data_lines)

			break
		else:
			print("予期せぬ入力がありました。再実行します")


def docker():
	os.system('docker-compose build')
	os.system('docker-compose up -d')



###### ./share/result.txtが出来上がるまで、無限ループで参照し続ける。もし、存在が確認されたら、処理終了。

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
			print("ファイルが作成されました")
			if is_size != 0:
				os.system('cat ./share/result.txt')
				break
		else:
			pass
		print("サービスのスキャン中")
		time.sleep(5)





install()
scan()
docker()
result_exist()
