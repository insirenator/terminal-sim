'''
Basic Terminal Simulator
Created by : Shakeeb Arsalaan

'''
class Terminal:
	'''
	Terminal Implementation

	dir_tree -> Contains all the folder connections
	sys_path -> Current Directory Full Path
	cursor -> Current directory
	terminal_name -> Terminal Name 

	'''
	def __init__(self,terminal_name='MYSHELL') :
		self.dir_tree = {
			'C:' : ['users'],
			'users' : ['john','paul','vlad'],
			'john' : [],
			'paul' : [],
			'vlad' : [],
		}

		self.sys_path = ['C:']
		self.cursor = 'C:'
		self.terminal_name = terminal_name

	def HELP(self) :
		print(f"\n RECOGNISABLE COMMANDS\n{'-'*22}")
		print(f" CD <name> : {self.CD.__doc__}")
		print(f" MD <name> : {self.MD.__doc__}")
		print(f" DIR       : {self.DIR.__doc__}")
		print(f" CD/       : {self.CD_SLASH.__doc__}")
		print(f" CD..      : {self.CD_DOT.__doc__}")
		print(f" PID       : {self.PRINT_INTERNAL_DATA.__doc__}")
		print(f" EXIT      : Exit The Terminal")

	def CD(self,folder) :
		'''Change Directory'''
		if folder in self.dir_tree[self.cursor] :
			self.sys_path.append(folder)
			self.cursor = folder

		else:
			print(f"'{folder}' doesn\'t exits!'")

	def MD(self,folder) :
		'''Make Directory'''
		if folder not in self.dir_tree[self.cursor] :
			self.dir_tree[self.cursor].append(folder)
			self.dir_tree[folder] = list()

		else :
			print(f"'{folder}' already exist!")

	def DIR(self) :
		'''List Directories'''
		print('\n Folders\n -------')
		for folder in self.dir_tree[self.cursor] :
			print(' ',folder)

	def PRINT_PATH(self) :
		'''Print Full Directory Path'''
		print(f'\n{self.terminal_name} : ',end='')
		print(*self.sys_path,sep='/',end='>')

	def CD_SLASH(self) :
		'''Go To Root Directory'''
		self.sys_path = ['C:']
		self.cursor = 'C:'

	def CD_DOT(self):
		'''Switch To Parent Directory'''
		if not len(self.sys_path) == 1 :
			self.sys_path.pop()
			self.cursor = self.sys_path[-1]

	def PRINT_INTERNAL_DATA(self):
		'''Print Internal Data(Object Attributes)'''
		print()
		print(f" NAME : {self.terminal_name}")
		print(f" SYS_PATH : {'/'.join(self.sys_path)}")
		print(f" CURSOR : {self.cursor}")
		for k,v in self.dir_tree.items() :
			print(f" {k} : {v}")

	def run(self) :
		'''Terminal Driver'''
		print('-'*82)
		print("Type 'help' for help.......")
		
		while True :
			self.PRINT_PATH()
			cmd = input().lower()

			if cmd == 'exit':
				break

			elif cmd == 'help':
				self.HELP()

			elif cmd.startswith('cd ') :
				folder = cmd.split(' ')[-1]
				if len(folder) > 0 :
					self.CD(folder)
				else :
					print('Provide Folder Name!')

			elif cmd.startswith('md ') :
				folder = cmd.split(' ')[-1]
				if len(folder) > 0 :
					self.MD(folder)
				else:
					print('Provide Folder Name!')

			elif cmd == 'cd/' :
				self.CD_SLASH()

			elif cmd == 'cd..' :
				self.CD_DOT()
					
			elif cmd == 'dir' :
				self.DIR()

			elif cmd == 'pid' :
				self.PRINT_INTERNAL_DATA()

			else :
				print(f"'{cmd}' command not recognised!")