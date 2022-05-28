import ply.lex as lex
from tabulate import tabulate

# resultado del analisis
resultado_lexema = []
errores_lexema = []
libreria_lexema = []

terminadores = [',', ';', '(', ')', '[', ']', ':', '=', '+', '-', '^', '<', '>', '*', '/', '%']
term_largos = [':=', '<>', '<=', '>=']

reservada = (
    'TIPO_CONSTANTES',
    'TIPO_VARIABLES',
    'TIPO_REAL',
    'TIPO_ENTERO',
    'TIPO_LOGICO',
    'TIPO_ALFABETICO',
    'FUNCION',
    'INICIO',
    'FIN',
    'DE',
    'PROCEDIMIENTO',
    'REGRESA',
    'SI',
    'HACER',
    'SINO',
    'CUANDO',
    'EL',
    'VALOR',
    'SEA',
    'OTRO',
    'DESDE',
    'HASTA',
    'INCR',
    'DECR',
    'REPETIR',
    'QUE',
    'MIENTRAS',
    'SE',
    'CUMPLA',
    'CONTINUA',
    'INTERRUMPE',
    'LIMPIA',
    'LEE',
    'IMPRIME',
    'IMPRIMENL',
    'VERDADERO',
    'FALSO',
    'PROGRAMA_PUNTO'
)

tokens = reservada + (
    'ASIGNACION',
    'IDENTIFICADOR',

    #region Constantes
    'ENTERO',
    'REAL',
    'ALFABETICO',
    'LOGICO',
    #endregion

    #region Aritmeticos
    'MAS',
    'MENOS',
    'POR',
    'ENTRE',
    'MODULO',
    'EXPONENTE',
    #endregion

    #region Logicos
    'Y',
    'O',
    'NO',
    #endregion

    #region Relacionales
    'IGUAL',
    'NOIGUAL',
    'MENOR',
    'MAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    #endregion

    #region Delimitadores
    'PUNTO',
    'COMA',
    'PUNTOCOMA',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'DOSPUNTOS',
    'NEWLINE',
    'TAB'
    #endregion
)

#region Reservadas
def t_TIPO_CONSTANTES(t):
    r'^(?i)constantes$'
    return t

def t_TIPO_VARIABLES(t):
    r'^(?i)variables$'
    return t

def t_TIPO_REAL(t):
    r'^(?i)real$'
    return t

def t_TIPO_ENTERO(t):
    r'^(?i)entero$'
    return t

def t_TIPO_LOGICO(t):
    r'^(?i)logico$'
    return t

def t_TIPO_ALFABETICO(t):
    r'^(?i)alfabetico$'
    return t

def t_FUNCION(t):
    r'^(?i)funcion$'
    return t

def t_INICIO(t):
    r'^(?i)inicio$'
    return t

def t_FIN(t):
    r'^(?i)fin$'
    return t

def t_DE(t):
    r'^(?i)de$'
    return t

def t_PROCEDIMIENTO(t):
    r'^(?i)procedimiento$'
    return t

def t_REGRESA(t):
    r'^(?i)regresa$'
    return t

def t_SI(t):
    r'^(?i)si$'
    return t

def t_HACER(t):
   r'^(?i)hacer$'
   return t

def t_SINO(t):
   r'^(?i)sino$'
   return t

def t_CUANDO(t):
    r'^(?i)cuando$'
    return t

def t_EL(t):
    r'^(?i)el$'
    return t

def t_VALOR(t):
    r'^(?i)valor$'
    return t

def t_SEA(t):
    r'^(?i)sea$'
    return t

def t_OTRO(t):
    r'^(?i)otro$'
    return t

def t_DESDE(t):
    r'^(?i)desde$'
    return t

def t_HASTA(t):
    r'^(?i)hasta$'
    return t

def t_INCR(t):
    r'^(?i)incr$'
    return t

def t_DECR(t):
    r'^(?i)decr$'
    return t

def t_REPETIR(t):
    r'^(?i)repetir$'
    return t

def t_QUE(t):
    r'^(?i)que$'
    return t

def t_MIENTRAS(t):
    r'^(?i)mientras$'
    return t

def t_SE(t):
    r'^(?i)se$'
    return t

def t_CUMPLA(t):
    r'^(?i)cumpla$'
    return t

def t_CONTINUA(t):
    r'^(?i)continua$'
    return t

def t_INTERRUMPE(t):
    r'^(?i)interrumpe$'
    return t

