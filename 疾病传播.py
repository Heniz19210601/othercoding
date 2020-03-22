##这是一个疾病传播模型。一开始只有一个感染者和一百个健康人，每个人每天只在规定世界内不动或移动一格。
##当感染者和健康人处在同一坐标时会感染健康人。感染者的治愈几率是1以内随机的小数，如果治愈几率小于治愈值则感染者恢复为健康人。
##画一张度过最大运行时间之后所有人的分布图吧！

import numpy as np
import matplotlib.pyplot as plt

maxtime = 1000##最大运行时间
npeople = 100##健康人的数量
remission = 0##治愈几率
sidelength = 40
x = np.arange(0,sidelength+1,1)
y = np.arange(0,sidelength+1,1)
world = np.zeros([sidelength,sidelength])##圈定一个移动范围

human = np.zeros(npeople)
coordinate_human = []##健康人的坐标
for h in human:
    coordinate_human.append([np.random.choice(x),np.random.choice(y)])##第一天所有人的随机坐标

zombie_initial = [np.random.choice(x),np.random.choice(y)]##第一个感染者的坐标
coordinate_zombie = []##感染者的坐标
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
plt.show() ##画出第一天所有健康人和感染者的分布图

def move(x):##单次移动
    list40 = [-1,-1,0]
    list0 = [0,1,1]
    list_all = [-1,0,1] ##范围内移动
    move40 = np.random.choice(list40)
    move0 = np.random.choice(list0)
    move_normal = np.random.choice(list_all)
    if x[0] <= 0:
        x[0] += int(move0)##移动后x坐标小于0则必须前进或者原地不动
        if int(move0) == 0:##如果x坐标不移动则考虑y坐标移动
            if x[1] <= 40:
                x[1] += int(np.random.choice(list0))
            elif x[1] >= 40:
                x[1] += int(np.random.choice(list40))
            else:
                x[1] += int(np.random.choice(list_all))
    elif x[0] >= 40:
        x[0] += int(move40)##移动后x坐标大于40则必须后退或原地不动
        if int(move40) == 0:##如果x坐标不移动则考虑y坐标移动
            if x[1] <= 40:
                x[1] += int(np.random.choice(list0))
            elif x[1] >= 40:
                x[1] += int(np.random.choice(list40))
            else:
                x[1] += int(np.random.choice(list_all))
    else:    
        x[0] += int(move_normal)##移动后不超出范围
        if int(move_normal) == 0:##如果x坐标不移动则考虑y坐标移动
            if x[1] <= 40:
                x[1] += int(np.random.choice(list0))
            elif x[1] >= 40:
                x[1] += int(np.random.choice(list40))
            else:
                x[1] += int(np.random.choice(list_all))
    return x

def step(coordinate_zombie,coordinate_human):
    for i in range(len(coordinate_zombie)-1):
        for j in range(len(coordinate_human)-1):
            each_zombie = [coordinate_zombie[i][0],coordinate_zombie[i][1]]
            each_human = [coordinate_human[j][0],coordinate_human[j][1]]
            
            if each_zombie == each_human:##判定是否有健康人和感染者在同一坐标
                coordinate_human.remove(each_zombie)
                coordinate_zombie.append(each_human)##如果是则健康人被感染，从健康列表移除，加入感染者列表
        
    reborn = []##治愈
    for i in range(len(coordinate_zombie)):
        a = np.random.random(1)
        if a < remission:
            reborn.append(i)##当治愈几率小于治愈值时感染者恢复为健康人
    
    for j in reborn:
        new_human = reborn[j]
        zombie.remove(new_human)
        human.append(new_human)##治愈者从感染者列表移除，加入健康人列表
        
    for x in coordinate_zombie:
        move(x)

    for y in coordinate_human:
        move(y)
   
    return coordinate_zombie,coordinate_human

maxtime = 1000

for day in range(maxtime):
    step(coordinate_zombie,coordinate_human)##运行最大天数次数的移动

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
