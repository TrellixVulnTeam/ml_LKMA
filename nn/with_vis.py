# 2 - 2 - 2 - 1 NN ReLu
import random
import matplotlib.pyplot as plt
import numpy as np

def rand():
    return random.random() - random.random()

'''=============== Sample ============'''
data = []
for i in range(100):
    x = i % 2 + rand()
    y = i % 2 + rand()
    t = i % 2
    data.append([x, y, t])

for p in data:
    x = p[0]
    y = p[1]
    t = p[2]
    mark = ['x', '.'][t]
    plt.plot(x, y, mark, color='#aaaaaa')

#plt.show()

'''=============== NN ================='''
def ReLu(v):
    return max(0, v)

def layer_calc(x, w):
    ans = []
    for wi in w:
        v = 0
        for i in range(len(x)):
            v += wi[i] * x[i]
        ans.append(ReLu(v))
    return ans

def define(x):
    return x[0]

def train():
    d = 0
    for p in data:
        x = [p[0], p[1]]
        t = p[2]
        for wx in w:
            x1 = layer_calc(x, wx)
        #x1 = layer_calc(x, w1)
        #x1 = layer_calc(x, w2)
        #x1 = layer_calc(x, w3)
        d += abs(define(x1) - t)
    error_rate = d / len(data)
    return error_rate

w1 = []
for i in range(2):
    w1.append([rand(), rand()])
w2 = []
for i in range(4):
    w2.append([rand(), rand()])
w3 = []
for i in range(1):
    w3.append([rand(), rand()])

w = [w1, w2, w3]

def get_slope(wx):
    slope = [[0 for y in x] for x in wx]
    for xi in range(len(wx)):
        for yi in range(len(wx[xi])):
            tmp = wx[xi][yi]
            inc = wx[xi][yi] + d
            dec = wx[xi][yi] - d
            wx[xi][yi] = inc
            inc_e = train()
            wx[xi][yi] = dec
            dec_e = train()
            dx = inc - dec
            dy = inc_e - dec_e
            slope[xi][yi] = dy / dx
            wx[xi][yi] = tmp
    return slope

d = 0.1
alpha = 0.2
for i in range(10):
    #slope1 = get_slope(w1)
    #slope2 = get_slope(w2)
    #slope3 = get_slope(w3)
    for i in range(len(w)):
        slope = get_slope(w[i])
        w[i] = [[w[i][xi][yi] - slope[xi][yi] * alpha for yi in range(len(w[i][xi]))] for xi in range(len(w[i]))]
    #w1 = [[w1[xi][yi] - slope1[xi][yi] * alpha for yi in range(len(w1[xi]))] for xi in range(len(w1))]
    #w2 = [[w2[xi][yi] - slope2[xi][yi] * alpha for yi in range(len(w2[xi]))] for xi in range(len(w2))]
    #w3 = [[w3[xi][yi] - slope3[xi][yi] * alpha for yi in range(len(w3[xi]))] for xi in range(len(w3))]
    print("E:", train())
