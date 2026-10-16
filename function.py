# def double(num):
#     result= num*2
#     print(result)

# double(4)

# def sum(a,b):
#     return a+b

# total = sum(3, 2)
# print('total: ',total)


   # args(as many parameters as needed)
# def demo(num1,num2, *numbers):
#     print(numbers)
#     for num in numbers:
#         print(num)
# demo(3,5,8,12,45,8)


    # kargs(argument passed as key)

def a(name, id, **extra):
    identity = f'info: {name} {id} '
    # print(extra['dept'])
    # print(extra)
    for key,value in extra.items():
        print(key,value)
    return identity
so=a(name='moriom',id='24',dept=' cse' , does='walks')
print(so)


# scope
""" local scope= local to func
global scope= can be accesses everywhere
global scope can be modified in a a func only by using global keyword """
