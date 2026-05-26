print("=== Registro de de equipaje -VueloCHILE ===")
#1.validar la cantidad total a registrarse
total_equipaje = 0
while total_equipaje <= 0:
    try:
        entrada = input("cuantos equipajes desea registrar: ")
        total_equipaje = int(entrada)
        if total_equipaje <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
       print("¡Cantidad inválida! Ingresa un entero positivo para continuar.") 

#inicializador de contadores
equipajes_cabina = 0
equipajes_bodega = 0

#paso 2 Ciclo registro delquipaje
for i in range(total_equipaje):
    print(f"\n-- Registro del equipaje 0° {i+i} ---")
    codigo_tiquet = ""
    while True:
        codigo_tiquet = input("ingrese codigo de tiquet (min 5 caracteres, sin espacio)")
        #validar largo de codigo de ticket
        if len(codigo_tiquet) < 5:
            print("Error: el codigo debe tener al menos 5 caracteres")
            continue
        #validar que no tenga espacios
        tiene_espacios = False
        for caracter in codigo_tiquet:
            if caracter == " ":
                tiene_espacios = True
        if tiene_espacios:
            print("Error: el codigo no debe incluir espacios")
            continue 
        break
    #validacion del peso
    peso = -1
    while peso <= 0:
        try:
            entrada_peso = input("ingrese el peso del equuipaje en kg (entero positivo)")
            peso =int(entrada_peso)
            print("Error de pesaje, ingrese un numero positivo para el peso")
        except ValueError:
            print("Error de pesaje, ingrese un numero positivo para el peso")
    
    #paso numero 3 Clasificacion del producto
    if peso > 10:
        equipajes_bodega += 1
        print("clasificado como equipaje de bodega")
    else:
        equipajes_cabina += 1
        print("clasificado como equipaje cabina")
    #paso 4 Salida final.
print("\n===========================================================")
print(f"¡El avión transportará {equipajes_cabina} equipajes en Cabina y {equipajes_bodega} equipajes en Bodega! ¡Manifiesto de carga listo!")
print("\n===========================================================")
