import psutil
import sys
import os
from time import sleep

count = 0
processToCheck = 't-rex'
sleepTime = 24
countMaximum = 5

def processInList(process):
	for p in psutil.process_iter():
		if process in p.name().lower():
			return True
		else:
			continue
	return False

while count < countMaximum:
	if processInList(processToCheck):
		count = 0
		print(f'Found {processToCheck}, sleeping for another {sleepTime}, count is {count}/{countMaximum}')
		sleep(sleepTime)
	else:
		count += 1
		print(f'Did not find {processToCheck} count is now: {count}/{countMaximum}')
		print(f'Sleeping for {sleepTime}')
		sleep(sleepTime)
else:
	print(f'Count hit: {countMaximum}, restarting PC.')
	os.system("shutdown -t 0 -r -f")