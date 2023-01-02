from collections import OrderedDict

# Dictionary Comprehension

numbers = {x: x ** 2 for x in range(10)}
print(numbers)

# Nested Dictionaries

employees = {

    'John': {'age': 35, 'salary': 50_000},
    'Alice': {'age': 32, 'salary': 40_000}

}

for k1, v1 in employees.items():
    for k2, v2 in v1.items():
        print(k1, k2, v2)

alice_salary = employees['Alice']['salary']
print(alice_salary)

# OrderedDict: Maintains the order of the keys as they are added to the dictionary.

d = OrderedDict()

d['a'] = 1
d['g'] = 3
d['c'] = 5

print(d.items())