def t_LIMPIA(t):
    r'^(?i)limpia$'
    return t

def t_LEE(t):
    r'^(?i)lee$'
    return t

def t_IMPRIME(t):
    r'^(?i)imprime$'
    return t

def t_IMPRIMENL(t):
    r'^(?i)imprimenl$'
    return t

def t_VERDADERO(t):
    r'^(?i)verdadero$'
    return t

def t_FALSO(t):
    r'^(?i)falso$'
    return t

def t_PROGRAMA_PUNTO(t):
    r'^(?i)programa\.$'
    return t
#endregion

t_ASIGNACION = r':='

def t_IDENTIFICADOR(t):
    r'^[A-Z][A-Z\d_]*$'
    return t

#region Aritmeticos
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ENTRE = r'/'
t_MODULO = r'\%'

def t_EXPONENTE(t):
    r'\^'
    return t
#endregion

#region Logicos
def t_Y(t): 
    r'y'
    return t

t_O = r'o'
t_NO = r'no'
#endregion

#region Relacionales
t_IGUAL = r'='
t_NOIGUAL = r'<>'
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
#endregion

#region Delimitadores
t_PUNTO = r'\.'
t_COMA = r','
t_PUNTOCOMA = r';'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_DOSPUNTOS = r':'
t_NEWLINE = r'\n'
t_TAB = r'\t'
#endregion

#region Constantes
def t_ENTERO(t):
    r'^[-+]?\d+$'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'^[-+]?\d*.?\d+$'
    t.value = float(t.value)
    return t

def t_ALFABETICO(t):
   r'^(\"|\').*(\"|\')$'
   return t

def t_LOGICO(t):
   r'^(?i)(verdadero|falso)$'
   return t
#endregion

def t_error( t):
    global errores_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    errores_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data, line):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(line),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
        libreria_lexema.append([str(tok.type), str(tok.value)])
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

def get_words(line):
    words = []
    temp_word = ''
    flag_str = False
    str_starter = ""
    for pos, c in enumerate(line):
        if not flag_str:
            if len(temp_word) < 2 and temp_word in terminadores:
                test = temp_word + c
                if test in term_largos: 
                    words.append(test)
                    temp_word = ''
                else: 
                    words.append(temp_word)
                    temp_word = ''
                    if not c == ' ':
                        temp_word += c
            else:
                if c in terminadores or c == ' ':
                    words.append(temp_word)
                    temp_word = ''

                if not c == ' ':
                    temp_word += c

            if pos == len(line) - 1: words.append(temp_word)

            if c == "\'" or c == "\"": 
                flag_str = True
                str_starter = c
        else:
            temp_word += c
            if c == str_starter:
                flag_str = False
                words.append(temp_word)
                temp_word = ''
    return words

def general_type(lex_type):
    tipo = ""
    if lex_type in reservada: tipo = "<PalRes>"
    elif lex_type == "ASIGNACION": tipo = "<OpAsig>"
    elif lex_type in ['PUNTO', 'COMA', 'PUNTOCOMA', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'DOSPUNTOS', 'NEWLINE', 'TAB']: tipo = "<Delim>"
    elif lex_type in ['MAS', 'MENOS', 'POR', 'ENTRE', 'MODULO', 'EXPONENTE']: tipo = "<OpArit>"
    elif lex_type in ['IGUAL', 'NOIGUAL', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL']: tipo = "<OpRel>"
    elif lex_type in ['Y', 'O', 'NO']: tipo = "<OpLog>"
    elif lex_type == "IDENTIFICADOR": tipo = "<Ident>"
    elif lex_type == "ENTERO": tipo = "<CteEnt>"
    elif lex_type == "REAL": tipo = "<CteReal>"
    elif lex_type == "ALFABETICO": tipo = "<CteAlfa>"
    elif lex_type == "LOGICA": tipo = "<CteLog>"
    else: tipo = "<Error>"
    return tipo


def write_lex_file(filename):
    global libreria_lexema

    table = [ ["Lexema", "Token"] ]
    for lexema in libreria_lexema:
        table.append([lexema[1], general_type(lexema[0])])
    file = open(filename + ".lex", "w")
    file.write(tabulate(table, headers="firstrow", tablefmt="psql"))
    file.close()
    

if __name__ == '__main__':
    filename = "examen"

    data = open(filename + ".up").read().split("\n")
    for pos, line in enumerate(data):
        for word in get_words(line):
            prueba(word, pos+1)
    
    write_lex_file(filename)