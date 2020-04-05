def findorder(listt):
    arr = []
    for i in range(len(listt)):
        arr.append((listt[i][0], listt[i][1], i))
    arr.sort()
    c_end = 0
    j_end = 0
    res_arr = []
    for start, end, index in arr:
        if start < c_end and start < j_end:
            return "IMPOSSIBLE"
        if start >= c_end:
            res_arr.append(('C', index))
            c_end = end
        else:
            res_arr.append(('J', index))
            j_end = end
    ans = ''
    for c, index in sorted(res_arr, key=lambda x: x[1]):
        ans += c
    return ans

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    time = []
    for _ in range(N):
        interval = [int(s) for s in input().split(" ")]
        time.append(interval)
    ans = findorder(time)
    print("Case #{}: {}".format(t, ans))