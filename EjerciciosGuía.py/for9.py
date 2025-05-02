#Serie de Fibonacci hasta un límite
n = int(input("Ingrese un número positivo: "))
a, b = 0,1
print("Serie de Fibonacci hasta el número", n, ":")
for i in range(n):
    print(a, end=" ")
    a,b = b, a + b
print(b, end=" ")