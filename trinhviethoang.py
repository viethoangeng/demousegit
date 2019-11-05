a = [3, 8, 9, 13, 10, 16, 21]
b = [2, 6, 7, 12, 15]
a.sort()
b.sort()

print(" list a is:" + str(a))
print(" list b is:" + str(b))
size_a = len(a)
size_b = len(b)

concatenate = []
m, n = 0, 0

while m < size_a and n < size_b:
    if a[m] < b[n]:
        concatenate.append(a[m])
        m += 1
    else:
        concatenate.append(b[n])
        n += 1

concatenate = concatenate + a[m:] + b[n:]
print("the result is :" + str(concatenate))



