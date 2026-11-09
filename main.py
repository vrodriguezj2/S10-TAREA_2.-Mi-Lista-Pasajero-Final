
from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython


lista1 = MiLista(10)
lista2 = ListaPython()


# FUNCIONES DE APOYO

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def leer_pasajero():
    numero = leer_entero("N.º de pasajero: ")
    nombre = input("Nombre: ").strip()
    cedula = input("Cédula: ").strip()
    edad = leer_entero("Edad: ")
    fecha = input("Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("Destino: ").strip()
    asiento = input("Asiento: ").strip().upper()

    return Pasajero(numero, nombre, cedula, edad,
                    fecha, destino, asiento)


def cargar_datos_prueba(lista):
    pasajeros = [
        Pasajero(1005, "Diana", "0923456789", 22,
                 "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28,
                 "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35,
                 "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16,
                 "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41,
                 "2026-11-22", "Lima", "01A")
    ]

    agregados = 0

    for pasajero in pasajeros:
        if lista.añadir(pasajero):
            agregados += 1

    print("Datos de prueba cargados.")
    print("Pasajeros agregados:", agregados)


def mostrar_opciones(titulo, extras=False):
    print("\n==========", titulo, "==========")
    print("1. Añadir pasajero")
    print("2. Listar pasajeros")
    print("3. Insertar en posición")
    print("4. Buscar (lineal)")
    print("5. Buscar (binaria)")
    print("6. Modificar pasajero")
    print("7. Eliminar por posición")
    print("8. Eliminar por número")
    print("9. Ordenar ascendente")
    print("10. Ordenar descendente")
    print("11. Reversar lista")
    print("12. Copiar lista")
    print("13. Longitud de la lista")

    if extras:
        print("14. Filtrar por destino")
        print("15. Mayores de edad")

    print("C. Cargar datos de prueba")
    print("0. Volver")


# COMPROBAR SI LA LISTA ESTA ORDENADA

def esta_ordenada(lista):
    if isinstance(lista, MiLista):
        pasajeros = lista.datos
    else:
        pasajeros = lista.pasajeros

    for i in range(lista.longitud() - 1):
        if pasajeros[i].numero > pasajeros[i + 1].numero:
            return False

    return True


# OPERACIONES DE LOS DOS MENUS

def menu_operaciones(lista, titulo, extras=False):

    while True:
        mostrar_opciones(titulo, extras)
        op = input("Opción: ").strip().upper()

        # 1. AÑADIR
        if op == "1":
            pasajero = leer_pasajero()

            if lista.añadir(pasajero):
                print("Pasajero añadido correctamente.")
            else:
                print("No se pudo añadir el pasajero.")

        # 2. LISTAR
        elif op == "2":
            lista.listar()

        # 3. INSERTAR
        elif op == "3":
            posicion = leer_entero("Posición: ")
            pasajero = leer_pasajero()

            if lista.insertar(posicion, pasajero):
                print("Pasajero insertado correctamente.")
            else:
                print("No se pudo insertar el pasajero.")

        # 4. BÚSQUEDA LINEAL
        elif op == "4":
            numero = leer_entero("Número de pasajero: ")
            posicion = lista.buscar(numero)

            if posicion != -1:
                print("Encontrado en la posición:", posicion)

                if isinstance(lista, MiLista):
                    print(lista.datos[posicion])
                else:
                    print(lista.pasajeros[posicion])
            else:
                print("El pasajero no existe.")

        # 5. BÚSQUEDA BINARIA
        elif op == "5":
            if not esta_ordenada(lista):
                print("Primero debe ordenar la lista de forma ascendente.")
            else:
                numero = leer_entero("Número de pasajero: ")
                posicion = lista.buscar_binaria(numero)

                if posicion != -1:
                    print("Encontrado en la posición:", posicion)

                    if isinstance(lista, MiLista):
                        print(lista.datos[posicion])
                    else:
                        print(lista.pasajeros[posicion])
                else:
                    print("El pasajero no existe.")

        # 6. MODIFICAR
        elif op == "6":
            numero = leer_entero("Número de pasajero: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if lista.modificar(numero, destino, asiento):
                print("Pasajero modificado correctamente.")
            else:
                print("El pasajero no existe.")

        # 7. ELIMINAR POR POSICIÓN
        elif op == "7":
            posicion = leer_entero("Posición a eliminar: ")
            eliminado = lista.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print("Pasajero eliminado:")
                print(eliminado)
            else:
                print("Posición no válida.")

        # 8. ELIMINAR POR NÚMERO
        elif op == "8":
            numero = leer_entero("Número de pasajero: ")

            if lista.eliminar_por_valor(numero):
                print("Pasajero eliminado correctamente.")
            else:
                print("El pasajero no existe.")

        # 9. ORDENAR ASCENDENTE
        elif op == "9":
            lista.ordenar_asc()
            print("Lista ordenada de menor a mayor.")
            lista.listar()

        # 10. ORDENAR DESCENDENTE
        elif op == "10":
            lista.ordenar_desc()
            print("Lista ordenada de mayor a menor.")
            lista.listar()

        # 11. REVERSAR
        elif op == "11":
            lista.reversar()
            print("Lista reversada correctamente.")
            lista.listar()

        # 12. COPIAR
        elif op == "12":
            copia = lista.copiar()

            print("\nLISTA ORIGINAL:")
            lista.listar()

            print("\nLISTA COPIADA:")
            copia.listar()

            print("\nREVERSANDO LA COPIA:")
            copia.reversar()
            copia.listar()

            print("\nLISTA ORIGINAL SIN CAMBIOS:")
            lista.listar()

        # 13. LONGITUD
        elif op == "13":
            print("Cantidad de pasajeros:", lista.longitud())

        # 14. FILTRAR POR DESTINO
        elif op == "14" and extras:
            destino = input("Destino a buscar: ").strip()
            encontrados = lista.filtrar_por_destino(destino)

            if encontrados:
                print("Pasajeros encontrados:")

                for pasajero in encontrados:
                    print(pasajero)
            else:
                print("No hay pasajeros con ese destino.")

        # 15. MAYORES DE EDAD
        elif op == "15" and extras:
            mayores = lista.mayores_de_edad()

            if mayores:
                print("Pasajeros mayores de edad:")

                for pasajero in mayores:
                    print(pasajero)
            else:
                print("No hay pasajeros mayores de edad.")

        # C. CARGAR DATOS
        elif op == "C":
            cargar_datos_prueba(lista)

        # 0. VOLVER
        elif op == "0":
            break

        else:
            print("Opción no válida.")


# MENU 1 - MILISTA

def menu_lista1():
    menu_operaciones(lista1, "MENÚ 1 - MiLista")


# MENU 2 - LISTA DE PYTHON

def menu_lista2():
    menu_operaciones(
        lista2,
        "MENÚ 2 - list de Python",
        extras=True
    )


# MENU PRINCIPAL

def main():
    while True:
        print("\n===== SISTEMA DE PASAJEROS =====")
        print("1. Menú 1 - MiLista")
        print("2. Menú 2 - list de Python")
        print("3. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            menu_lista1()

        elif op == "2":
            menu_lista2()

        elif op == "3":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()