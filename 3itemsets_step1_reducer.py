#!/usr/bin/env python

import sys

prev_val = None
prev_item1 = None
prev_item2 = None


_2itemsets = []
for line in sys.stdin:
	line = line.strip()
	key, joiner = line.split('\t')
	_2itemsets.append([key,joiner])
	
_2itemsets_dup = list(_2itemsets)
	
for entry in _2itemsets:
	outer_val = entry[1]
	prev_val = None
	prev_item1 = None
	prev_item2 = None
	for entry_inner in _2itemsets_dup:		
		if entry_inner[1] == outer_val:
			item1, item2 = entry_inner[0].split('-')
			#print(entry_inner)
			if prev_val == outer_val:
				print('%s\t%s\t%s' % (prev_item2, item2, outer_val))
			elif entry_inner[1] == outer_val:
				#print(entry_inner)
				prev_val = outer_val
				prev_item1 = item1
				prev_item2 = item2
				entry_inner[1] = None
			else:	
				break

