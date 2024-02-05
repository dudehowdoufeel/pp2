def poli(s):
    if s==s[-1::-1]:
        return True
    return False
    
a=input()
result=poli(a)
print(result)