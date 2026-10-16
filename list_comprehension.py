fruits=['apple','banana','lyche','watermelon']
prices=[35,40,45,50]

# price_comb=[]
# for fruit in fruits:
#     print(fruit)
#     for price in prices:
#         print(fruit,price)
#         price_comb.append([fruit,price])
# print(price_comb)

# list comprehension
price_comb2=[[fruit,price] for fruit in fruits for price in prices]
print(price_comb2)