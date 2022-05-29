from lexema import Simbolo, Tabla_Simbolos


BLOQUES = {"TIPO_CONSTANTES":"CONSTANTE", "TIPO_VARIABLES":"VARIABLE", "FUNCION": "FUNC", "PROCEDIMIENTO":"PROC", "INICIO": "BLOQUE"}
TIPOS = {"TIPO_ENTERO":"ENTERO", "TIPO_REAL":"REAL", "TIPO_ALFABETICO":"ALFABETICO", "TIPO_LOGICO":"LOGICO"}

tabla = Tabla_Simbolos()

def variable_ident(texto, temp_lex, pos, tipo, guardar=True, funcion='', local=''):
    global tabla

    flag = True
    if "CORIZQ" in texto:
        if texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER CORIZQ IDENTIFICADOR CORDER ":
            if guardar: 
                dim1 = tabla.buscar(temp_lex[pos + 2].value)
                dim2 = tabla.buscar(temp_lex[pos + 5].value)
                if dim1 == "Fail" or dim2 == "Fail": flag = False
                else:
                    if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, dim1, dim2, 0), funcion)
                    else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, dim1, dim2, 0))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER CORIZQ ENTERO CORDER ": 
            if guardar: 
                if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, 0), funcion)
                else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, temp_lex[pos + 2].value, temp_lex[pos + 5].value, 0))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER CORIZQ IDENTIFICADOR CORDER ": 
            if guardar:
                dim2 = tabla.buscar(temp_lex[pos + 5].value)
                if dim2 == "Fail": flag = False
                else:
                    if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, temp_lex[pos + 2], dim2, 0), funcion)
                    else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, temp_lex[pos + 2], dim2, 0))
        elif texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER CORIZQ ENTERO CORDER ": 
            if guardar:
                dim1 = tabla.buscar(temp_lex[pos + 2].value)
                if dim1 == "Fail": flag = False
                else:
                    if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, dim1, temp_lex[pos + 5], 0), funcion)
                    else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, dim1, temp_lex[pos + 5], 0))
        elif texto == "IDENTIFICADOR CORIZQ IDENTIFICADOR CORDER ":
            if guardar:
                dim1 = tabla.buscar(temp_lex[pos + 2].value)
                if dim1 == "Fail": flag = False
                else:
                    if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, dim1, 0, 0), funcion)
                    else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, dim1, 0, 0))
        elif texto == "IDENTIFICADOR CORIZQ ENTERO CORDER ": 
            if guardar: 
                if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, temp_lex[pos + 2], 0, 0), funcion)
                else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, temp_lex[pos + 2], 0, 0))
        else: flag = False
    elif texto == "IDENTIFICADOR ": 
        if guardar: 
            if funcion: tabla.agregar_param(Simbolo(temp_lex[pos + 0].value, "PARAMETRO", tipo, 0, 0, 0), funcion)
            else: tabla.agregar(Simbolo(temp_lex[pos + 0].value, "VARIABLE", tipo, 0, 0, 0))
    else: flag = False

    return flag

def asignar_constantes(op, lex, guardar=True, esLocal=False):
    global tabla

    if op == "IDENTIFICADOR ASIGNACION REAL PUNTOCOMA ": 
        if guardar: tabla.agregar(Simbolo(lex[0].value, "CONSTANTE", "REAL", 0, 0, lex[2].value))
    elif op == "IDENTIFICADOR ASIGNACION ENTERO PUNTOCOMA ": 
        if guardar: tabla.agregar(Simbolo(lex[0].value, "CONSTANTE", "ENTERO", 0, 0, lex[2].value))
    elif op == "IDENTIFICADOR ASIGNACION LOGICO PUNTOCOMA ": 
        if guardar: tabla.agregar(Simbolo(lex[0].value, "CONSTANTE", "LOGICO", 0, 0, lex[2].value))
    elif op == "IDENTIFICADOR ASIGNACION ALFABETICO PUNTOCOMA ":
        if guardar: tabla.agregar(Simbolo(lex[0].value, "CONSTANTE", "ALFABETICO", 0, 0, lex[2].value))
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

