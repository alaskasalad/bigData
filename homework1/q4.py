def duplicates(c):
    ans = []
    freq = {}
    for num in c:
        if num in freq:
            freq[num] += 1
            ans.append(num)
        else:
            freq[num] = 1
    return ans

l3 = [1,2,5,3,6,2,4,5]
print(duplicates(l3))
