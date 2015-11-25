a = 1
b = 2
c = 0
d = 2

while c <= 4000000:
    c = a + b
    if c%2 == 0:
        d += c
    a = b
    b = c

print(d)


