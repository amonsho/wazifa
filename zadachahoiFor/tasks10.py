n = int(input())

for num in range(1, n + 1):
    print(num, ": ", end='')
    for d in range(1, num + 1):
        if num % d == 0:
            print(d, end=' ')
    print()
