def triangles():
    t = 0
    i = 0
    while True:
        t, i = t + i + 1, i + 1
        yield t

for t in triangles():
    count = len([i for i in range(1, t+1) if not t % i])
    if count > 500:
        print(t)
        break
