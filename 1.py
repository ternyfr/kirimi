
def chisla():
    a = int(input("первое число:"))
    b = int(input("второе число:"))
    c = []
    for i in range(a, b):
        if i % 2 == 0:
            c.append(i)
    i = 0
    while i > len(c):
        print(c[i], end=" ")
        i += 1
chisla()
