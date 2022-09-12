import subprocess

def run(cmd):
		completed = subprocess.run(["powershell", "-Command", cmd], shell=True)
		return completed

def rerunprompt():
	loop = input("Run another command? Y/N: ")
	if loop == "Y":
		proc()
	elif loop == "N":
		exit()
	else:
		print("Please type Y or N")
		rerunprompt()

def proc():
	command = input("Enter your powershell command: ")
	commandRun = run(command)
	if commandRun.returncode != 0:
		print("An error occured: %s", commandRun.stderr)
	else:
		print("Command executed successfully!")
	rerunprompt()

if __name__ == '__main__':
	proc()