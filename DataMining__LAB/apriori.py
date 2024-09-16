import pandas as p
import numpy as np
import statistics

data = p.read_csv(r"C:\Users\abhis\Downloads\apriori.csv")
print(data)

import numpy as np

k = data.values.tolist()
print(k)

unique_ids = {id for i in k for id in i[1].split(',')}
iD = sorted(unique_ids)
print('\n Id is: ',iD)

id_counts = {}
for i in k:
    itemsets = i[1].split(',')
    for item in itemsets:
        if item in id_counts:
            id_counts[item] +=1
        else:
            id_counts[item] = 1
print('C1')
print(id_counts)

min_sup = 2
freq_id = {id:count for id, count in id_counts.items() if count>=min_sup}
print('L1')
print(freq_id)

from itertools import combinations
candidate_itemsets = list(combinations(freq_id.keys(),2))
itemset_counts = {}
for itemset in candidate_itemsets:
    itemset_counts[itemset] = 0
    for i in k:
        if all(id in i[1] for id in itemset):
            itemset_counts[itemset] +=1
print('C2')
print(itemset_counts)

freq_itemsets = {itemset:count for itemset, count  in itemset_counts.items() if count>=min_sup}
print("L2") 
print(freq_itemsets)

c3 = {}
for t in k:
    items = t[1].split(',')
    for c in combinations(items,3):
        if all ((c[i],c[j]) in freq_itemsets or (c[j],c[i]) in freq_itemsets for i in range(3) for j in range(i+1,3)):
            c3[c] = c3.get(c,0)+1
print(c3)

c3 = [('I1', 'I2', 'I5')]
rules=[]
for i in range(len(c3[0])):
    lhs = c3[0][:i]+c3[0][i+1:]
    rhs = c3[0][i]
    rules.append((lhs,rhs))

for rule in rules:
    lhs,rhs = rule
    lhs_and_rhs_count = 0
    lhs_count = 0
    for i in k:
        if all(item in i[1] for item in lhs)and rhs in i[1]:
            lhs_and_rhs_count +=1
            lhs_count +=1
        elif all(item in i[1] for item in lhs):
            lhs_count+=1
    confidence = lhs_and_rhs_count /lhs_count
    print(f"Rule:{lhs} => {rhs}, Confidence: {confidence}")
