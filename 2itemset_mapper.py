#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = re.findall(r"[\'A-Za-z0-9]+", line)
	# increase counters
	#print(words)
	for word1 in words:
		#print("test1")
		for word2 in words:
			#print("test2")
			if int(word1) != int(word2) and int(word1) < int(word2):
				print('%s\t%s\t%s' % (word1,word2,1))
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		#print('%s\t%s' % (word, 1))
