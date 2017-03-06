#!/usr/bin/env python

import sys

hash_table = {}

for line in sys.stdin:
	line = line.strip()
	#print(line)
	itemA, itemB, itemC, value = line.split('\t')
	itemset = itemA + '-' + itemB + '-' +itemC
	try:
		hash_table[itemset] = int(hash_table[itemset]) + int(value)
	except KeyError:
		hash_table[itemset] = int(value)
	
for i in hash_table:
	if hash_table[i] >= 1000:
		iA, iB, iC = i.strip().split('-')
		print('%s\t%s\t%s' % (iA, iB, iC ))