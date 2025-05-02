#Contador regresivo
n = int(input("Ingrese un número positivo; "))
for i in range(n,0,-1):
  regresivo = n - i
  print(i, "-", n, "=", regresivo)
    