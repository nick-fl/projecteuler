#looked up the closed forms for the sum of n squares and the sum of n integers

n = int(input("Enter any number of the first n natural numbers to be calculated"))

x = ((n*(n+1)*(2*n+1))/(6))

intsum = ((n*(n+1))/(2))

intsumsq = intsum**2

print(intsumsq-x)
