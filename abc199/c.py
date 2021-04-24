N = int(input())
S = input()
Q = int(input())

Q_row = [0] * Q
N_Len = N/2
for i in range(Q):
    Q_row[i] = list(map(int,input().split()))

for i in range(1,Q-1,1):
    # Tが１の時
    if(Q_row[i][0] == 1):
        tmp_aa = S[int(Q_row[i][2])]
        tmp_bb = S[Q_row[i][1]]
        S = tmp_bb + tmp_aa
        print(S)
    # Tが２以上の時
    if(Q_row[i][0] == 2):
        tmp_a = S[0:int(N_Len+1)]
        tmp_b = S[int(N_Len+1)::]
        S = tmp_b + tmp_a
print(S)