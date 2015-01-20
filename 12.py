import math

def triangles():
    t = 1
    i = 1
    while True:
        t, i = t + i + 1, i + 1
        yield t

table = {}

def factors(num):
    f = set([num])
    if num == 1:
        return set([1])
    if num in table:
        return table[num]
    for i in reversed(range(1, math.ceil(num/2)+1)):
        if num % i == 0:
            f = f | factors(i)
    table[num] = f
    return f


for t in triangles():
    l = len(factors(t))
    if l > 500:
        print("%d has %d" % (t, l))
        break


