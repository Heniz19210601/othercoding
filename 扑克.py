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
���� = A + A + B + B + C + C + D + D + Kings + Kings
print(����)
def ����():
    S1 = random.sample(����,25)
    for i in S1:
        ����.remove(i)
    S2 = random.sample(����,25)
    for i in S2:
        ����.remove(i)
    S3 = random.sample(����,25)
    for i in S3:
        ����.remove(i)
    S4 = random.sample(����,25)
    for i in S4:
        ����.remove(i)
    ���� = ����
            
    print("���1��",S1)
    print("���2��",S2)
    print("���3��",S3)
    print("���4��",S4)
    print("����:",����)
    
����()