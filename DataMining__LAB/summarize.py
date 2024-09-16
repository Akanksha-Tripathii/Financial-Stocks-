import pandas as p
import numpy as np
import statistics
#import matplotlib.pyplot as plt
data_path = p.read_csv(r"C:\Users\abhis\Downloads\summarise.csv")
sorted_data = data_path.sort_values(by='age')
print(sorted_data)

data_path = sorted_data['age']

new_data = []
for i in data_path:
    new_data.append(i)
print(new_data)

length = len(new_data)
get_sum = sum(new_data)
mean = get_sum/length
print('mean: ',mean)

def cal_median(numbers):
    size = len(numbers)
    numbers.sort()
    if size%2 == 0:
        mid = int(size/2)
        median = int(numbers[mid-1]+numbers[mid])/2
    else:
        mid = int((size+1)/2)
        median = int(numbers[mid-1])
    return median
median = cal_median(new_data)
print('Median: ',median)

# fig = plt.figure(figsize=(10,7))
# plt.boxplot(new_data)
# plt.show()

low = new_data[0]
high = new_data[-1]
d_range = high - low
mid_range = (high+low)/2

print('Mid range: ',mid_range)
print('Range: ',d_range)

v = 0
for i in new_data:
    v += (i-mean)**2
    variance = v/length
print(variance)

std_dev = variance ** (1/2)
print('Standard deviation: ',std_dev)

def cal_quartile(num):
    size = len(num)
    mid = int(size/2)
    return mid

q1 = []
mid_q1 = cal_quartile(new_data)
for i in range(0,mid_q1):
    q1.append(new_data[i])
Quartile_1 = cal_median(q1)
print("Quartile 1: ",Quartile_1)

print("Quartile 2: ",median)

q3 = []
mid_q3 = cal_quartile(new_data)
for i in range(mid_q1+1,len(new_data)):
    q3.append(new_data[i])
Quartile_3 = cal_median(q3)
print("Quartile 3: ",Quartile_3)

iqr = Quartile_3 - Quartile_1
print("IQR: ",iqr)