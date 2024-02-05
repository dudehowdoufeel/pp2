def poli(n):
   
    a = [c for c in n] #
    return a == a[::-1]

a= input()
if poli(a):
    print("YES")
else:
    print("NO")
