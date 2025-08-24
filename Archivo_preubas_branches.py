print("archivo de prueba sobre el manejo de brancehs")
while True:
    print("---------MENU DE OPCIONES----------")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potenciacion")
    print(f"6. saliar del menu")
    op_elegida = input(f"ELIJA UNA ACCION A REALIZAR (1-5): ")
    match op_elegida:
        case "1":
            a = int(input("ingrese primer numero: "))
            b= int( input("ingrese segundo numero: "))
            suma = a+b
            print(f"RESULTADO DE LA SUMA: {suma}")

        case "2":
            c = int(input(f"ingrese primer numero: "))
            d = int(input(f"ingrese segundo numero: "))
            resta = c-d
            print(f"EL RESULTADO DE LA RESTA: {resta}")

        case "3":
            e = int(input(f"ingrese primer numero: "))
            f = int(input(f"ingrese segundo numero: "))
            multi = e * f
            print(f"EL RESULTADO DE LA MULTIPLICACION ES IGUAL A: {multi}")

        case "4":
            g = int(input(f"ingresar primer numero: "))
            h = int(input(f"ingresar segundo numero: "))
            division = g / h
            print(f"El resultado de la division es igual a: {division}")

        case "5":
            vq1 =int(input(f"ingrese algun numero: "))
            potencia = vq1**2
            print(f"RESULTADO DE LAS POTENCIA: {potencia}")

        case "6":
            print(f"SALIENDO DEL SISTEMA...............")
            break

        case _:
            print(f"----------ERROR, INGRESE ALGUN VALOR CORRECTO----------")
