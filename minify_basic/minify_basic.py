import re
from sys import argv as arglist

def minify_basic(codestream:str)->str:
	#Remove single & multi-line comments, except for in ""s
	#src https://stackoverflow.com/a/58784551
	codestream = re.sub(r"(/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/|//(?:[^\\\\]|\\\\(?:\\r?\\n)?)*?(?:\\r?\\n|$))|(\"[^\"\\\\]*(?:\\\\[\\S\\s][^\"\\\\]*)*\"|'[^'\\\\]*(?:\\\\[\\S\\s][^'\\\\]*)*'|[\\S\\s][^/\"'\\\\]*)","",codestream)
	
	#Remove whitespace around non-alphanumerics
	codestream = re.sub(r"(?<=\S)\s*([^\w\s])\s*(?=\S)",r"\1",codestream)
	
	#fix newlines around `else`
	codestream = re.sub(r"else\s*\n","else ",codestream)
	codestream = re.sub(r"\n\s*else"," else",codestream)
	
	#fix `this` following newline
	codestream = re.sub(r"\nthis"," this",codestream)
	
	#remove remaining newlines
	codestream = re.sub(r"\n","",codestream)
	
	return codestream

if len(arglist) != 2:
	print("Usage: minify_basic.py <input.js>")
	exit(1)

with open(arglist[1], "r+", encoding="utf-8") as file:
	minified = minify_basic(file.read())
	#rewrite file from start
	file.seek(0)
	file.write(minified)
	#shrinkwrap file to new size
	file.truncate()
