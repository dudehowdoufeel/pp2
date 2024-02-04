def solve(numheads, numlegs):
    for chi in range(numheads+1):
        rab=numheads-chi
        if 2*chi + 4*rab == numlegs:
            return chi, rab
    

result=solve(numheads=35, numlegs=94)
if result:
    chi, rab=result
    print("chi: ",chi)
    print("rab: ",rab)
  

