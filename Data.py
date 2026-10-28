data = {'a': 1, 'b': 2, 'c': 3}
new_data = {}
for k in data:
    new_data[data[k]] = k
print(new_data)