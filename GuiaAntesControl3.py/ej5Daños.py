N = int(input())
Pa, Pb, Pc = map(int, input().split())
combo = []
for i in range(N):
    ataques = input().upper()
    total_dano =  (int(ataques.count("A"))*Pa)+(int(ataques.count("B"))*Pb)+(int(ataques.count("C"))*Pc)
    combo.append(total_dano)
for x in combo:
    print(x)
