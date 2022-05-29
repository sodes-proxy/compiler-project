from re import L


errores = []

class Lexema:
    def __init__(self, line, tipo, value):
        self.line = line
        self.tipo = tipo
        self.value = value

    def __repr__(self):
        return f"{self.value} of type {self.tipo} found in {self.line}"

class Simbolo:
    def __init__(self, nombre, clase, tipo, dimension1, dimension2, uso='#'):
        self.nombre = nombre
        self.clase = clase
        self.tipo = tipo
        self.dimension1 = dimension1
        self.dimension2 = dimension2
        self.alp = []
        self.uso = uso

    def __repr__(self):
        alp = ''
        for sim in self.alp:
            alp += f'{sim.clase},{sim.tipo},{sim.dimension1},{sim.dimension2},{sim.uso},'
        return f'{self.nombre},{self.clase},{self.tipo},{self.dimension1},{self.dimension2},{alp}{self.uso}'

class Tabla_Simbolos:
    def __init__(self):
        self.simbolos = dict()
        self.parametros = dict()
        self.__etiqueta = 0

    def agregar(self, simbolo):
        self.simbolos[simbolo.nombre] = simbolo

    def agregar_etiqueta(self, simbolo):
        self.__etiqueta += 1
        simbolo.nombre = "_E" + str(self.__etiqueta)
        self.agregar(simbolo)

    def agregar_param(self, simbolo):
        if simbolo.nombre in self.simbolos.keys(): self.simbolos[simbolo.nombre].alp.append(simbolo)
        else: 
            self.agregar(Simbolo(simbolo.nombre, "I", "I", 0, 0))
            self.agregar_param(simbolo)

    def buscar(self, name):
        if name in self.simbolos.keys(): return self.simbolos[name]
        else: return False

    def print(self):
        for sim in self.simbolos.keys():
            print(self.simbolos[sim])