my_list = [1,2,3,2,4,1,2,4,5]
frequency_count = {}

for item in my_list:
    if item in frequency_count:
        frequency_count[item] += 1
    else:
        frequency_count[item] = 1

print(frequency_count)
