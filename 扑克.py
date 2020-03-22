##这是一个简单的扑克玩法——打升级的摸牌规则。
##游戏中使用两副扑克共108张，每局四个玩家参与。
##每个玩家从牌组里随机抓取25张牌，剩余8张作为底牌参与后续玩法。
import random
花色 = ["♥","♠","♣","♦"]
编号 = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
常规牌 = []
for i in 花色:
    for j in 编号:
        常规牌.append(i + j)
Kings = ["Joker","JOKER"]
牌组 = 常规牌 + Kings + 常规牌 + Kings

def 摸牌():
    S1 = random.sample(牌组,25)##每个玩家摸取25张牌
    for i in S1:
        牌组.remove(i)##牌组剩余的牌
    S2 = random.sample(牌组,25)
    for i in S2:
        牌组.remove(i)
    S3 = random.sample(牌组,25)
    for i in S3:
        牌组.remove(i)
    S4 = random.sample(牌组,25)
    for i in S4:
        牌组.remove(i)
    底牌 = 牌组##底牌剩余8张
            
    print("玩家1：",S1)
    print("玩家2：",S2)
    print("玩家3：",S3)
    print("玩家4：",S4)
    print("底牌:",底牌)
    
摸牌()
