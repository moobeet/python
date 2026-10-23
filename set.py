# set= collection of unique items== no duplicates
num=[3,88,45,2,17,3,88]
print(num)
num_set=set(num)
print(num_set)
#cannot assign or find index
num_set.add(4)
print(num_set)
num_set.remove(17)
print(num_set)

if 31 in num_set:
    print('exists')
else:
    print('not found')

a={1,5,8,34}
b={3,9,5,7}
print(a & b)  #intersection
print(a | b)  #union