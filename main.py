
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultados(self):
        if self.nota >= 70:
            print("aprovado")
        else:
            print("suspendido")

alumno1 = Alumno("Juan", 60)
alumno2 = Alumno("Carlos",80)

alumno1.datos()
alumno1.resultados()
alumno2.datos()
alumno2.resultados()