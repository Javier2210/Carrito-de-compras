#Carrito de compras

carrito_de_compras = []
precio = []

def mostrar_menu():
    print ('Menu')
    print ('1. Agregar al menu')
    print ('2. Mostrar contenido de la cesta')
    print ('3. Eliminar un producto')
    print ('4. Calcular el total de la compra')
    print ('5. Salir')
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
       
        print (f'Ingresa 6 para regresar al menu anterior')
        elemento = input(f"Ingresa el nombre del elemento: ")
        
        if elemento == "6"
           print(f"Regresaste al menu anterior")
        else:
            precios = float(input(f"Ingresa el precio del producto: "))
            carrito_de_compras.append(elemento)
            precio.append(precios)
            print(f"{elemento} ha sido agregado a la cesta.")
    
    elif opcion == "2":
      
        print("Carrito de la compra:")
        for i, item in enumerate(carrito_de_compras, start=1):
            print(f"{i}. {item}")

    elif opcion == "3":
        
        print (f'Ingresa 6 para regresar al menu anterior')
        elemento_a_eliminar = input(f"Ingresa el nombre y precio del elemento a eliminar: ")
        if elemento_a_eliminar == "6":
            print(f"Regresaste al menu anterior")

        elif elemento_a_eliminar in carrito_de_compras:
            carrito_de_compras.remove(elemento_a_eliminar)
            precio_a_eliminar = float(input(f"Ingresa el precio a eliminar: "))
            precio_a_eliminar in precio           
            precio.remove(precio_a_eliminar)
            print(f"{elemento_a_eliminar} ha sido eliminado.")
        else:
            print(f"{elemento_a_eliminar} no esta en el carrito.")

    elif opcion == "4":
       
        print(f"El total es {len(carrito_de_compras)} elementos.") 
        print(f'El precio total es de: {sum(precio)}$')

    elif opcion == "5":
     
        print("Gracias por usar el programa, adios.")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
