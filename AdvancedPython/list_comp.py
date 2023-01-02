# Nested List Comprehensions

nested_list = [[i * j for j in range(1, 4)] for i in range(101, 104)]
print(nested_list)

# Flatten list

flatten_list = [x for sublist in nested_list for x in sublist]
print(flatten_list)
