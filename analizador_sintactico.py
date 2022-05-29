from sympy import E, false
from lexema import Lexema, Simbolo, Tabla_Simbolos
from pprint import pprint


BLOQUES = {"TIPO_CONSTANTES":"CONSTANTE", "TIPO_VARIABLES":"VARIABLE", "FUNCION": "FUNC", "PROCEDIMIENTO":"PROC", "INICIO": "BLOQUE", "FIN": "BLOQUE2"}
TIPOS = {"TIPO_ENTERO":"E", "TIPO_REAL":"R", "TIPO_ALFABETICO":"A", "TIPO_LOGICO":"L"}
T_VAR = ["ENTERO", "ALFABETICO", "REAL", "LOGICO"]

tabla = Tabla_Simbolos()

def variable_ident(texto, temp_lex, pos, tipo, funcion='', local=''):
    global tabla

    flag = True
    if "CORIZQ" in texto:
        if texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER CORIZQ IDENTIFICADOR CORDER ":
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER CORIZQ ENTERO CORDER ": 
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER CORIZQ IDENTIFICADOR CORDER ": 
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value))
        elif texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER CORIZQ ENTERO CORDER ": 
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value))
        elif texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER ":
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2].value, 0, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2].value, 0))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER ": 
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, temp_lex[pos + 2], 0, funcion))
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, temp_lex[pos + 2], 0))
        else: flag = False
    elif texto == "IDENTIFICADOR ": 
        if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "P", tipo, 0, 0, funcion))
        else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "V", tipo, 0, 0))
    else: flag = False

    return flag

def asignar_constantes(op, lex, esLocal=False):
    global tabla

    if op == "IDENTIFICADOR ASIGNACION REAL PUNTOCOMA ": 
        tabla.agregar(Simbolo(lex[0].value, "C", "R", 0, 0))
    elif op == "IDENTIFICADOR ASIGNACION ENTERO PUNTOCOMA ": 
        tabla.agregar(Simbolo(lex[0].value, "C", "E", 0, 0))
    elif op == "IDENTIFICADOR ASIGNACION LOGICO PUNTOCOMA ": 
        tabla.agregar(Simbolo(lex[0].value, "C", "L", 0, 0))
    elif op == "IDENTIFICADOR ASIGNACION ALFABETICO PUNTOCOMA ":
        tabla.agregar(Simbolo(lex[0].value, "C", "A", 0, 0))
    else: return False
    return True

def asignar_variables(op, lex, funcion='', local=''):
    global tabla

    flag = True
    if "DOSPUNTOS" in op:
        info = op.split("DOSPUNTOS ")
        if info[1] in [f"{key} PUNTOCOMA " for key in TIPOS.keys()]:
            tipo = TIPOS[info[1].split(" ")[0]]
            if "COMA" in info[0]:
                variables = info[0].split("COMA ")
                current = 0
                for variable in variables:
                    if not variable_ident(variable, lex, current, tipo, funcion=funcion, local=local): flag = False
                    current += len(variable.split(" "))
            else: 
                if not variable_ident(info[0], lex, 0, tipo, funcion=funcion, local=local): flag = False
        else: flag = False
    else: flag = False
    return flag

