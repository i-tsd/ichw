class solar(object):
    pass

import turtle as t
import math
de = [0,0,0,0,0,0,0]
bas = 2*math.pi/360
ax = [40,60,100,120,200,300,0]
ex = [0,0.2,0.1,0.4,0.6,0.3,0]
s =[]
colors = ['blue','lime','red','black','orange','cyan','yellow']
for i in range(7):
    exec("s%s = t.Turtle()"%i)
    exec("s%s.shape('circle')"%i)
    exec("s.append(s%s)"%i)
    s[i].color(colors[i])
    
def intl (n):
    s[n].penup()
    r = (ax[n] * (1 - ex[n] ** 2))/(1 - ex[n] * math.cos(de[n]))
    x = r*math.cos(de[n])
    y = r*math.sin(de[n])
    s[n].speed(0)
    s[n].goto(x,y)
    s[n].pendown()
    deg = de[n]
    return(deg)

def draw (n):
    r = (ax[n]* (1 - ex[n] ** 2))/(1 - ex[n] * math.cos(de[n]))
    x = r*math.cos(de[n])
    y = r*math.sin(de[n])
    deg = de[n] + bas*math.sqrt(100 ** 3 / ax[n] ** 3)
    s[n].goto(x,y)
    return(deg)

for n in range(6):
    de[n] = intl(n)

while True:
    for n in range(6):
        de[n] = draw (n)
    
