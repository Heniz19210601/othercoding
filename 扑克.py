import random
a = "?"
b = "?"
c = "?"
d = "?"
A = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
for i in range(len(A)):
    A[i] = a + A[i]
B = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
for i in range(len(B)):
    B[i] = b + B[i]
C = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
for i in range(len(C)):
    C[i] = c + C[i]
D = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
for i in range(len(D)):
    D[i] = d + D[i]
Kings = ["Joker","JOKER"]
ÅÆ×é = A + A + B + B + C + C + D + D + Kings + Kings
print(ÅÆ×é)
def ÃþÅÆ():
    S1 = random.sample(ÅÆ×é,25)
    for i in S1:
        ÅÆ×é.remove(i)
    S2 = random.sample(ÅÆ×é,25)
    for i in S2:
        ÅÆ×é.remove(i)
    S3 = random.sample(ÅÆ×é,25)
    for i in S3:
        ÅÆ×é.remove(i)
    S4 = random.sample(ÅÆ×é,25)
    for i in S4:
        ÅÆ×é.remove(i)
    µ×ÅÆ = ÅÆ×é
            
    print("Íæ¼Ò1£º",S1)
    print("Íæ¼Ò2£º",S2)
    print("Íæ¼Ò3£º",S3)
    print("Íæ¼Ò4£º",S4)
    print("µ×ÅÆ:",µ×ÅÆ)
    
ÃþÅÆ()