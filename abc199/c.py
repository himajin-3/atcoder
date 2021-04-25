N = int(input())
S = input()
Q = int(input())

S = [ss for ss in S]
flg_flip = False
for _ in range(Q):
  T, A, B = map(int, input().split())
  if T==1:
    if flg_flip:
      if A > N:
        A = A - N
      else:
        A = A + N
      if B > N:
        B = B - N
      else:
        B = B + N
    S[A-1], S[B-1] = S[B-1], S[A-1]
  else:
    flg_flip = not flg_flip
S = "".join(S)
if flg_flip:
  S = S[N:] + S[:N]
print(S)
