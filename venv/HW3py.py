a = [int(input("->")) for i in range(int(input("n=")))]
s = 0
t = 0
for i in range(len(a)):
    if a[i] >  0:
        s += a[i]
t = s / len(a)
print(t)