def asignar_func(op, lex):
    global tabla

    flag = True
    if op in [f"IDENTIFICADOR PARIZQ PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
        tabla.agregar(Simbolo(lex[0].value, "F", TIPOS[lex[-2].tipo], lex[0].line - 2, 0))
    elif op in [f"FUNCION IDENTIFICADOR PARIZQ PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
        tabla.agregar(Simbolo(lex[1].value, "F", TIPOS[lex[-2].tipo], lex[0].line - 2, 0))
    else:
        info1 = op.split("PARIZQ IDENTIFICADOR")
        info2 = info1[1].split("PARDER DOSPUNTOS")
        inicio = info1[0] + "PARIZQ "
        medio = "IDENTIFICADOR" + info2[0] + "PUNTOCOMA "
        final = "PARDER DOSPUNTOS" + info2[1]

        if inicio.split(" ")[0] == "FUNCION": 
            param_start = 3
            nombre = lex[1].value
        else: 
            param_start = 2
            nombre = lex[0].value

        simbol = Simbolo(nombre, 'F', TIPOS[lex[-2].tipo], lex[0].line - 2, 0)
        
        if not inicio in ["FUNCION IDENTIFICADOR PARIZQ ", "IDENTIFICADOR PARIZQ "]:
            print("Error P")
            flag = False
        elif not asignar_variables(medio, lex[param_start:], funcion=simbol.nombre):
            print("Error M")
            flag = False
        elif final not in [f"PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
            print("Error F")
            flag = False

        if flag:
            tabla.agregar(simbol)
    return flag

def asignar_proc(op, lex):
    global tabla

    flag = True
    if op == "IDENTIFICADOR PARIZQ PARDER PUNTOCOMA ":
        tabla.agregar(Simbolo(lex[0].value, "P", "I", lex[0].line - 2, 0))
    elif op == "PROCEDIMIENTO IDENTIFICADOR PARIZQ PARDER PUNTOCOMA ":
        tabla.agregar(Simbolo(lex[1].value, "P", "I", lex[0].line - 2, 0))
    else:
        info1 = op.split("PARIZQ IDENTIFICADOR")
        info2 = info1[1].split("PARDER PUNTOCOMA")
        inicio = info1[0] + "PARIZQ "
        medio = "IDENTIFICADOR" + info2[0] + "PUNTOCOMA "
        final = "PARDER PUNTOCOMA" + info2[1] 

        if inicio.split(" ")[0] == "PROCEDIMIENTO": 
            param_start = 3
            nombre = lex[1].value
        else: 
            param_start = 2
            nombre = lex[0].value

        simbol = Simbolo(nombre, 'P', 'I', lex[0].line - 2, 0)

        if not inicio in ["PROCEDIMIENTO IDENTIFICADOR PARIZQ ", "IDENTIFICADOR PARIZQ "]:
            print("Error P")
            flag = False
        elif not asignar_variables(medio, lex[param_start:], funcion=simbol.nombre): 
            print("Error M")
            flag = False
        elif final not in [f"PARDER PUNTOCOMA "]: 
            print("Error F")
            flag = False

        if flag:
            tabla.agregar(simbol)
    return flag

def expresion_booleana(op):
    flag = True
    expresiones = []
    split1 = op.split(" Y ")
    for split in split1:
        for expr in split.split(" O "):
            expresiones.append(expr)

    for expr in expresiones:
        temp_flag = False
        if not expr: continue
        if expr in [f"IDENTIFICADOR NOIGUAL {key}" for key in T_VAR] + [f"IDENTIFICADOR NOIGUAL {key} " for key in T_VAR]: temp_flag = True
        elif expr in [f"IDENTIFICADOR IGUAL {key}" for key in T_VAR] + [f"IDENTIFICADOR IGUAL {key} " for key in T_VAR]: temp_flag = True
        elif expr in [f"IDENTIFICADOR MENOR {key}" for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]] + [f"IDENTIFICADOR MENOR {key} " for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]]: temp_flag = True
        elif expr in [f"IDENTIFICADOR MAYOR {key}" for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]] + [f"IDENTIFICADOR MAYOR {key} " for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]]: temp_flag = True
        elif expr in [f"IDENTIFICADOR MENORIGUAL {key}" for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]] + [f"IDENTIFICADOR MENORIGUAL {key} " for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]]: temp_flag = True
        elif expr in [f"IDENTIFICADOR MAYORIGUAL {key}" for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]] + [f"IDENTIFICADOR MAYORIGUAL {key} " for key in T_VAR if key not in ["LOGICO", "ALFABETICO"]]: temp_flag = True
        elif expr in ["NO IDENTIFICADOR", "NO IDENTIFICADOR "]: temp_flag = True

        if not temp_flag:
            flag = False
            break
    return flag

    
    return flag

