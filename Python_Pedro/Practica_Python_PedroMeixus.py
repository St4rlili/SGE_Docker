import csv

# 1
nombre_empresa = "TechSolutions" # Creamos una variable con el nombre y otra con el año y las printeamos
año_fundacion = 2010
print(nombre_empresa,año_fundacion)



# 2
numero = int(input("Introduce un número: ")) # Definimos una variable y la comparamos con 0 para identificar si es positiva o negativa
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es 0")

for num in [1,2,3,4,5,6,7,8,9,10]: # Creamos un array en el bucle y printeamos el contenido de este
    print("{}".format(num))



# 3
def calcular_iva(precio): # Creamos una funcion que recibe el precio y devuelve el precio multiplicado por 1.21
    return precio * 1.21
print(calcular_iva(100))



# 4
lista = ["Ana","Carlos","Maria","Luis"] # Creamos una lista de nombre y añadimos otro con append
lista.append("Pedro")

info_empleados = {"nombre": "Pedro", "edad": 21, "departamento": "Contabilidad"} # Creamos un diccionario de un empleado y printeamos los values
print(list(info_empleados.values()))



# 5
class Producto(object): # Creamos una clase producto que tendra nombre, precio y cantidad, y un método que devuelve el precio total multiplicando precio por cantidad

    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.cantidad}"

    def calcular_total(self,precio,cantidad):
        return self.precio * self.cantidad
    
    def aumentar_cantidad(self,cantidad): # Creamos dos funciones una para aumentar y otra disminuir, simplemente sumamos o restamos la cantidad introducida a la cantidad base
        aumento = int(input("Introduce cuanto quieres aumentar la cantidad: "))
        self.cantidad = self.cantidad + aumento
        return self.cantidad
    
    def disminuir_cantidad(self,cantidad):
        disminuir = int(input("Introduce cuanto quieres aumentar la cantidad: "))
        self.cantidad = self.cantidad - disminuir
        return self.cantidad
    
i = Producto("Plato",2,5)
print(i.calcular_total(i.precio,i.cantidad))
print(i.aumentar_cantidad(i.cantidad))
print(i.disminuir_cantidad(i.cantidad))



# 6
file = open("empleados.txt","w") # Abrimos el archivo empleados.txt y escribos los empleados de la lista creada anteriormente, luego leemos el archivo y lo printeamos
for empleado in lista:
    file.write(empleado + " ")
file.close()

file = open("empleados.txt")
print(file.read())

productos_csv = [] # Abrimos el archivo productos.csv y lo leemos creando objetos producto con los datos recolectados.

with open("productos.csv", mode="r", newline="") as file:
    contenido = csv.DictReader(file)
    for fila in contenido:
        producto = Producto(fila["nombre"],fila["precio"],fila["cantidad"])
        productos_csv.append(producto)

for producto in productos_csv:
    print(producto)