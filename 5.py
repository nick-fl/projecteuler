#infinitely outputs multiples of 20. there is probably and easier way

print("Finding the smallest number that has every number between 1 and 20 as a factor.")

found = 0
a = 0

while found == 0:
    counter = 0
    b = a + 20
    for i in range(1,21):
        if b%i == 0:
            counter += 1
        if counter == 20:
            print(b,"is the smallest number that has every number between 1 and 20 as a factor.")
            found += 1
            break
    a = b
    

