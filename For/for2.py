#Leer un número ingresado por el usuario
#Mostrar la lera a por cada múmero del 1 al número
#Ingresado por el usuario ejemplo número 3
#a
#aa
#aaa
#i es igual a la iteratura del operador

def mostrarletra(numero):
    for i in range (1, numero+1):
        print(f"a"*i)
        
def main():
    num = int(input("Ingrese un número: "))
    mostrarletra(num)

main()        