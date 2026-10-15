# def double(num):
#     result= num*2
#     print(result)

# double(4)

# def sum(a,b):
#     return a+b

# total = sum(3, 2)
# print('total: ',total)


   # args(as many parameters as needed)
def demo(num1,num2, *numbers):
    print(numbers)
    for num in numbers:
        print(num)

demo(3,5,8,12,45,8)
