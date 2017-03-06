# Mapper-Reducer
Frequent Itemset Mining:
We generate candidate 3-itemsets by joining frequent 2-items. If A B and A C are frequent, a candidate A B C is generated.
If A B and A C are frequent, a candidate A B C is generated. We further check if B C is frequent. If not, A B C is pruned, without scanning the transaction database. To do this, we need the output from 2 itemsets. If B C is a frequent 2-itemset the output 2 itemset reducer and the mapper for this task will produce a key-value pair using a composite key <B, C> and some special value that can indicate B C is a frequent 2-itesemt. If A B C is generated as candidate 3 itemset in the output of 3itemsetstep1, the mapper for this task will produce a key-value pair using a composite key <B,C> and value A.

Scan the transaction table to find the support count of remaining candidate 3- itemsets and report frequent 3-itsesets. The mapper will read through the transaction table. For each transaction, it will emit a key-value pair for every candidate 3-itemset contained in the transaction.

Min_sup_count was set to be 1000 for the given data set
