'''Syntax: lambda arguments : expression'''

from functools import reduce

original_list = list(range(1, 11))

# Map

doubled_numbers = list(map(lambda x: x * 2, original_list))
print(doubled_numbers)

# Filter


evens_list = list(filter(lambda x: x % 2 == 0, original_list))
print(evens_list)

# Reduce


total = reduce(lambda x, y: x + y, original_list)
print(total)

# Sorting

items = [('apple', 3), ('banana', 2), ('orange', 1)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)
