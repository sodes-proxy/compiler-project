errores = []

class Lexema:
    def __init__(self, line, tipo, value):
        self.line = line
        self.tipo = tipo
        self.value = value

    def __repr__(self):
        return f"{self.value} of type {self.tipo} found in {self.line}"

class Simbolo:
    def __init__(self, nombre, clase, tipo, dimension1, dimension2, avg, alp=[], uso=[]):
        self.nombre = nombre
        self.clase = clase
        self.tipo = tipo
        self.dimension1 = dimension1
        self.dimension2 = dimension2
        self.alp = alp # Lista de Simbolos
        self.uso = uso # Funciones

        # Valor
        if not avg == 0:
            self.avg = avg
        else:
            if tipo == "ALFABETICO": self.avg = ''
            elif tipo == "LOGICO": self.avg = True
            else: self.avg = 0

    def cambiar_valor(self, lexema):
        if self.tipo == lexema.tipo: self.avg = lexema.value
        else: errores.append(f"Error en linea {lexema.line}, tipo de dato distinto.")

    def __repr__(self):
        return f"{self.nombre}|{self.clase}|{self.tipo}|{self.dimension1}|{self.dimension2}|{self.avg}"

class Tabla_Simbolos:
    def __init__(self):
        self.simbolos = dict()
        self.parametros = dict()

    def agregar(self, simbolo):
        self.simbolos[simbolo.nombre] = simbolo

    def agregar_param(self, simbolo, funcion):
        if funcion in self.parametros.keys(): self.parametros[funcion].append(simbolo)
        else: self.parametros[funcion] = [simbolo]

    def buscar(self, name):
        if name in self.simbolos.keys(): return self.simbolos[name].avg
        else: return "Fail"