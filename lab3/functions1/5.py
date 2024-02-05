from itertools import permutations

def per(sti):
    arr = permutations(sti)
    return list(arr)

word=input()
result=per(word)

print(result)
