print("Bienvenido al sistema de gestion de bicicletas")
capacidad_maxima = 25
bicis_disponibles= 25
viajes_activos = 0
ejecutando = True
#ciclo #Principal
while ejecutando:
    print("\n=== MENU PRINCIPAL===")
    print("1. Bicicletas disponibles")
    print("2. arrendar bicicletas (salida)")
    print("devolver bicilcetas (entrada)")
    print("4. historial deviajes activos")
    print("5. Salir ")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, porfavor, ingrese un numero entre 1 y 5")
        continue
    #opcion 1 Bicis disponibles
    if opcion == 1:
        print(f"\n[INFO] cantidad actual de bicicletas disponibles: {bicis_disponibles}")
    #opcion 2 Arrendar bicicletas
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Disponibles: {bicis_disponibles})---")
        if bicis_disponibles == 0:
            print("Lo sentimos, no quedan bicicletas disponibles")
        else:
            try:
                cantidad_a_arrendada = int(input("¿Cuantas bicicletas desea arrendar?:  "))
                if cantidad_a_arrendada <=0:
                    print("Error: la cantidad a arrendar debe ser mayor a 0")
                elif cantidad_a_arrendada > bicis_disponibles:
                    print(f"no hay suficientes bicis disponibles, puede arrendar hasta {bicis_disponibles}")
                else:
                    bicis_disponibles -= cantidad_a_arrendada
                    viajes_activos += cantidad_a_arrendada
                    print(f"arriendo exitoso,ha retirado {cantidad_a_arrendada} bicis")
            except ValueError:
                print("Error, debe ingresar un numero entero")
    #opcion 3 Devolver bicicletas
    elif opcion == 3:
        diferencia = capacidad_maxima - bicis_disponibles
        print(f"\n--- Devolver Bicicleta (espacio libre en estacion: {diferencia})")
        try:
            cantidad_a_devolver = int(input(" ¿Cuantas bicicletas desea devolver?:-  "))
            if cantidad_a_devolver <= 0:
                print("Error, lacantidada a devolver debe ser mayor a o")
            elif bicis_disponibles + cantidad_a_devolver > capacidad_maxima:
               print("Error, no se deben devolver tantas bicicletas, supera capacidad maxima de 25 bicics")
            else:
                bicis_disponibles += cantidad_a_devolver
                viajes_activos -= cantidad_a_devolver
                print(f"Devolucion exitosa ha regresado {cantidad_a_devolver} bicicletas")
        except ValueError:
            print("Error: debe ingresar un numero entero valido")
    #opcion 4 Historial de viajes activos
    elif opcion == 4:
        print(f"\n [Historial] Actualmente hay {viajes_activos} bicicleta(s) en uso por usuarios")
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        ejecutando = False
    else: 
        print("Opcion fuera de rango ")
        





