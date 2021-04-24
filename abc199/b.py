N = int(input())

a = [0] * N
b = [0] * N
cnt = 0
max_a = 0
min_b = 1000

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

ans = b[0]+1 - a[-1]
if(ans<0):
    print(0)
else:
    print(ans)

