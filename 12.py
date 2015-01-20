import math, time

def triangles():
    t = 1
    i = 1
    while True:
        t, i = t + i + 1, i + 1
        yield t

table = {}

def factors(n):
    count = 0
    lim = n
    i = 1
    while i < lim:
        if n % i == 0:
            lim = n//i
            count += 2
        i += 1
    return count


max = 0
start = time.time()
last = start
for i in triangles():
    f = factors(i)
    if f > max:
        now = time.time()
        max = f
        print("%10d --> %3d === %4d (%4.2f)" % (i, f, int(now-start), now-last))
        last = now
    if f > 500:
        print("dast is: ", i)
        break

