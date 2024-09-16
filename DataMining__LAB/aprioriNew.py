import pandas as p
import numpy as np
from itertools import combinations

data = p.read_csv(r"C:\Users\abhis\Downloads\apriori.csv")
print(data)
 
list_data = data.values.tolist()
print(list_data)

unique_ids = {id for i in list_data for id in i[1].split(',')}
iD = sorted(unique_ids)
print('Ids are: ',iD)

c1 = {}
for i in list_data:
    itemsets = i[1].split(',')
    for item in itemsets:
        if item in c1:
            c1[item] +=1
        else:
            c1[item] = 1
print('C1')
print(c1)

min_sup = 2
L1 = {id:count for id,count in c1.items() if count>=min_sup}
print('L1')
print(L1)

candidate_itemsets = list(combinations(L1.keys(),2)) 
c2 = {}
for itemsets in candidate_itemsets:
    c2[itemsets] = 0
    for i in list_data:
        if all(id in i[1] for id in itemsets):
            c2[itemsets] += 1
print("c2: ")
print(c2)

L2 = {itemsets:count for itemsets,count in c2.items() if count>=min_sup}
print('L2')
print(L2)

c3 = {}
for i in list_data:
    items = i[1].split(',')
    for c in combinations(items,3):
        if all((c[i],c[j]) in L2 or (c[j],c[i]) in L2 for i in range(3) for j in range(i+1,3)):
            c3[c] = c3.get(c,0)+1
print("c3: ")
print(c3)

c3 = [('I1', 'I2', 'I5')]
rules = []
for i in range(len(c3[0])):
    lhs = c3[0][:i] + c3[0][i+1:]
    rhs = c3[0][i]
    rules.append((lhs,rhs))

for rule in rules:
    lhs,rhs = rule
    lhs_and_lhs_count = 0
    lhs_count =0
    for i in list_data:
        if all(item in i[1] for item in lhs)and rhs in i[1]:
            lhs_and_lhs_count +=1
            lhs_count +=1
        elif all(item in i[1] for item in lhs):
            lhs_count +=1
    confidence = lhs_and_lhs_count/lhs_count
    print(f"Rule {lhs} => {rhs}  Confidence: {confidence}")

c3 = [('I1', 'I2', 'I3')]
rules = []
for i in range(len(c3[0])):
    lhs = c3[0][:i] + c3[0][i+1:]
    rhs = c3[0][i]
    rules.append((lhs,rhs))

for rule in rules:
    lhs,rhs = rule
    lhs_and_lhs_count = 0
    lhs_count =0
    for i in list_data:
        if all(item in i[1] for item in lhs)and rhs in i[1]:
            lhs_and_lhs_count +=1
            lhs_count +=1
        elif all(item in i[1] for item in lhs):
            lhs_count +=1
    confidence = lhs_and_lhs_count/lhs_count
    print(f"Rule {lhs} => {rhs}  Confidence: {confidence}")

