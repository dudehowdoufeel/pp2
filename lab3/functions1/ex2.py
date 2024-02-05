def fah_to_cel(fah):
    cel=(5/9)*(fah-32)
    return cel
fah=float(input())
result= fah_to_cel(fah)
print(result)
