x = 0
n = 0

for begin in range(1000000,2,-1):
    length = 1
    n = begin
    while n != 1:
        b = 0
        if n%2 == 0:
            b = n//2
            n = b
            length += 1
        else:
            b = (3*n)+1
            n = b
            length += 1

    if length > x:
        x = length
        print(begin,"has",x,"terms.")
    
    
    
