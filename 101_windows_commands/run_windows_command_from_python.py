## get subprocess module
import subprocess

## call command ##
p = subprocess.Popen("ping www.google.com", stdout=subprocess.PIPE, shell=True)

## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
#Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument
#should be a string to be sent to the child process, or None, if no data should be sent to the child.
(output, err) = p.communicate()

## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
print ("Command output : ", output)
print ("Command exit status/return code : ", p_status)


print ("------------------------------------------")

## call command ##
p = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True)

## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
#Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument
#should be a string to be sent to the child process, or None, if no data should be sent to the child.
(output, err) = p.communicate()

## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
print ("Command output : ", output)
print ("Command exit status/return code : ", p_status)

