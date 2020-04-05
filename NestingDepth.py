def listToString(s):  
    str1 = ""  
    for i in s:  
        str1 += i   
    return str1  

T = int(input()) #number of testcases
for n in range(1,T+1):
    stack = []
    close = 0
    count = 0
    string = input() #string of numbers
    res = [int(x) for x in str(string)] #list of different integers
    prev = 0
    for i in res:
        if i!=0:
            count += 1
        if i-prev>0:
            k = i-prev
            while k:
                stack.append('(')
                k -= 1
        elif i-prev<0:
            k = prev-i
            while k:
                stack.append(")")
                k -= 1
        stack.append(str(i))
        prev = i
    while prev:
        stack.append(")")
        prev -= 1
    print("Case #{}: {}".format(n,listToString(stack)))