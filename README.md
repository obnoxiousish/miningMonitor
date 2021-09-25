# miningMonitor in python3 for T-Rex

## Whats it do

This software on launch will open t-rex and start mining for you, once it finds a process you've manually entered in self.gamingList it will stop mining until the process closes and then it will resume mining.

## Information

This could probably be easily edited into working for other mining software. Only tested with T-Rex. 
I developed this using windows, could imagine it would work on GNU/Linux & Mac OS X as well.

## How-to
	cd ~
	git clone https://github.com/obnoxiousish/miningMonitor
	cd miningMonitor
	python miningMonitor.py

### Easier
	Install Sublime Merge https://www.sublimemerge.com/download_thanks?target=win-x64
	clone https://github.com/obnoxiousish/miningMonitor
	Then just double click the .py file

## Configuration
The only things you'll need to configure is the t-rex command in self.miningCommand, very easy to find in miningMonitor.py. You will also have to add the process names yourself, I only added diablo 2 resurrected aka D2R.exe