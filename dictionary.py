person={'name':'A', 'job':'student','age': 22}
# key value pair
print(person)
print(person['age'])  #checking definite index/key value
print(person.keys())  #only keys
person['id']='1001'  #adding, can also edit one value
print(person)

del person['age']  #deleting a value
print(person)


#loop is different for dictionary
for key, value in person.items():
    print(key , value)
