"""flag = 0
n = int(input("Enter any number greater than 1:"))
if n == 2:
    flag = 0
else:
    for i in range(2, n):
        if (n % i == 0):
            flag = 1
            break
if flag == 0:
    print("Prime")
else:
    print("Non prime")
#############################
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print('Not Prime')
        break
else:
    print('Prime')
"""
n = int(input())
start=2
primes=[]
for i in range(start,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        primes.append(i)
print(primes)