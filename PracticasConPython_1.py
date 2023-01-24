
"""
1.-Dado un número entero,, realice las siguientes acciones condicionales:
Sies impar, imprimirWeird
Sies par y en el rango inclusivo dea, imprimirNot Weird
Sies par y en el rango inclusivo dea, imprimirWeird
Sies par y mayor que, imprimirNot Weird
Formato de entrada
Una sola línea que contiene un número entero positivo,.
Restricciones
Formato de salida
Imprima Weird si el número es raro. De lo contrario, imprima Not Weird
"""
if __name__ == '__main__':
    n = int(input("Ingrese un numero: ").strip())
    if n >=1 and n <= 100:
     if n %2 ==1:
        print("Weird")
     elif n % 2==0 and (n >= 2 and n <= 5):
        print("Not Weird")
     elif n % 2==0 and (n >= 5 and n <= 20):
        print("Weird")
     elif n % 2==0 and n > 20:
        print("Not Weird")

"""
2.- Imagina una máquina expendedora que vende frutas. Cada fruta tiene su propio número, comenzando desde 0.
Escriba un programa para la máquina expendedora, que tomará un número n como entrada del cliente y devolverá la fruta con ese índice.
frutas = ["manzana", "cereza", "plátano", "kiwi", "limón", "pera", "melocotón", "aguacate"]
py
Si n<0 o n>7 (el índice de la última fruta), el programa genera "Número incorrecto". 
Entrada de muestra: 2 
Salida de muestra: banana
"""
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
print("0.-apple ","1-.cherry ", "2-.banana ", "3-.kiwi ", "4-.lemon ", "5-.pear ", "6-.peach ", "7-.avocado ")
num = int(input("Ingrese el numero de la fruta que desea: "))
if num < 0 or num > 7:
    print("Wrong number")
else:
    print(fruits[num])

"""3-.Dada un lista de numeros , la salida (bingo) si contiene el numero de entrada"""

items = [42, 88, 721, 12, 43,22 ,908]
num = int(input("ingrese el numero de su bingo"))
if num in items:
    print("Bingo")

"""4.-Dada una lista calcule la lista de elementos medio"""

items = [2, 3, 6, 8, 10, 12, 14]
num = len(items)//2
print(items[num])

"""5-.Tienes una caja magica que duplica la cantida de cada objeto que metes ada dia.
      El programa toma como entrada el recuento inicial de los articulos y el numero de dias."""

objetos = int(input("Ingrese la cantidad de Objetos--> "))
days= int(input("Ingrese el numero de Dias--> "))
i=1
while i <= days:
    objetos *= 2
    i +=1
print(objetos)
# Alternativa Solucion
objetos = int(input("Ingrese la cantidad de Objetos--> "))
days= int(input("Ingrese el numero de Dias--> "))
while days > 0:
    objetos *= 2
    days -=1
print(objetos)