def asignar_bloque(op, lex):
    flag = True

    info = op.split(" ")
    if info[0] == "PROCEDIMIENTO":
        if not tabla.buscar(lex[1].value):
            op += "PUNTOCOMA "
            lex.append(Lexema(lex[0].line, "PUNTOCOMA", ";"))
            flag = asignar_proc(op, lex)
    elif info[0] == "FUNCION":
        if not tabla.buscar(lex[1].value):
            op += "PUNTOCOMA "
            lex.append(Lexema(lex[0].line, "PUNTOCOMA", ";"))
            flag = asignar_func(op, lex)
    elif info[0] == "VARIABLES": return # Variables locales
    elif info[0] == "REPETIR":
        if op == "REPETIR ": tabla.agregar_etiqueta(Simbolo('', "I", "I", lex[0].line, 0))
        else: flag = False
    elif info[0] == "CUANDO":
        if op == "CUANDO EL VALOR DE IDENTIFICADOR ": tabla.agregar_etiqueta(Simbolo('', "I", "I", lex[0].line + 1, 0))
        else: flag = False
    elif info[0] == "SI":
        split1 = op.split("PARIZQ ")
        split2 = split1[1].split("PARDER ")
        inicio = split1[0] + "PARIZQ "
        medio = split2[0]
        fin = "PARDER " + split2[1]

        if not inicio == "SI PARIZQ ":
            print("Error Si P")
            flag = False
        elif not expresion_booleana(medio):
            print("Error Si M")
            flag = False
        elif not fin == "PARDER HACER ":
            print("Error Si M")
            flag = False

        if flag: tabla.agregar_etiqueta(Simbolo('', 'I', 'I', lex[0].line, 0))
    elif op == "SINO ": tabla.agregar_etiqueta(Simbolo('', 'I', 'I', lex[0].line, 0))
    elif info[0] in ["SEA", "OTRO"]:
        temp_info = op.split("DOSPUNTOS ")
        temp_op = str(temp_info[1])
        temp_lex = lex[len(temp_info[0].split(" ")):]
        asignar_bloque(temp_op, temp_lex)

    return flag

def find_op(op, lex_op, operation):    
    for pos in range(len(op)):
        temp_op = op[pos]
        temp_lex = lex_op[pos]
        #print(temp_op)

        if operation == "CONSTANTE": 
            if not asignar_constantes(temp_op, temp_lex): print("Error C")
        elif operation == "VARIABLE": 
            if not asignar_variables(temp_op, temp_lex): print("Error V")
        elif operation == "FUNC": 
            if not asignar_func(temp_op, temp_lex): print("Error O")
        elif operation == "PROC": 
            if not asignar_proc(temp_op, temp_lex): print("Error P")
        elif operation == "BLOQUE":
            print(temp_op)
            if not asignar_bloque(temp_op, temp_lex): print("Error B")

def sintactic_analyzer(lexemas):
    global tabla

    lines = dict()
    for lexema in lexemas:
        if lexema.line not in lines.keys():
            lines[lexema.line] = []
        
        lines[lexema.line].append(lexema)

    past_op = ""
    current_op = ""

    op = []
    lex_op = []

    pila = []
    for key in lines.keys():
        temp_op = ''
        temp_lex = []
        if key in range(1, 44):
            for lex in lines[key]:
                if lex.tipo == "TAB" or lex.tipo == "COMENTARIO": continue

                if lex.tipo in BLOQUES.keys():
                    current_op = BLOQUES[lex.tipo]
                    if current_op == "BLOQUE": pila.append("INICIO")
                    elif current_op == "BLOQUE2":
                        pila.pop()
                        if pila: current_op = "BLOQUE"
                    
                if not past_op == current_op:
                    if current_op not in ["BLOQUE", "BLOQUE2"]:
                        if past_op == "BLOQUE2":
                            temp_op += f"{lex.tipo} "
                            temp_lex.append(lex)
                        else:
                            find_op(op, lex_op, past_op)
                            op = []
                            lex_op = []
                    elif current_op == "BLOQUE":
                        if len(op) > 1:
                            find_op(op[:-1], lex_op[:-1], past_op)
                        op = [op[-1]]
                        lex_op = [lex_op[-1]]
                    elif current_op == "BLOQUE2":
                        find_op(op, lex_op, past_op)
                        op = []
                        lex_op = []
                        past_op = current_op
                        break    
                    past_op = current_op
                else:
                    temp_op += f"{lex.tipo} "
                    temp_lex.append(lex)
        if temp_op: op.append(temp_op)
        if temp_lex: lex_op.append(temp_lex)

    tabla.print()