#Binary-search Insertion Sort
#Use binary search to locate the insertion position. Does it reduce comparisons? Does it reduce shifts? Does worst-case total
#time improve beyond O(n^2)?

'''
Binary-search Insertion Sort:

Reduces comparisons from O(n) per insertion to O(log n).
Does not reduce shifts; they can still be O(n) per insertion.
Does not improve worst-case total time beyond O(n²).
It can still be practically faster when comparisons are expensive, because it performs fewer comparisons.
'''
