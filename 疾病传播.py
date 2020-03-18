import numpy as np
import matplotlib.pyplot as plt

maxtime = 1000//�������ʱ��
npeople = 100//�����˵�����
remission = 0//��������
sidelength = 40
x = np.arange(0,sidelength+1,1)
y = np.arange(0,sidelength+1,1)
world = np.zeros([sidelength,sidelength])//Ȧ��һ���ƶ���Χ

human = np.zeros(npeople)
coordinate_human = []//�����˵�����
for h in human:
    coordinate_human.append([np.random.choice(x),np.random.choice(y)])//��һ�������˵��������

zombie_initial = [np.random.choice(x),np.random.choice(y)]//��һ����Ⱦ�ߵ�����
coordinate_zombie = []//��Ⱦ�ߵ�����
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
plt.show() //������һ�����н����˺͸�Ⱦ�ߵķֲ�ͼ

def move(x)://�����ƶ�
    list40 = [-1,-1,0]
    list0 = [0,1,1]
    rand_move = [-1,0,1] //��Χ���ƶ�
    for i in range(1):
        if x[i] >= 40:
            x[i] += int(np.random.choice(list40))//����ƶ����������40�������˻�ԭ�ز���
        elif x[i] <= 0 :
            x[i] += int(np.random.choice(list0))//����ƶ�������С��0�����ǰ������ԭ�ز���
        else:    
            x[i] += int(np.random.choice(rand_move))//����ƶ��󲻳�����Χ�򲻱�
    return x

def step(zombie,human)://����
    new = []//������Ⱦ��
    for i in range(len(zombie)):
        for j in range(len(human)):
            each_zombie = [zombie[i][0],zombie[i][1]]
            each_human = [human[j][0],human[j][1]]

            if each_zombie == each_human:
                new.append(j)//����Ⱦ�ߺͽ�������ͬһ����ʱ�����˱���Ⱦ

    for n in new:
        new_zombie = human[n]
        human.remove(new_zombie)//����Ⱦ�ߴӽ������б����Ƴ�
        zombie.append(new_zombie)//����Ⱦ�߼����Ⱦ���б�
        
    reborn = [] //����
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
