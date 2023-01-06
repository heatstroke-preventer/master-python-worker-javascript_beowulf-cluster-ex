import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("8.8.8.8", username = "master", pkey="12345678")
ssh.exec_command("node [자바스크립트 명령어]")