numbers=[34,89,78,44,95]

# index
# print(numbers[4],numbers[-4])

# # slice
# # [start:till index]
# print(numbers[:3])
# print(numbers[2:])
# print(numbers[1:3])
# # [start: last: step]
# print(numbers[1:3:2])
# print(numbers[::-1])
print(numbers[:])   #copy

# list methods
numbers.append(40)
print(numbers)
# insert=(index, value)
numbers.insert(3,77)
print(numbers)
# removind a num
numbers.remove(95)
print(numbers)
# pop
last= numbers.pop()
print(last,numbers)

index=numbers.index(78)
print(index)

numbers.sort()
print(numbers)
