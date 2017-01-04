from __future__ import print_function
import sys

def hline(max_length):
	dashes = '-' * max_length
	for i in range(0,rows):
		print('+', end="")
		print(dashes, end="")
	print('+')

lines = [line.rstrip('\n').split('\t') for line in open(sys.argv[1])]
rows = len(lines[0])

max_length=0
for line in lines:
	for element in line:
		length = len(element)
		if length > max_length:
			max_length = length
			e = element

max_length += 2

hline(max_length)
for line in lines: 
	print('|', end="")
	for element in line:
		length = len(element)
		blank_space = max_length - length
		left = (blank_space / 2 )
		right = blank_space - left
		print(' '*left, end="")
		print(element, end="")
		print(' '*right, end='|')
	print()
	hline(max_length)
