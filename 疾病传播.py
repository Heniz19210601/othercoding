import numpy as np
import matplotlib.pyplot as plt

maxtime = 1000//最大运行时间
npeople = 100//健康人的数量
remission = 0//治愈几率
sidelength = 40
x = np.arange(0,sidelength+1,1)
y = np.arange(0,sidelength+1,1)
world = np.zeros([sidelength,sidelength])//圈定一个移动范围

human = np.zeros(npeople)
coordinate_human = []//健康人的坐标
for h in human:
    coordinate_human.append([np.random.choice(x),np.random.choice(y)])//第一天所有人的随机坐标

zombie_initial = [np.random.choice(x),np.random.choice(y)]//第一个感染者的坐标
coordinate_zombie = []//感染者的坐标
coordinate_zombie.append(zombie_initial)

x = []
y = []
x1 = []
y1 = []
for m in coordinate_human:
    x.append(m[0])
    y.append(m[1])
for n in coordinate_zombie:
    x1.append(n[0])
    y1.append(n[1])

plt.plot(x1, y1, '.', color='lightgreen')
plt.plot(x, y, '.', color='blue')
plt.title('The first day for initial locations')
plt.show() //画出第一天所有健康人和感染者的分布图

def move(x)://单次移动
    list40 = [-1,-1,0]
    list0 = [0,1,1]
    rand_move = [-1,0,1] //范围内移动
    for i in range(1):
        if x[i] >= 40:
            x[i] += int(np.random.choice(list40))//如果移动后坐标大于40则必须后退或原地不动
        elif x[i] <= 0 :
            x[i] += int(np.random.choice(list0))//如果移动后坐标小于0则必须前进或者原地不动
        else:    
            x[i] += int(np.random.choice(rand_move))//如果移动后不超出范围则不变
    return x

def step(zombie,human)://运行
    new = []//新生感染者
    for i in range(len(zombie)):
        for j in range(len(human)):
            each_zombie = [zombie[i][0],zombie[i][1]]
            each_human = [human[j][0],human[j][1]]

            if each_zombie == each_human:
                new.append(j)//当感染者和健康人在同一坐标时健康人被感染

    for n in new:
        new_zombie = human[n]
        human.remove(new_zombie)//被感染者从健康人列表中移除
        zombie.append(new_zombie)//被感染者加入感染者列表
        
    reborn = [] //治愈
    for i in range(len(zombie)):
        a = np.random.random(1)
        if a < remission:
            reborn.append(i)
    
    for j in reborn:
        new_human = reborn[j]
        zombie.remove(new_human)
        human.append(new_human)

    for x in zombie:
        move(x)

    for x in human:
        move(y)

    return zombie,human

maxtime = 1000

for day in range(maxtime):
    step(coordinate_zombie,coordinate_human)

a = []
b = []
c = []
d = []
for n in coordinate_zombie:
    a.append(n[0])
    b.append(n[1])
for m in coordinate_human:
    c.append(m[0])
    d.append(m[1])
    
total_zombie = len(coordinate_zombie)
total_human = len(coordinate_human)
plt.plot(a, b, '.', color='lightgreen')
plt.plot(c, d, '.', color='blue')
plt.title('time = {}, zombies = {}, humans = {}'.format(maxtime,total_zombie,total_human))
plt.show()
