import sys
import os
from dataclasses import dataclass
import psutil
#based on https://code.activestate.com/recipes/496767/
import win32api,win32process,win32con

PRIORITY = {
	None: None,
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
	None: None, #shrug pt.II
	"None": None,
	"": None,
	"VERY_LOW": psutil.IOPRIO_VERYLOW,
	"VERYLOW": psutil.IOPRIO_VERYLOW,
	"LOW": psutil.IOPRIO_LOW,
	"NORMAL": psutil.IOPRIO_NORMAL,
	"HIGH": psutil.IOPRIO_HIGH #if available
}

@dataclass
class t_priority:
	name: str
	nice: type(PRIORITY)
	ionice: type(IOPRIO)

priority_list = [];
with open("list.csv",'r') as list_file:
	if list_file is not None:
		flines = sorted(list_file.readlines()[1:]); #skip example/title
		for cline in flines:
			if(cline[0] == '#'): #skip comment
				continue
			seg = cline.split(",");
			try:
				#ignore newlines
				if(seg[2][-2]) == '\r\n':
					seg[2] = seg[2][:-2]
				if(seg[2][-1]) == '\n':
					seg[2] = seg[2][:-1]
				
				priority_list.append(t_priority( seg[0], PRIORITY[seg[1]], IOPRIO[seg[2]] ));
			except:
				print(f"\b\n(!) Invalid priority value:\n{seg}\nMoving on...")
	#fi
#close

#for skipping
sorted_proc_list = sorted(psutil.process_iter(attrs=['name']), key=lambda p: p.info['name'] or "")

def setPriorityTyped(opt:t_priority): #for CSV
	for proc in sorted_proc_list: #python loops ew
		try: #Don't die if permission denied
			cname = proc.info['name']
			if opt.name > cname:
				continue
			elif opt.name == cname:
				if opt.nice is not None:
					proc.nice(opt.nice)
				if opt.ionice is not None:
					proc.ionice(opt.ionice)
			else: #opt.name < proc.name():
				break #passed matching target, give up
		except:
			print(f"\b\n(!) Permission denied: {opt.name}\nMoving on...")

def setPriority(pname:str,benice:str,ionice:str): #for API
	#Either priority type is optional
	setPriorityTyped(t_priority( pname, PRIORITY[benice], IOPRIO[ionice] ))


if __name__ == "__main__": 
	for ep in priority_list:
		setPriorityTyped(ep)
