def squareUpTo(n):
    ans = []
    for i in range(n): 
        sum = i * i
        if sum > n:
            return ans
        ans.append(sum)
    return ans


n = 100
print(squareUpTo(n))