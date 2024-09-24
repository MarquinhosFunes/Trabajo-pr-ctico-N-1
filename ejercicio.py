estudiantes = [
    {'nombre': 'Juan', 'apellido': 'Garcia','edad': '19', 'especialidad': 'Informatica'},
    {'nombre': 'Mateo', 'apellido': 'Fernandez','edad': '18', 'especialidad': 'Informatica'},
    {'nombre': 'Nicolas', 'apellido': 'Rodriguez','edad': '18', 'especialidad': 'Construcciones'},
    {'nombre': 'Lucio', 'apellido': 'Gonzalez','edad': '17', 'especialidad': 'Informatica'},
    {'nombre': 'Martina', 'apellido': 'Diaz','edad': '18', 'especialidad': 'Electronica'},
    {'nombre': 'Matias', 'apellido': 'Sanchez','edad': '17', 'especialidad': 'Construcciones'},
    {'nombre': 'Lucia', 'apellido': 'Martinez','edad': '19', 'especialidad': 'Informatica'},
    {'nombre': 'Rodrigo', 'apellido': 'Aguilar','edad': '18', 'especialidad': 'Informatica'},
    {'nombre': 'Gustavo', 'apellido': 'Delgado','edad': '18', 'especialidad': 'Electronica'},
    {'nombre': 'Hernesto', 'apellido': 'Herrera','edad': '20', 'especialidad': 'Informatica'}
]

def listar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}, Edad: {estudiante['edad']}, Especialidad: {estudiante['especialidad']}")

def actualizar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a actualizar: ")
    apellido = input("Ingrese el apellido del estudiante a actualizar: ")
    
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre and estudiante['apellido'] == apellido:
            campo = input("¿Qué desea actualizar (edad/especialidad)? ").lower()
            if campo in ['edad', 'especialidad']:
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                estudiante[campo] = nuevo_valor
                print("Información actualizada con éxito.")
                return
    
    print("Estudiante no encontrado.")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    apellido = input("Ingrese el apellido del estudiante a eliminar: ")
    
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre and estudiante['apellido'] == apellido:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return
    
    print("Estudiante no encontrado.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Listar estudiantes")
        print("2. Actualizar información de estudiante")
        print("3. Eliminar estudiante")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            listar_estudiantes()
        elif opcion == '2':
            actualizar_estudiante()
        elif opcion == '3':
            eliminar_estudiante()
        elif opcion == '4':
            print("El programa finalizo.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()


