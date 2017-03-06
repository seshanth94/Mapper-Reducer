#!/usr/bin/env python

import sys
	
_3itemsets_s1 = []
_2itemsets = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	try:
		word1, word2, word3 = line.split('\t')
		s = str(word1)+str('-')+str(word2)
		_3itemsets_s1.append([s,word3])
	except ValueError:
		word1, word2 = line.split('\t')
		s1= str(word1)+str('-')+str(word2)
		_2itemsets[s1]=1
		continue	

#print(_3itemsets_s1)
#print("over")
#print(_2itemsets)

for item in _3itemsets_s1:
	try:
		if _2itemsets[item[0]] == 1:
			iB, iC = item[0].split('-')
			print('%s\t%s\t%s' % (item[1],iB,iC))
	except KeyError:
		continue