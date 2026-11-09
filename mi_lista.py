
from pasajero import Pasajero


class MiLista:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    # 1. AÑADIR PASAJERO
    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("Ya existe un pasajero con ese número")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # 2. LISTAR PASAJEROS
    def listar(self):
        if self.cantidad == 0:
            print("(lista vacía)")
            return

        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

    # 3. INSERTAR EN UNA POSICIÓN
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            return False

        if posicion < 0 or posicion > self.cantidad:
            return False

        if self.buscar(pasajero.numero) != -1:
            return False

        for i in range(self.cantidad, posicion, -1):
            self.datos[i] = self.datos[i - 1]

        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # 4. BÚSQUEDA LINEAL
    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i

        return -1

    # 5. BÚSQUEDA BINARIA
    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1

        while izq <= der:
            medio = (izq + der) // 2

            if self.datos[medio].numero == numero:
                return medio

            elif self.datos[medio].numero < numero:
                izq = medio + 1

            else:
                der = medio - 1

        return -1

    # 6. MODIFICAR PASAJERO
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    # 7. ELIMINAR POR POSICIÓN
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None

        eliminado = self.datos[posicion]

        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return eliminado

    # 8. ELIMINAR POR NÚMERO
    def eliminar_por_valor(self, numero):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.eliminar_por_posicion(posicion)
        return True

    # 9. ORDENAR ASCENDENTE
    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # 10. ORDENAR DESCENDENTE
    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # 11. REVERSAR LA LISTA
    def reversar(self):
        izq = 0
        der = self.cantidad - 1

        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux

            izq = izq + 1
            der = der - 1

    # 12. COPIAR LA LISTA
    def copiar(self):
        nueva_lista = MiLista(self.capacidad)

        for i in range(self.cantidad):
            nueva_lista.añadir(self.datos[i])

        return nueva_lista

    # 13. OBTENER LONGITUD
    def longitud(self):
        return self.cantidad
