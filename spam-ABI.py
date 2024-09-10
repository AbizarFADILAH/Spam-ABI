import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
__  ___	__  __ __    __  __ __	__  __  
/' _/| _,\/  \|  V  | /' _/|  V  |/' _/ 
`._`.| v_/ /\ | \_/ | `._`.| \_/ |`._`. 
|___/|_| |_||_|_| |_| |___/|_| |_||___/\
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		;       Author : ABIZAR     ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

NOTE: This tool's only work for Indonesia number phone.

1. SMS Gratis
""")
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
