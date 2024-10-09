
def cargar_paciente(pacientes):
    historia_clinica = int(input("Ingrese el número de historia clínica: "))
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    diagnostico = input("Ingrese el diagnóstico del paciente: ")
    dias_internacion = int(input("Ingrese la cantidad de días de internación: "))
    
    paciente = [historia_clinica, nombre, edad, diagnostico, dias_internacion]
    pacientes.append(paciente)
    print(f"Paciente {nombre} cargado con éxito")

def buscar_paciente(pacientes, historia_clinica):
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            return paciente
    return print("paciente no encontrado")

def paciente_mas_dias_internacion(pacientes):
    if not pacientes:#caso de no encontrar el paciente
        return None
    mas_dias_i = pacientes[0][4]# tomo al primer paciente como el que tiene mas dias internado primera fila cuarta columna
    paciente_max = pacientes[0]#etiqueto
    for paciente in pacientes:
        if paciente[4] > mas_dias_i:
            mas_dias_i = paciente[4]
            paciente_max = paciente
    return paciente_max

def paciente_menos_dias_internacion(pacientes):
    if not pacientes:
        return None
    min_dias_i = pacientes[0][4]
    paciente_min_i = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < min_dias_i:
            min_dias_i = paciente[4]
            paciente_min_i = paciente
    return paciente_min_i

def ordenamiento_por_h_clinica(pacientes):
    len = len(pacientes)
    for i in range(len):
        for j in range(0, len-i-1):
            if pacientes[j][0] > pacientes[j+1][0]:  # Ordena por historia clínica que esta en el primer indice
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j] #cambio de posicion j y j+1

def mostrar_menu():
    print("\n Menú del Sistema de Gestión de Pacientes ")
    print("1. Cargar paciente")
    print("2. Buscar paciente por Historia Clínica")
    print("3. Paciente con más días de internación")
    print("4. Paciente con menos días de internación")
    print("5. Ordenar pacientes por número de historia clínica")
    print("6. Salir")

# Funciones para las operaciones del sistema
def cargar_paciente(pacientes):
    historia_clinica = int(input("Ingrese el número de historia clínica: "))
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    diagnostico = input("Ingrese el diagnóstico del paciente: ")
    dias_internacion = int(input("Ingrese la cantidad de días de internación: "))
    paciente = [historia_clinica, nombre, edad, diagnostico, dias_internacion]
    pacientes.append(paciente)
    print(f"Paciente {nombre} cargado con éxito.\n")

def buscar_paciente_por_historia(pacientes, historia_clinica):
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            return paciente
    return None

def buscar_paciente_por_nombre(pacientes, nombre):
    for paciente in pacientes:
        if paciente[1].strip().lower() == nombre.strip().lower():  # Comparar ignorando mayúsculas/minúsculas
            return paciente
    return None

def paciente_mas_dias_internacion(pacientes):
    if not pacientes:
        return None
    max_dias = pacientes[0][4]
    paciente_max = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > max_dias:
            max_dias = paciente[4]
            paciente_max = paciente
    return paciente_max

def paciente_menos_dias_internacion(pacientes):
    if not pacientes:
        return None
    min_dias = pacientes[0][4]
    paciente_min = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < min_dias:
            min_dias = paciente[4]
            paciente_min = paciente
    return paciente_min

def ordenamiento_por_h_clinica(pacientes):
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][0] > pacientes[j+1][0]:  # Ordenar por historia clínica
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
            print("\nDespués de ordenar por historia clinica")
            for paciente in pacientes:
               print(pacientes)

            

def mostrar_menu():
    print("\n--- Menú del Sistema de Gestión de Pacientes ---")
    print("1. Cargar paciente")
    print("2. Buscar paciente por Historia Clínica")
    print("3. Buscar paciente por Nombre")
    print("4. Paciente con más días de internación")
    print("5. Paciente con menos días de internación")
    print("6. Ordenar pacientes por número de historia clínica")
    print("7. Salir")

# Programa principal
def gestion():
    pacientes = []  

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_paciente(pacientes)
        elif opcion == "2":
            historia_clinica = int(input("Ingrese el número de historia clínica a buscar: "))
            paciente = buscar_paciente_por_historia(pacientes, historia_clinica)
            if paciente:
                print(f"Paciente encontrado: {paciente}")
            else:
                print("Paciente no encontrado.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del paciente a buscar: ")
            paciente = buscar_paciente_por_nombre(pacientes, nombre)
            if paciente:
                print(f"Paciente encontrado: {paciente}")
            else:
                print("Paciente no encontrado.")
        elif opcion == "4":
            paciente = paciente_mas_dias_internacion(pacientes)
            if paciente:
                print(f"Paciente con más días de internación: {paciente}")
            else:
                print("No hay pacientes registrados.")
        elif opcion == "5":
            paciente = paciente_menos_dias_internacion(pacientes)
            if paciente:
                print(f"Paciente con menos días de internación: {paciente}")
            else:
                print("No hay pacientes registrados.")
        elif opcion == "6":
            ordenamiento_por_h_clinica(pacientes)
            

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


gestion()
