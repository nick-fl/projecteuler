import math
primesum = 2
factors = 0


for i in range(3,2000000):
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j == 0:
            factors += 1
            break
    if factors == 0:
        primesum += i
        
        
    factors = 0
    if i == 100000 or i%100000 == 0 or i == 1999999:
        
        print(primesum)
    
    
