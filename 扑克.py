import random
a = "♥"
b = "♥"
c = "♣"
d = "♦"//四种花色
编号 = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
A = []
for i in range(len(编号)-1):
    A.append(a + 编号[i])//红桃花色的牌组
B = []
for i in range(len(编号)-1):
    B.append(a + 编号[i])//黑桃花色的牌组
C = []
for i in range(len(编号)-1):
    C.append(a + 编号[i])//梅花花色的牌组
D = []
for i in range(len(编号)-1):
    D.append(a + 编号[i])//方片花色的牌组
Kings = ["Joker","JOKER"]
牌组 = A + A + B + B + C + C + D + D + Kings + Kings
//每套颜色的牌组合在一起再加两个王

def 摸牌():
    S1 = random.sample(牌组,25)//每个玩家摸取25张牌
    for i in S1:
        牌组.remove(i)//牌组剩余的牌
    S2 = random.sample(牌组,25)
    for i in S2:
        牌组.remove(i)
    S3 = random.sample(牌组,25)
    for i in S3:
        牌组.remove(i)
    S4 = random.sample(牌组,25)
    for i in S4:
        牌组.remove(i)
    底牌 = 牌组//底牌剩余8张
            
    print("玩家1：",S1)
    print("玩家2：",S2)
    print("玩家3：",S3)
    print("玩家4：",S4)
    print("底牌:",底牌)
    
摸牌()
