number = input()

max1 = -1  
max2 = -1 

for ch in number:
    digit = int(ch)

    if digit > max1:
        max2 = max1   
        max1 = digit 
    elif digit != max1 and digit > max2:
        max2 = digit 

if max2 == -1:
    print()
else:
    print(max2)
