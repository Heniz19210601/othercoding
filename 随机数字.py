��[1,2,3,4]�ĸ���������ѡ�������������λ����ÿλ���ֲ����ظ����г����еĿ����ԡ�
s = [1,2,3,4]
l = []
while len(l) < 4*3*2:
    m = random.sample(s,3)
    x = m[0]*100 + m[1]*10 + m[2]
    if x not in l:
        l.append(x)
l.sort()
print(l)