import sys
import subprocess

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
		self.miningCommand = "mine.bat"
		self.gamingList = ["CocKS.eXe", "D2R.exe"]
		self.log('Initialized.')


		self.lowerGamingList()
		self.amIGaming()

		return None

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
		We check and iter through the available processes, lowercase the capitals and then check if it is in the gaming list

		returns True / False depending on success

		Boolean
		"""
		for process in psutil.process_iter():
			processName = process.name().lower().strip().rstrip()
			if processName in self.gamingList:
				self.log(f"{processName} is running & in the gaming list!", alert="!")
				self.log('We are gaming: Closing T-Rex....')
			else:
				pass
				#self.log(f"{processName} is NOT in the gaming list!")

		return True

	def log(self, msg, alert='+'):
		print(f'[{alert}] {msg}')
if __name__ == "__main__":
	main()