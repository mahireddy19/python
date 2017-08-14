x = [0,1]
for i in xrange(10):
    x.append(x[-1] + x[-2])
print ', '.join(str(y) for y in x)

a = [0,1]
for i in range(10):
    lengtha=len(a)
    a.append(a[lengtha-1]+a[lengtha-2])

print a

def fibonnaci(size):
    a=[0,1]
    for i in range(size-2):
        lengtha=len(a)
        a.append(a[lengtha-1]+a[lengtha-2])
        return a

print fibonnaci(5)
print fibonnaci(6)

myDict={}
