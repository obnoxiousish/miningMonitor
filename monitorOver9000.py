import psutil
import sys
from time import sleep

count = 0
processToCheck = 't-rex'
sleepTime = 5
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
	sys.exit(0)