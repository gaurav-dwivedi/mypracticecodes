list1 = []
for x in range(12,23):
    list1.append(x)
    
print(list1)

for y in list1:
    if (y%2==0):
        print('even:',y)
    else:
        print('odd:',y)

z=len(list1)
list2=[]

for s in range(z-1,-1,-1):
    print(list1[s])
    list2.append(list1[s])

print(list2)

sum=0

for k in list1:
    sum=sum+k
    pow = k**2
    print(pow)
    
print(sum)





