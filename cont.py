def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
    
    return respuesta

print(f(10))
print(f(100))
print(f(1000))
print(f(10000))
