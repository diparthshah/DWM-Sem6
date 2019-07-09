x = [1,2,4,5] 
y = [1,1,3,4]
n = 4
dist1 = []
dist2 = []
cx1 = float(x[0])
cy1 = float(y[0])
cx2 = float(x[1])
cy2 = float(y[1])

print ("\nInitial Centroid1 = (",cx1 ,",",cy1,")")
print ("Initial Centroid2 = (",cx2 ,",",cy2,")")
k1 = []
k2 = []
prev_k1 = set()
prev_k2 = set()

while(True):
    for i in range(0,n):
        val = ((cx1-x[i])**2 + (cy1-y[i])**2)**0.5
        dist1.append(val)
        val = ((cx2-x[i])**2 + (cy2-y[i])**2)**0.5
        dist2.append(val)

    print("\nDistance Matrix:\n")
    print(dist1)
    print(dist2)

    for i in range(0,n): 
        if(dist1[i] <= dist2[i]):
            k1.append(i)
        else:
            k2.append(i)
    print("K1 Cluster : ",k1)
    print("K2 Cluster : ",k2)
    
    curr_k1 = set(k1)
    curr_k2 = set(k2)
    if(len(curr_k1 - prev_k1) is 0 and len(curr_k2 - prev_k2) is 0):
        break
    prev_k1 = curr_k1
    prev_k2 = curr_k2

    g1 = len(k1)
    sumx = 0
    sumy = 0
    for a in range(0,g1):
        item = k1[a]
        sumx = sumx + x[item]
        sumy = sumy + y[item]
    cx1 = float(sumx/g1)
    cy1 = float(sumy/g1)
    print ("Centroid1 = (",cx1 ,",",cy1,")")

    g2 = len(k2)
    sumx = 0
    sumy = 0
    for a in range(0,g2):
        item = k2[a]
        sumx = sumx + x[item]
        sumy = sumy + y[item]
    cx2 = float(sumx/g2)
    cy2 = float(sumy/g2)
    print ("Centroid2 = (",cx2 ,",",cy2,")")
    
    dist1 = []
    dist2 = []
    k1 = []
    k2 = []    

"""
https://people.revoledu.com/kardi/tutorial/kMean/NumericalExample.htm

D:\sem6\dwm>python kmeans.py

Initial Centroid1 = ( 1.0 , 1.0 )
Initial Centroid2 = ( 2.0 , 1.0 )

Distance Matrix:

[0.0, 1.0, 3.605551275463989, 5.0]
[1.0, 0.0, 2.8284271247461903, 4.242640687119285]
K1 Cluster :  [0]
K2 Cluster :  [1, 2, 3]
Centroid1 = ( 1.0 , 1.0 )
Centroid2 = ( 3.6666666666666665 , 2.6666666666666665 )

Distance Matrix:

[0.0, 1.0, 3.605551275463989, 5.0]
[3.144660377352201, 2.357022603955158, 0.4714045207910319, 1.885618083164127]
K1 Cluster :  [0, 1]
K2 Cluster :  [2, 3]
Centroid1 = ( 1.5 , 1.0 )
Centroid2 = ( 4.5 , 3.5 )

Distance Matrix:

[0.5, 0.5, 3.2015621187164243, 4.6097722286464435]
[4.301162633521313, 3.5355339059327378, 0.7071067811865476, 0.7071067811865476]
K1 Cluster :  [0, 1]
K2 Cluster :  [2, 3]
Centroid1 = ( 1.5 , 1.0 )
Centroid2 = ( 4.5 , 3.5 )

""" 
