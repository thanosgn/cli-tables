# This Python file uses the following encoding: utf-8
from __future__ import print_function
import sys, re

def hline(max_length, double = False):
	if double == False:
		dashes = '-' * max_length
	else:
		dashes = '=' * max_length
	for i in range(0,rows):
		print('+', end="")
		print(dashes, end="")
	print('+')

lines = [re.split("\t+",line.replace("    ","\t").rstrip('\n')) for line in sys.stdin]
rows = len(lines[0])

double_hline = double_vline = False

if("-h" in sys.argv):
	double_hline = True
if("-v" in sys.argv):
	double_vline = True

max_length=0
for line in lines:
	for element in line:
		length = len(element)
		if length > max_length:
			max_length = length

max_length += 2

hline(max_length)
for i in range(0,len(lines)): 
# for line in lines: 
	line = lines[i]
	print('|', end="")
	for j in range(0,len(line)):
		element = line[j]
		length = len(element)
		blank_space = max_length - length
		left = (blank_space / 2 )
		right = blank_space - left
		print(' '*left, end="")
		print(element, end="")
		if j==0 and double_vline:
			print(' '*right, end='‖')
		else:
			print(' '*right, end='|')
	print()
	hline(max_length, (i==0 and double_hline))

