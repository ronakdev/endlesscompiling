import os
import random

percentage = 0
while (True):
	os.system("clear")
	os.system("echo Starting to Compile")
	os.system("sleep 2")
	os.system("echo Compiling Base Files ...")
	while (True):
		cmd = "echo Progress: " + `percentage` + "%"
		os.system(cmd)
		ran =  random.randint(1,4)
		cmd = "sleep " + `ran`
		os.system(cmd);
		percentage += ran	
		if (percentage >= 101):
			os.system("echo Base Compilation Complete")
			break
	percentage = 0
	os.system("echo Compiling Internals")
	while (True):
		cmd = "echo Progress: " + `percentage` + "%"
		os.system(cmd)
		ran =  random.randint(1,4)
		cmd = "sleep " + `ran`
		os.system(cmd);
		percentage += ran	
		if (percentage >= 101):
			os.system("echo Internal Compilation Complete")
			break
	os.system("echo Compilation Failed, Trying Again")
#os.system("echo Compilation Complete")