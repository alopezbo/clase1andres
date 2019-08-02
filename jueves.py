#Ejemplo 
#print('ejecuta -pytho')

#Ejemplo 1
#producto = int ("producto")
#precio = int (input ("precio"))
#IVA = float (input("porcentaje impuesto"))
#Total = (precio*IVA)+precio
#print(producto,Total)

#Ejemplo 2
opcion = int(input("Que desea hacer \n 1-Agregar \n 2-Salir \n Su opcion "))
lista=[]
while True:
    if opcion==1:
            producto=input("Producto > ")  #variables locales
            precio=int(input("Precio > ")) #variables locales
            lista.append(producto)
            lista.append(precio)
    elif opcion==2:
            break
print(lista)
