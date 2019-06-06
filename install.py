import os
from platform import system
from colorama import init, Fore, Style
from distutils.dir_util import copy_tree

init(convert = True)

OSTYPE = system()

if OSTYPE == 'Windows':
	# Install on Windows
	LIBPATH = "C:/Users/"+os.getlogin()+'/GitProject'
	if os.path.isdir(LIBPATH):
		print(Fore.RED+LIBPATH+" already exists."+Style.RESET_ALL)
	else:
		os.mkdir(LIBPATH)
		cf = copy_tree('./Win',LIBPATH)
		if len(cf) == 4:
			print(Fore.GREEN+"GitProject has been installed successfully!"+Style.RESET_ALL)
			print('In order to access GitProject from anywhere, add "'+LIBPATH+'" to PATH.')
			print(Fore.GREEN+'\nUsage:'+Style.RESET_ALL+'\nGitProject projectFolder [remoteRepo]\n(OR)\nNGP projectFolder [remoteRepo]\n\n'+Fore.YELLOW+'If remoteRepo isn\'t specified, you will be prompted for it later.'+Style.RESET_ALL)
			print(Fore.RED+'\nIf you don\'t add the directory to PATH, you can specify the full path when you use GitProject.'+Style.RESET_ALL)
		else:
			print(Fore.RED+"Some error occurred while installing GitProject."+Style.RESET_ALL)
elif OSTYPE == 'Linux':
	# Install on Linux
	i = 1
elif OSTYPE == 'Darwin':
	# Install on Mac
	i = 1
else:
	print(Fore.RED+"Sorry, your OS isn't recognized.\n"+Fore.GREEN+"This software currently works on Windows, Linux and Mac only."+Style.RESET_ALL)