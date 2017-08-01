"""s = "Python"
print(s[::-1])
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)
rev = []
print(list(reversed(l)), l[::-1])
for i in range(len(l) - 1, -1, -1):
    rev.append(l[i])
assert isinstance(rev, object)
print(rev)
d = {'11': '111'}
print(d)
s = input()
S=set()
r=[]
for i in s:
    if i not in S:
        S.add(i)
    else:
        r.append(i)
print(S,r)

"""
