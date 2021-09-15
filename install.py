#!/usr/bin/python

import os, sys, subprocess

def install():
	n = os.system("which nmap>/dev/null")
	if n == 0:
		print ("[+] Nmap        Installed [✔]")
	else:
		print ("[+] Nmap        Not Installed [✗] ")
		print("")
		print("Installing nmap ....")
		time.sleep(2)
		os.system("sudo apt-get install nmap", shell=True)

		#///
	n = os.system("which netdiscover>/dev/null")
	if n == 0:
		print ("[+] Netdiscover        Installed [✔]")
	else:
		print ("[+] Netdiscover        Not Installed [✗] ")
		print("")
		print("Installing Netdiscover ....")
		time.sleep(2)
		os.system("sudo apt-get install Netdiscover", shell=True)

install()

