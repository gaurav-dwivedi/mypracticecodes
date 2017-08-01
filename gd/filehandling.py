##sampleTextFile
file = open("SampleTextFile.txt","r")
d={}
for line in file:
    l1=line.split(" ")

    for item in l1:
        d[item] = d.get(item,0) + 1
#print(d)

maxValue = 0
for k,v in d.items():
    if v>maxValue:
        maxValue = v
    
print(maxValue)
l2=[]
for v in d.values():
    l2.append(v)
    

l3=list(reversed(sorted(l2)))

print(l3)

    

    
    
