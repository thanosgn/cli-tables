# This Python file uses the following encoding: utf-8
from __future__ import print_function
import sys, re

def hline(max_length, columns, double = False):
    if double == False:
        dashes = '-' * max_length
    else:
        dashes = '=' * max_length
    for i in range(0, columns):
        print('+', end="")
        print(dashes, end="")
    print('+')

def print_table(lines, double_hline=False, double_vline=False):
    columns = len(lines[0])
    max_length=0
    for line in lines:
        for element in line:
            length = len(element)
            if length > max_length:
                max_length = length

    max_length += 2 

    hline(max_length,columns)
    for i in range(0,len(lines)):
    # for line in lines:
        line = lines[i]
        print('|', end="")
        for j in range(0,len(line)):
            element = line[j]
            length = len(element)
            blank_space = max_length - length
            left = int((blank_space / 2 ))
            right = blank_space - left
            print(' '*left, end="")
            print(element, end="")
            if j==0 and double_vline:
                print(' '*right, end='‖')
            else:
                print(' '*right, end='|')
        print()
        hline(max_length, columns, (i==0 and double_hline))

def main():
    lines = [re.split("\t+",line.replace("    ","\t").rstrip('\n')) for line in sys.stdin]
    print_table(lines, ("-h" in sys.argv), ("-v" in sys.argv))

if __name__ == "__main__":
    main()
