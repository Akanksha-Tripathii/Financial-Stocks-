list_data = [
2.78, 9.5, 13.51, 20.85, 36.35, 27.55, 15.06, 72.6, 218.65, 327.75
]

percentage_changes = []

for i in range(len(list_data) - 1):
    diff = list_data[i + 1] - list_data[i]
    avg = (list_data[i + 1] + list_data[i]) / 2
    if avg == 0:  # Avoid division by zero
        percentage = 0
    else:
        percentage = (diff / abs(avg)) * 100
    percentage_changes.append(percentage)

print('\n',percentage_changes)
print('\nTotal percentage over 10 years: ',round(sum(percentage_changes))/10)
