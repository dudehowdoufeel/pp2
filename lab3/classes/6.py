class Prime:
    def __init__(self, a):
        self.a = a
    def isPrime(self, a):
        if (a>1):
            for i in range(2,a):
                if (a%i==0):
                    return False
            return True
        return False
    def filterPrimes(self):
        return list(filter(lambda x: self.isPrime(x),self.a))
    
b = input()
a = list(map(int, b.split()))
prF= Prime(a)
print(prF.filterPrimes())