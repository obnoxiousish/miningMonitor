import sys
import subprocess
import time

"""
Author: obnoxious
Contact: obnoxious@is.too.gay
"""

#Quick code to tell user to install psutil if not done already.

try:
	import psutil
except:
	print('pip install psutil')
	sys.exit(0)

"""

Comment this in to a list of your processes for debugging or development

for process in psutil.process_iter():
	print(process.name())

"""

class main:
	def __init__(self):
		"""
		
		This function is creating some variables to be used in our actual code.
		Our booleans will be used to monitor our state.
		Gaming list will be used to maintain a list processes that are games.
		Mining command is the command to be ran to run a miner (T-Rex)

		None

		"""
		self.mining = False
		self.gaming = False
		self.miningCommand = "t-rex.exe --coin eth --url stratum+tcp://us2.ethermine.org:4444 -u 0xa40a9B1176ee3B606D4EAB472aEbF7A2C9C1b013 -w mary -a ethash --ab-indexing -d 1 --intensity 25"
		self.gamingList = ["D2R.exe"]
		self.log('Initialized.')

		#self.log('Mining now starting....')
		#self.startMining()

		while True:
			self.log('Loop started')
			self.lowerGamingList()
			self.amIGaming()
			time.sleep(10)
			self.log('Done sleeping')
			continue
		return None

	def startMining(self):
		self.popen = subprocess.Popen(self.miningCommand.split(' '))

	def stopMining(self):
		for process in psutil.process_iter():
			if process.name() == 't-rex.exe':
				process.kill()
				continue

		return True

	def lowerGamingList(self):
		"""
		This function is for lowering the strings in the gaming list for our string comparison code.
		This function uses count integer variable to update the proper item in our gamingList as our for loop was already being used for the string.

		Returns true / false depending on success

		Boolean

		"""
		count = 0
		for string in self.gamingList:
			self.gamingList[count] = string.lower()
			count += 1

		#print(self.gamingList)

		return True

	def amIGaming(self):
		"""
		This function is a bit crazy.

		We start off by checking to see if we are gaming, if gaming is true then lets check if we are still gaming, if we are not still gaming then set gaming to False.
		
		Then if gaming is false lets check if we are gaming, we check if we are gaming by checking the process list for processes in our gaming process list variable
		If we are indeed gaming we stop mining, set mining to False and set gaming to True

		If mining and gaming is false we start mining, this is true at launch and when you are no longer gaming.

		Boolean
		"""

		#If gaming status is true we will check to see if the gaming process is still open if it is not gaming status is set to False
		if self.gaming == True:
			for process in psutil.process_iter():
				if process.name().lower() == self.processName:
					#print(process.name(), self.processName)
					self.log('were still gaming!', alert='!')
					return

		#This will only be ran if the above for loop is unable to find the gaming process
		self.gaming = False

		#if gaming status is false we will check to see if there is a gaming process in our process list
		if self.gaming == False:
			for process in psutil.process_iter():
				pname = process.name().lower().strip().rstrip()
				if pname in self.gamingList:
					self.processName = process.name().lower().strip().rstrip()
					self.log(f"{self.processName} is running & in the gaming list!", alert="!")
					self.log('We are gaming: Closing miner.......')
					self.stopMining()
					self.mining = False
					self.gaming = True
		
		#by default mining and gaming status are false so this will launch the miner on start and when the status variables are both set back to false
		if self.mining == False and self.gaming == False:
			self.log('Mining is false and gaming is false, starting miner.')
			self.startMining()
			self.log('Miner started.')
			self.mining = True
			self.gaming = False
			return
		
		elif self.mining == True and self.gaming == False:
			self.log('I am already mining so I will not start a new one.')

		return

	def log(self, msg, alert='+'):
		print(f'[{alert}] {msg}')


if __name__ == "__main__":
	main()