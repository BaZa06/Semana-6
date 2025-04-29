# Leer 
def mostrarNumeros(inicio=0, fin=0):
	if(inicio > fin):
		for numero in range(inicio, fin-1, -1):  # Corrected to iterate in reverse
			print(numero, end=" ")
	else:
		for i in range(inicio, fin + 1):
			print(i, end=" ")


def main():
	inicio = int(input("Ingrese el número de inicio: "))
	fin = int(input("Ingrese el número de fin: "))
	mostrarNumeros(inicio, fin)

main()