obj = [1,2,3,4,5,6,7]

def sum(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    else:
        s = a[0] + a[1]
        a = a[2:]
        a.append(s)
        return sum(a)
print(sum(obj))
