"""filename=input('enter the name of the string:')
if not filename.endswith('.txt'):
    filename=filename+'.txt'
file=open(filename,'r')
d={}
for line in file:
    L=line.split(' ')[3][1:]
    d[L]=d.get(L,0)+1
out_file=open('req_'+filename,'w')
for k,v in d.items():
    if v>1:
        out_file.write(k)
        out_file.write('\n')
out_file.close()
"""
filename = input()
file = open(filename,"r")
d = {}
for line in file:
    timestamp = line.split(' ')[3][1:]
    d[timestamp] = d.get(timestamp,0) +1
output=open("output_timestamp.txt","w")
for k, v in d.items():
    if v>1:
        output.write(k)
        output.write("\n")