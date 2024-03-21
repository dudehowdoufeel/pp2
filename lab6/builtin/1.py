'''
nums = [1,2,3,4,5]

doubles = list(map(lambda x : x*2, nums))

print(", ".join(map(str, nums)))
'''

from functools import reduce

def fun(a, b):
    return a*b

myList=input()
num = [int(x) for x in myList.split()]
result = reduce(fun, num)
print(result)
