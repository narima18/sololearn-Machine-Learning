import math
w1, w2, b, x1, x2 = [float(x) for x in input().split()]
r = w1*x1 + w2*x2 + b

def sigmoid(r):
    sig = 1 / (1+math.exp(-r))
    print(round(sig, 4))
sigmoid(r)
