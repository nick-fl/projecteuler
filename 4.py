palindromes = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        revnum = ""
        stringrevnum = str(revnum)
        num = str(i*j)
        length = len(num)
        for n in range(length-1,-1,-1):
            stringrevnum += num[n]
            if stringrevnum == num:
                palindromes.append(int(stringrevnum))

print(max(palindromes))
                
                


        
        
        
       
