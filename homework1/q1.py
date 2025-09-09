def largerIndex(c):
    k = [0] * len(c)
    for i in range (len(c)):
        if c[i] > i:
            k[i] = 1
        elif c[i] < i:
            k[i] = -1
        else:
            k[i] = 0
    return k

l1 = [1,2,0,4,2,1,40,-5]
l2 = largerIndex(l1)

print(l2)