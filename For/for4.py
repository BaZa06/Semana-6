# Multiplicación de un número del 1 hasta el 12.

for n in range(1,13):
   print ("--- Tabla" +str(n)+ "---")
   for i in range(13):
    resultado = n * i
    print (i, "x", n, "=", resultado)