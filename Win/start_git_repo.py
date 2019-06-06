import sys
import os
from getpass import getpass
from github import Github
from colorama import init, Fore, Style

init(convert = True)

username = ""
psd = ""

repo_name = sys.argv[1]

if not os.path.isfile(sys.argv[3]+'\creds'):
	print(Fore.YELLOW + "Your GitHub credentials will be stored for future use.\nYou will be prompted whether you'd like to use this account every time.\n" + Style.RESET_ALL)

	username = input("Enter your GitHub username: ")
	psd = getpass("Enter your GitHub password: ")

	with open(sys.argv[3]+'\creds','w') as creds:
		creds.write(username+";,;"+psd)
else:
	with open(sys.argv[3]+'\creds','r') as creds:
		(username, psd) = creds.read().split(';,;')
	print(Fore.YELLOW + "Using GitHub account {0}.".format(username) + Style.RESET_ALL)
	ctn = input("Continue with this account? (y): ").lower()
	while not (ctn == 'y' or ctn == 'n' or ctn == ''):
		ctn = input("Continue with this account? (y): ").lower()
	if ctn == 'n':
		print(Fore.YELLOW + "\nYour GitHub credentials will be stored for future use.\nYou will be prompted whether you'd like to use this account every time.\n" + Style.RESET_ALL)

		username = input("Enter your GitHub username: ")
		psd = getpass("Enter your GitHub password: ")

		with open(sys.argv[3]+'\creds','w') as creds:
			creds.write(username+";,;"+psd)

remote_name = repo_name

if(sys.argv[2] == 'getip'):
	remote_name = input("Please enter remote name (%s): " % remote_name)
	if(remote_name == ""):
		remote_name = repo_name

user = Github(username, psd).get_user()
repo = user.create_repo(remote_name)
print("Created remote repository {0} on GitHub in the account {1}.".format(remote_name,username))

os.system('add_origin '+username+" "+remote_name)