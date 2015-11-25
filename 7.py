import time
import math

start_time = time.time()

nth = int(input("Enter a number n to find the nth prime number"))
nprime = 0

for i in range(2,1+2**nth):
    if nprime != nth:
        factors = 0
        for j in range(int(math.sqrt(i)),1,-1):
            if i%j == 0:
                factors += 1
                break
        if factors == 0:
            nprime +=1     
    else:
        break

if i != 2:
    print(i-1,"is the n =",nth,"prime number")
else:
    print(i,"is the n =",nth,"prime number")

print("took",time.time() - start_time,"s to run")



    
