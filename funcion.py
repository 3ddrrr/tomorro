import time

# Lista para almacenar los trabajadores
listatrabajadores = []

def registrarTrabajador():
    print("Registrar trabajador. \nSolicitud de datos personales...")
    time.sleep(1)
    nombre=input("Ingrese nombre del trabajador: ")
    apellido=input("Ingrese apellido del trabajador: ")
    cargo=input("Ingrese su cargo: CEO/Analista de datos/Desarrollador --> ")
    sueldo=input("Ingrese su sueldo bruto: ")
    listatrabajadores.append([nombre, apellido, cargo, sueldo])
    print("Trabajador agregado correctamente.\n")

def listar():
    print("\nLista de Trabajadores:")
    for trabajador in listatrabajadores:
        print(f"Nombre: {trabajador[0]}, Apellido: {trabajador[1]}, Cargo: {trabajador[2]}, Sueldo: {trabajador[3]}")
    print()

def imprimir():
    with open('archivo_trabajadores.txt','w',encoding='utf-8') as archivo:
        archivo.write("Nombre | Apellido | Cargo | Sueldo\n")
        for trabajador in listatrabajadores:
            archivo.write(f"{trabajador[0]} | {trabajador[1]} | {trabajador[2]} | {trabajador[3]}\n")
    print("Archivo 'archivo_trabajadores.txt' generado correctamente.\n")


def menu():
    while True:
        print("1.- Registrar trabajador")
        print("2.- Listar trabajadores")
        print("3.- Imprimir planilla de sueldos")
        print("4.- Salir del programa")
        opcion=int(input("Seleccione la opción que desea: "))
        
        if opcion==1:
            registrarTrabajador()
        elif opcion==2:
            listar()
        elif opcion==3:
            imprimir()
        elif opcion==4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.\n")
