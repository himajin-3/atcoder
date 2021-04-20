N = input()

ans = "No"
for i in range(10):
    tmp = "0" * i + N
    if(tmp == tmp[::-1]):
        ans = "Yes"
        break
print(ans)