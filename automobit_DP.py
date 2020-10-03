from random import randint
def assemblystation(a, t, e, x):
    t1 = [0 for i in range(len(a))]
    t2 = [0 for i in range(len(a))]
    
    t1[0] = e[0] + a[0][0]
    t2[0] = e[1] + a[1][0]

    for i in range(len(a)):
        t1[i] = min(t1[i-1] + a[0][i], t2[i-1] + t[1][i] + a[0][i])
        t2[i] = min(t2[i-1] + a[1][i], t1[i-1] + t[0][i] + a[1][i])

    return min(t1[len(a) - 1] + x[0], t2[len(a) - 1] + x[1]) 

a = [[randint(5,15) for i in range(0,15)],[randint(5,15) for i in range(0,15)]]
t = [[randint(5,15) for i in range(0,15)], [randint(5,15) for i in range(0,15)]]
e = [randint(5, 15) for i in range(2)]
x = [randint(5, 15) for i in range(2)] 

print(a)
print(t)
print(e)
print(x)
print('')
print("The shortest time is:", end = ' ')
print(assemblystation(a, t, e, x))