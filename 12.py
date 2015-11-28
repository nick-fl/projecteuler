import math

def divisors(n):
    divisors = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            divisors += 2
        if i**2 == n:
            divisors -= 1
    return(divisors)
        
    
    
print("Finding the smallest triangular number with over 500 divisors...")

a = 0
i = 1
while a == 0:
    tn = ((i*(i+1))//2)
    if divisors(tn) > 500:
        a = 1
    else:
        i += 1

print(tn)

