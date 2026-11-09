
from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:

    def __init__(self):
        self.pasajeros = []

    # 1. AÑADIR PASAJERO
    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("Ya existe un pasajero con ese número")
            return False

        self.pasajeros.append(pasajero)
        return True

    # 2. LISTAR PASAJEROS
    def listar(self):
        if not self.pasajeros:
            print("(lista vacía)")
            return

        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # 3. INSERTAR EN UNA POSICIÓN
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            return False

        if self.buscar(pasajero.numero) != -1:
            return False

        self.pasajeros.insert(posicion, pasajero)
        return True

    # 4. BÚSQUEDA LINEAL
    def buscar(self, numero):
        posiciones = [
            i for i, p in enumerate(self.pasajeros)
            if p.numero == numero
        ]

        if posiciones:
            return posiciones[0]

        return -1

    # 5. BÚSQUEDA BINARIA
    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]

        posicion = bisect_left(numeros, numero)

        if posicion < len(numeros):
            if numeros[posicion] == numero:
                return posicion

        return -1

    # 6. MODIFICAR PASAJERO
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento

        return True

    # 7. ELIMINAR POR POSICIÓN
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None

        eliminado = self.pasajeros.pop(posicion)
        return eliminado

    # 8. ELIMINAR POR NÚMERO
    def eliminar_por_valor(self, numero):
        if self.buscar(numero) == -1:
            return False

        self.pasajeros = [
            p for p in self.pasajeros
            if p.numero != numero
        ]

        return True

    # 9. ORDENAR ASCENDENTE
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    # 10. ORDENAR DESCENDENTE
    def ordenar_desc(self):
        self.pasajeros.sort(
            key=lambda p: p.numero,
            reverse=True
        )

    # 11. REVERSAR LA LISTA
    def reversar(self):
        self.pasajeros.reverse()

    # 12. COPIAR LA LISTA
    def copiar(self):
        nueva_lista = ListaPython()
        nueva_lista.pasajeros = self.pasajeros.copy()

        return nueva_lista

    # 13. OBTENER LONGITUD
    def longitud(self):
        return len(self.pasajeros)

    # 14. FILTRAR POR DESTINO
    def filtrar_por_destino(self, destino):
        encontrados = [
            p for p in self.pasajeros
            if p.destino.lower() == destino.lower()
        ]

        return encontrados

    # 15. PASAJEROS MAYORES DE EDAD
    def mayores_de_edad(self):
        mayores = [
            p for p in self.pasajeros
            if p.es_mayor_de_edad()
        ]

        return mayores