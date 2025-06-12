# n = int(input())

# for i in range(1, n + 1):
#     a = ' ' * (n - i)        
#     z= '*' * (2 * i - 1) 
#     print(a + z)

n=int(input())
k=n-1
l=1
for i in range(1, n+1):
    print(' '*k,l*'*')
    k-=1
    l+=2
