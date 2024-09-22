def f(a, b):
    if b == 0:
        return (a, 1, 0)  
    else:
        d, x1, y1 = f(b, a % b)  
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)

k = input().strip().split()
a, b = int(k[0]), int(k[1])

d, x, y = f(a, b)

print(x, y, d)
