import numpy as np

T = int(input())
ans = []
for n in range(1,T+1):
    d = int(input())
    c = 0
    r = 0
    matrix = []
    for i in range(0,d):     
        matrix.append(input().strip().split())
    for i in range(d):
        if len(set(matrix[i]))<d:
            c += 1
    matrix = np.array(matrix)
    col = []
    for i in range(0,d):
        col.append([row[i] for row in matrix])
    for i in range(d):
        if len(np.unique(col[i]))<d:
            r += 1
    k = 0
    for i in range(0,d):
        k += int(matrix[i][i])
    ans.append([n,k,r,c])
for n in range(T):
    print("Case #{}: {} {} {}".format(ans[n][0],ans[n][1],ans[n][3],ans[n][2]))