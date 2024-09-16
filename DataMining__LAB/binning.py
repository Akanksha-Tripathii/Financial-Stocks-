import pandas as p
import numpy as np

bin_data = p.read_csv(r'C:\Users\abhis\Downloads\data.csv')
print(bin_data)

sorted_bin_data = bin_data.sort_values(by="data")
print('Sorted data is: ')
print(sorted_bin_data)

p=sorted_bin_data['data']
new_data = []
for i in p:
    new_data.append(i)
    new_data.sort()
print('\n')
print(new_data)

bin_size = 3
def equifreq(array, bin_size):
    array_s = len(array)
    n = int(array_s/bin_size)
    for i in range(0,bin_size):
        array_1=[]
        for j in range(i*n,(i+1)*n):
            if j>=array_s:
                break
            array_1 = array_1 + [array[j]]
        print(array_1)
print("\n\n Equal partition is: ")
equifreq(new_data,bin_size)


bin1 = np.zeros((3,4)) #bin_size, data in bin
bin2 = np.zeros((3,4))
bin3 = np.zeros((3,4))

for i in range(0,12,4): #total data in 3 bins is 12
    k = int(i/4)
    mean = (new_data[i]+new_data[i+1]+new_data[i+2]+new_data[i+3])/4
    for j in range(4):
        bin1[k,j]=mean
print("\nBin mean: \n",bin1)


for i in range (0,12,4):
    k = int(i/4)
    for j in range(4):
        bin3[k,j] = (new_data[i+1] + new_data[i+2])/2
print("\n\nBin Median is : \n",bin3)


array_size = len(new_data)
n =  array_size/ bin_size
print("\nBin boundaries are: ")
for i in range(0,bin_size):
    print("Bin", i + 1, "boundaries:", end=" ")
    start_index = i * int(n)
    end_index = min((i + 1) * int(n), array_size)
    low = new_data[start_index]
    high = new_data[end_index - 1]  # Adjusted to get the last element of the bin
    for j in range(int(n)):
        print(low, end=' ')
    print(high)  # Print the high value of the bin