things='pen','rubber','pencil'
print(things)  
 #tupple is a list where () is used

print(type(things))
print(things[2])
# slicing, loop kora jay nromal list er moto but item assignment kora jay na
for items in things:
    print(items)

 #tupple can consist mutable(list,string)
mega= ([3,5],[4,0])
print(type(mega))
print(mega[0])
mega[0][1]=2
print(mega)