def asignar_func(op, lex, guardar=True):
    global tabla

    flag = True
    if op in [f"IDENTIFICADOR PARIZQ PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
        if guardar: tabla.agregar(Simbolo(lex[0], "FUNCION", lex[-2], 0, 0, 0))
    elif op in [f"FUNCION IDENTIFICADOR PARIZQ PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
        if guardar: tabla.agregar(Simbolo(lex[1], "FUNCION", lex[-2], 0, 0, 0))
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

        simbol = Simbolo(nombre, 'FUNCION', lex[-2].value, 0, 0, 0)
        
        if not inicio in ["FUNCION IDENTIFICADOR PARIZQ ", "IDENTIFICADOR PARIZQ "]:
            print("Error P")
            flag = False
        elif not asignar_variables(medio, lex[param_start:], funcion=simbol.nombre):
            print("Error M")
            flag = False
        elif final not in [f"PARDER DOSPUNTOS {key} PUNTOCOMA " for key in TIPOS.keys()]: 
            print("Error F")
            flag = False

        if flag and guardar:
            tabla.agregar(simbol)
    return flag

def asignar_proc(op, lex, guardar=True):
    global tabla

    flag = True
    if op == "IDENTIFICADOR PARIZQ PARDER PUNTOCOMA ":
        if guardar: tabla.agregar(Simbolo(lex[0], "PROCEDIMIENTO", "NONE", 0, 0, 0))
    elif op == "PROCEDIMIENTO IDENTIFICADOR PARIZQ PARDER PUNTOCOMA ":
        if guardar: tabla.agregar(Simbolo(lex[1], "PROCEDIMIENTO", "NONE", 0, 0, 0))
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

        simbol = Simbolo(nombre, 'PROCEDIMIENTO', 'NONE', 0, 0, 0)

        if not inicio in ["PROCEDIMIENTO IDENTIFICADOR PARIZQ ", "IDENTIFICADOR PARIZQ "]:
            print("Error P")
            flag = False
        elif not asignar_variables(medio, lex[param_start:], funcion=simbol.nombre): 
            print("Error M")
            flag = False
        elif final not in [f"PARDER PUNTOCOMA "]: 
            print("Error F")
            flag = False

        if flag and guardar:
            tabla.agregar(simbol)
    return flag


def find_op(op, lex_op, operation):    
    for pos in range(len(op)):
        temp_op = op[pos]
        temp_lex = lex_op[pos]
        #print([temp_op])

        if operation == "CONSTANTE": asignar_constantes(temp_op, temp_lex)
        elif operation == "VARIABLE": asignar_variables(temp_op, temp_lex)
        elif operation == "FUNC": asignar_func(temp_op, temp_lex)
        elif operation == "PROC": asignar_proc(temp_op, temp_lex)            

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
    for key in lines.keys():
        temp_op = ''
        temp_lex = []
        if key in range(1, 20):
            for lex in lines[key]:
                if lex.tipo == "TAB" or lex.tipo == "COMENTARIO": continue

                if lex.tipo in BLOQUES.keys():
                    current_op = BLOQUES[lex.tipo]
                    
                if not past_op == current_op:
                    if not current_op == "BLOQUE":
                        find_op(op, lex_op, past_op)
                        op = []
                        lex_op = []
                    else:
                        find_op(op[:-1], lex_op[:-1], past_op)
                        op = [op[-1]]
                        lex_op = [lex_op[-1]]
                        op = []
                        lex_op = []
                    past_op = current_op
                else:    
                    temp_op += f"{lex.tipo} "
                    temp_lex.append(lex)
        if temp_op: op.append(temp_op)
        if temp_lex: lex_op.append(temp_lex)