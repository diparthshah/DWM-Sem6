mat = [[0,1,1],[0,0,1],[1,0,0]]
p =[1.0,1.0,1.0]
v= 3
d = 0.85
out = []
inarr = []
tempres = float(0)

for i in range(0,v):
    out.append(mat[i].count(1))

print(p)
for it in range(0,3):
    for i in range(0,v):
        for j in range(0,v):
            if(mat[j][i]==1):
                inarr.append(j)
        for k in range(0,len(inarr)):
            tempres = tempres + float(p[inarr[k]] / out[inarr[k]])
        p[i] = float((1-d) + d * tempres)
        tempres = 0
        inarr = []
    print(p)

"""
E:\dwm>python pagerank.py
[1.0, 1.0, 1.0]
[1.0, 0.575, 1.06375]
[1.0541874999999998, 0.5980296875, 1.106354921875]
[1.09040168359375, 0.6134207155273438, 1.134828323725586]
"""  