#!/usr/bin/python
import re
import argparse

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

''' Initial a counter and list to hold results '''
linecount = 0
foundit = []

''' Search each line of the file and return a list of line numbers 
    that match the pattern. There could be multiple returns. '''
for line in lines:
    line = line.strip()
    if p.search(line):
        foundit.append(linecount)
    linecount = linecount + 1

''' Print results padded with before and after lines until newlines are found '''
for x in foundit:
    # Determine start position by taking line number (x), subtract 1 and test
    # for a blank line.
    k = x
    while lines[k] not in ['\n', '\r\n']:
        startposition = k
        k = k - 1

    # Print starting with line number startposition, advance line number by 1
    # and test for blank line. If not blank, print. If blank, stop. If EOF,
    # stop.
    print '\n'
    k = startposition
    while lines[k] not in ['\n', '\r\n']:
        print lines[k].strip()
        k = k + 1
        if lines[k] == lines[-1]:
            break

args.infile.close()

