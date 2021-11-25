def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total


funcion=[1,2,3,4]
print(suma(funcion))


def multiplicacion(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total


print(multiplicacion(funcion))

