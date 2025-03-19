import sys
import os
import psutil
#based on http://code.activestate.com/recipes/496767/
import win32api,win32process,win32con

#sorting enabels skipping loop
proc_sorted_list = sorted(psutil.process_iter(attrs=['name']), key=lambda p: p.info['name'] or "")

def setProcessPriority(pname,benice):
	ff_matched = None
	for proc in proc_sorted_list:
		if pname > proc.info['name']:
			continue
		elif pname == proc.name():
			proc.nice(benice)
		elif pname < proc.name() :
			break #alphabetically past the name of the exe
#test
if __name__ == "__main__":
	setProcessPriority("firefox.exe",psutil.BELOW_NORMAL_PRIORITY_CLASS)
	setProcessPriority("notepad++.exe",psutil.IDLE_PRIORITY_CLASS)
	exit(0) #I don't remember what this fixes & I don't have time to figure it out
