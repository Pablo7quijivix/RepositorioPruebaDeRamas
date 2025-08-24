print("archivo de prueba sobre el manejo de brancehs")
while True:
    print("---------MENU DE OPCIONES----------")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potenciacion")
    op_elegida = input(f"ELIJA UNA ACCION A REALIZAR (1-5): ")
    match op_elegida:
        case "1":
            a = int(input("ingrese primer numero: "))
            b= int( input("ingrese segundo numero: "))
            suma = a+b
            print(f"RESULTADO DE LA SUMA: {suma}")
