#!/usr/bin/env python

import sys
import re

_3itemsets_s2 = []
retail = []
f = open('candidates', 'r')
#for l in f:
#	cache_line = f.readline()
#	_3itemsets_s2.append(cache_line)

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	retail.append(line)
	
while True:	
	try:
		iA, iB, iC = f.readline().strip().split('\t')
		if int(iA) != 0:
			for line in retail:
				line = line.strip()
				# split the line into words
				words = re.findall(r"[\'A-Za-z0-9]+", line)
				# increase counters
				count = 0
				for word in words:
					if word == iA:
						count = count + 1
					elif word == iB:
						count = count + 1
					elif word == iC:
						count = count + 1
				
				if count == 3:
					print('%s\t%s\t%s\t%s' % (iA, iB, iC, '1'))
			#print('%s\t%s\t%s' % (iA, iB, iC))
	except ValueError:
		break