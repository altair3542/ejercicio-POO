# Ejercicio Completo: Sistema de Gestión de Biblioteca
# Descripción:
# Crear un sistema de gestión de biblioteca que permita manejar libros y revistas, gestionar usuarios y préstamos, y realizar búsquedas en el catálogo de publicaciones. El sistema debe utilizar los principios de programación orientada a objetos: encapsulamiento, herencia y polimorfismo.
# Requisitos:
# 1.	Encapsulamiento: Usa atributos protegidos para manejar los datos de las publicaciones.
# 2.	Herencia: Crea clases Libro y Revista que hereden de la clase Publicacion.
# 3.	Polimorfismo: Implementa métodos polimórficos para mostrar información específica de cada tipo de publicación.
# 4.	Gestión de Préstamos: Implementa una clase Usuario que pueda tomar prestadas publicaciones.
# 5.	Búsquedas: Permite buscar publicaciones por título, autor o año.

#crear una clase llamada Publicación.

class Publicacion:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio

    def mostrar_informacion(self):
        print(f"Publicacion: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}")



class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self.__genero = genero

    def mostrar_informacion(self):
        print(f"Libro: {self.get_titulo()}, Autor: {self.get_autor()}, Año: {self.get_anio()}, Género: {self.__genero}")

class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, numero_edicion):
        super().__init__(titulo, autor, anio)
        self.__numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"Revista: {self.get_titulo()}, Autor: {self.get_autor()}, Año: {self.get_anio()}, Número de publicacion: {self.__numero_edicion}")


# clase usuario

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__prestamos = []

    def tomar_prestado(self, publicacion):
        self.__prestamos.append(publicacion)
        print(f"{self.nombre} ha tomado prestado '{publicacion.get_titulo()}'")

    def devolver_publicacion(self, publicacion):
        if publicacion in self.__prestamos:
            self.__prestamos.remove(publicacion)
            print(f"{self.nombre} ha devuelto '{publicacion.get_titulo()}'")
        else:
            print(f"{self.nombre} no tiene prestado '{publicacion.get_titulo()}")

    def mostrar_prestamos(self):
        print(f"{self.nombre} ha tomado prestados los siguientes titulos")
        for publicacion in self.__prestamos:
            publicacion.mostrar_informacion()

#clase bliblioteca para gestionar publicaciones y usuarios

class Biblioteca:
    def __init__(self):
        self.__catalogo = []
        self.__usuarios = []

    def agregar_publicacion(self, publicacion):
        self.__catalogo.append(publicacion)
        print(f"Se ha agregado '{publicacion.get_titulo()}' al catalogo")

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' ha sido registrado")

    def buscar_por_titulo(self, titulo):
        resultados = [pub for pub in self.__catalogo if pub.get_titulo().lower() == titulo.lower()]
        self.__mostrar_resultados_busqueda(resultados)

    def buscar_por_autor(self, autor):
        resultados = [pub for pub in self.__catalogo if pub.get_autor().lower() == autor.lower()]
        self.__mostrar_resultados_busqueda(resultados)

    def buscar_por_anio(self, anio):
        resultados = [pub for pub in self.__catalogo if pub.get_anio() == anio]
        self.__mostrar_resultados_busqueda(resultados)

    def __mostrar_resultados_busqueda(self, resultados):
        if resultados:
            print("resultados de la busqueda")
            for pub in resultados:
                pub.mostrar_informacion()
        else:
            print("no se han encontrado coincidencias")

# funcion para mostrar informacion de cualquier publicacion

def mostrar_publicacion(publicacion):
    publicacion.mostrar_informacion()

#crear instancias de libro y revista

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 1943, "ficcion")

revista1 = Revista("National Geographic", "varios autores", 2021, 7)

libro2 = Libro("1984", "George Orwell", 1949, "Distopía")

revista2 = Revista("Science", "Varios Autores", 2023, 12)

#creamos instancias de usuarios.
usuario1 = Usuario("Santiago Serna")
usuario2 = Usuario("Camila Usma")

#creamos una instancia de biblioteca.

biblioteca = Biblioteca()

#Agregar publicaciones al catalogo de la biblioteca.
biblioteca.agregar_publicacion(libro1)
biblioteca.agregar_publicacion(revista1)
biblioteca.agregar_publicacion(libro2)
biblioteca.agregar_publicacion(revista2)

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Mostrar información de publicaciones
mostrar_publicacion(libro1)
mostrar_publicacion(revista1)

# Gestionar préstamos
usuario1.tomar_prestado(libro1)
usuario1.tomar_prestado(revista2)
usuario1.mostrar_prestamos()
usuario1.devolver_publicacion(libro1)
usuario1.mostrar_prestamos()

# Búsquedas en el catálogo de la biblioteca
print("\nBusqueda por titulo:")
biblioteca.buscar_por_titulo("1984")
print("\nBusqueda por autor:")
biblioteca.buscar_por_autor("Antoine de Saint-Exupéry")
print("\nBúsqueda por año:")
biblioteca.buscar_por_anio(2021)
