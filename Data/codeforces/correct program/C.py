
t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    mx = [-1,-1]
    for i in range(n):
        if mx[0]==-1 or s[i]>=s[mx[0]]:
            mx[1] = mx[0]
            mx[0] = i
        elif mx[1]==-1 or s[i]>=s[mx[1]]:
            mx[1] = i
    for i in range(n):
        if i==mx[0]:
            print(s[i]-s[mx[1]],end=" ")
        else:
            print(s[i]-s[mx[0]],end=" ")
    print()

    