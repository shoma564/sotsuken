import os, shutil

os.system('cd ./template && ./reset.sh')

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
			with open(file_name, encoding="cp932") as f:
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
			break
		else:
			print("予期せぬ入力がありました。再実行します")


def docker():
	os.system('docker-compose build')
	os.system('docker-compose up -d')



###### ./share/result.txtが出来上がるまで、無限ループで参照し続ける。もし、存在が確認されたら、処理終了。


install()
scan()
docker()
