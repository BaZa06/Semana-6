#Suma de números hasta alcanzar un límite

n = int(input("Ingrese un número: "))
for i in range(0, n+1):
    suma = i + i
    
    if suma < 100:
        print(i, end=" ")
    else:
     print("Se alcanzo al límite de 100")

print(i,"+",i,"=",suma)
    
        
        
