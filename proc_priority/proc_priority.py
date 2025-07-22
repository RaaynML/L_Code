import sys
import os
import psutil
#based on https://code.activestate.com/recipes/496767/
import win32api,win32process,win32con

"""
IDLE				= 1
BELOW_NORMAL	= 5
NORMAL			= 7
ABOVE_NORMAL	= 6
HIGH				= 10
REALTIME			= ?
"""
PRIORITY = {
	None: None, #shrug
	"None": None,
	"": None,
	"LOW": psutil.IDLE_PRIORITY_CLASS,
	"IDLE": psutil.IDLE_PRIORITY_CLASS,
	"BELOWNORMAL": psutil.BELOW_NORMAL_PRIORITY_CLASS,
	"BELOW_NORMAL": psutil.BELOW_NORMAL_PRIORITY_CLASS,
	"NORMAL": psutil.NORMAL_PRIORITY_CLASS,
	"ABOVE_NORMAL": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
	"ABOVENORMAL": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
	"HIGH": psutil.HIGH_PRIORITY_CLASS
	#,"REALTIME": psutil.REALTIME_PRIORITY_CLASS #? not available
}

IOPRIO = {
	None: None,
	"None": None,
	"": None,
	"VERY_LOW": psutil.IOPRIO_VERYLOW,
	"VERYLOW": psutil.IOPRIO_VERYLOW,
	"LOW": psutil.IOPRIO_LOW,
	"NORMAL": psutil.IOPRIO_NORMAL,
	"HIGH": psutil.IOPRIO_HIGH #? if available
}

priority_list = [];
with open("list.csv",'r') as priority_file:
	flines = priority_file.readlines(); #get as a list
	priority_list = flines.sort();

#for skipping
sorted_proc_list = sorted(psutil.process_iter(attrs=['name']), key=lambda p: p.info['name'] or "")

def setProcessPriority(pname,benice=None,ionice=None):
	"""
		Either priority type is optional.
		TODO: skip more, faster.
	"""
	for proc in sorted_proc_list: #loop in python ew
		try: #Don't die if permission denied
			cname = proc.info['name']
			if pname > cname:
				continue
			elif pname == cname:
				if PRIORITY[benice] is not None:
					proc.nice(PRIORITY[benice])
				if IOPRIO[ionice] is not None:
					proc.ionice(IOPRIO[ionice])
			else: #pname < proc.name():
				break #passed matching target, give up
		except:
			print(f"\n[!] Permission denied for {pname}\n")


def splitLines(the_text):		#TODO placeholder
	return the_text.split(",")

if __name__ == "__TEST_TODO__":
	for line in priority_list:		#TODO placeholder
		try:
			splitLines(line)
		except:
			break
##

if __name__ == "__main__":  #Example
	setProcessPriority("Discord.exe","IDLE","VERYLOW")
	setProcessPriority("librewolf.exe","IDLE","VERYLOW")
	setProcessPriority("obs-browser-page.exe",None,"LOW")
	setProcessPriority("pwsh.exe","IDLE","VERYLOW")
