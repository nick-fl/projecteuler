import math

number = int(input("What number do you want to know the largest prime factor of?"))



def findpfs(x):
#first finding the factors, starting with the largest
    for i in range(1,int((x/2)+1)):
        if x%i == 0:
#if it found a factor, see if it is prime
            checkfactor = x/i
            print("Checking if",checkfactor,"is prime")
            factors = 0
#if a number is not prime it must have a factor <= sqrt(number) (that isn't 1)
            for j in range(int(math.sqrt(checkfactor)),1,-1):
                if checkfactor%j == 0:
                    factors += 1
                    break
            if factors == 0:
                print(checkfactor,"is the largest prime factor of",x)
                break

findpfs(number)
                    



