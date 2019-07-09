from statistics import mean 

billamt = [34,108,64,88,99,51]
tipamt = [5,17,11,8,14,5]
n = 6
xbar = mean(billamt)
ybar = mean(tipamt)
print("Xbar : ",xbar)
print("Ybar : ",ybar)
xiarr = []
yiarr = []
xiyiarr = []
xiarrsq = []
for i in range(0,n):
    xiarr.append(billamt[i]-xbar)
    yiarr.append(tipamt[i]-ybar)
for i in range(0,n):
    xiyiarr.append(xiarr[i]*yiarr[i])
    xiarrsq.append(xiarr[i]**2)
sumofxiarrsq = sum(xiarrsq)
sumofxiyi = sum(xiyiarr)
print("Sum of (xi-xbar)*(yi-ybar) : ",sumofxiyi)
print("Sum of (xi-xbar)sq : ",sumofxiarrsq)
w1 = sumofxiyi/sumofxiarrsq
w0 = ybar - w1 * xbar
print("W1 : ",w1)
print("W0 : ",w0)
x = 75
print("Assuming x is 75")
y = w0 + w1 * x
print("Y = W0 + W1 * X")
print("Y = : ",y)
"""
E:\dwm>python linearreg.py
Xbar :  74
Ybar :  10
Sum of (xi-xbar)*(yi-ybar) :  615
Sum of (xi-xbar)sq :  4206
W1 :  0.14621968616262482
W0 :  -0.8202567760342365
Assuming x is 75
Y = W0 + W1 * X
Y = :  10.146219686162626
"""
