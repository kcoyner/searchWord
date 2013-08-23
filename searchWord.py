#!/usr/bin/python
import argparse
import re

''' A utility to search for a word in a text file. If found, returns the
complete paragraph the word was found in.

Useful in conjunction with gpg to use as a command line password manager
using a simple text file.
'''

def printparagraph(startpositions):
    '''
    Print starting with startposition (a line number) and continue
    until a blank line is encountered. If EOF is encountered, break.
    '''
    for start in startpositions:
        while lines[start] not in ['\n', '\r\n']:
            print lines[start].strip()
            start = start + 1
            if lines[start] == lines[-1]:
                break
        print '\n'

parser = argparse.ArgumentParser(description="search for a word and display the surrounding paragraph")
parser.add_argument("pattern", help="the word you wish to match")
parser.add_argument("--input", type = argparse.FileType("r"), default = "-",
                    dest = "infile", help = "the file you wish to search,\
                    defaults to stdin")
args = parser.parse_args()

''' Read each line of the file into a list '''
lines = args.infile.readlines()

''' Compile a regular expression search pattern, case insensitive '''
p = re.compile(args.pattern, re.I | re.M)

''' Search each line of the file and return a list of line numbers 
    that match the pattern. There could be multiple returns. '''
linecount = 0
founditems = []
for line in lines:
    line = line.strip()
    if p.search(line):
        founditems.append(linecount)
    linecount = linecount + 1

''' Determine start position by taking line number (item), subtract 1 and test
    for a blank line. '''
startpositions = []
for item in founditems:
    while lines[item] not in ['\n', '\r\n']:
        item = item - 1
    startpositions.append(item + 1)

printparagraph(startpositions)

args.infile.close()

