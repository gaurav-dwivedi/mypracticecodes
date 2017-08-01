##Vote count


def VoteCount(l):
    list1=[]
    d={}
    #print(list1)

    for item in l:
        d[item] = d.get(item,0) + 1
    print(d)
    maxValue=0
    for k,v in d.items():
        if v>maxValue:
            maxValue=v
    print(maxValue)

    for k,v in d.items():
        if maxValue == v:
            print(k)
    


L=['t','d','h','t','t','t','h','d','t','t']
VoteCount(L)




