from pprint import pprint
import os
import re
#TODO agregar reglas para las funciones de (si,cuando,imprime,lee,sea,otro,hasta que,regresa,desde)
#TODO remover comentarios por que no se poner el caso de ignorar en regex 
#!^(?i)constantes .+:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n(.*:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n)*\n*^(?i)variables (.+,|.+\[.+\],).+:.+;\n((.+,|.+\[.+\],).+:.+;\n)*(((?i)funcion .+\(.+:.+\):.+;\n)*\n*((?i)procedimiento .+\(.+:.+\);\n)*)*\n*(((?i)procedimiento .+\((.*(,.*)*:.+)*\)(:.+)*)\n^(?i)inicio\n(.*\n)*(?i)fin de procedimiento;\n*)*(((?i)funcion .+\((.*(,.*)*:.+)*\)(:.+)*)\n^(?i)inicio\n(.*\n)*(?i)fin de funcion;\n*)*(?i)programa\n(.*\n)*(?i)fin de programa.$ Complete rule
RULES = ["^(?i)constantes .+:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n(.*:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n)*\n*^(?i)variables (.+,|.+\[.+\],).+:.+;\n((.+,|.+\[.+\],).+:.+;\n)*(((?i)funcion .+\(.+:.+\):.+;\n)*((?i)procedimiento .+\(.+:.+\);\n)*)*"]
RESERVED = {
    "constantes": 1,
    "variables": 1,
    "real": 1,
    "alfabetico": 1,
    "logico": 1,
    "entero": 1,
    "funcion": 1,
    "inicio": 1,
    "fin": 1,
    "de": 1,
    "procedimiento": 1,
    "regresa": 1,
    "si": 1,
    "hacer": 1,
    "sino": 1,
    "cuando": 1,
    "el": 1,
    "valor": 1,
    "sea": 1,
    "otro": 1,
    "desde": 1,
    "hasta": 1,
    "incr": 1,
    "decr": 1,
    "repetir": 1,
    "que": 1,
    "mientras": 1,
    "se": 1,
    "cumpla": 1,
    "continua": 1,
    "interrumpe": 1,
    "limpia": 1,
    "lee": 1,
    "imprime": 1,
    "imprimenl": 1,
    "verdadero": 1,
    "falso": 1,
}
LOGIC = {"==": 1, "!=": 1, ">": 1, "<": 1, ">=": 1, "<=": 1, "&&": 1, "||": 1, "!": 1}
OPERATOR = {
    ":=": 1,
    "+": 1,
    "-": 1,
    "/": 1,
    "*": 1,
    "%": 1,
    "+=": 1,
    "-=": 1,
    "/=": 1,
    "*=": 1,
    "++": 1,
    "--": 1,
}
BLOCK = {"(": 1, ")": 1, "{": 1, "}": 1, "[": 1, "]": 1}
LITERAL = {'"': 1, "'": 1}
SEPARATORS = {";": 1, ",": 1, ":": 1}

variable_table = {
    "identifier": [],
    "reserved": [],
    "logic": [],
    "operator": [],
    "block": [],
    "literal": [],
    "separator": [],
    "number": [],
}
variable_types={"Alfabetico":"idk","Logico":"idk","Entero":"idk","Real":"idk"}


def get_word(symbol, line, position):
    """Searches for the end of a literal.

    Args:
        symbol (str): The literal symbol that started the str.
        line (str): The line in which the symbol was found.
        position (int): The starting position of the literal symbol.

    Returns:
        str: The word found.
        int: The position after the word found.
    """

    word = ""
    count = 0
    for pos, char in enumerate(line[position:]):
        word += char
        if char == symbol:
            count += 1
        if count == 2:
            return word, position + pos + 1
    return word, len(line)


def get_number(line, position):
    """Searches for the end of a number.

    Args:
        line (str): The line in which the number was found.
        position (int): The starting position of the number.

    Returns:
        str: The number found.
        int: The position after the number found.
    """

    word = ""
    for pos, char in enumerate(line[position:]):
        if char.isdigit() or char == ".":
            word += char
        else:
            return word, position + pos
    return word, len(line)


def is_from(category, symbol):
    """Checks if the symbol is from the category given.

    Args:
        category (dict): The dictionary of the category to check.
        symbol (str): The symbol or word given to analyze.

    Returns:
        bool: Whether the symbol is part of the category given.
    """

    try:
        category[symbol]
        return True
    except:
        return False


def categorize(symbol):
    """Checks the category of a word or symbol.

    Args:
        symbol (str): The symbol to be categorized.

    Returns:
        str: The key to a dictionary with all the categories.
    """

    try:
        float(symbol)
        category = "number"
    except:
        category = "identifier"

    if is_from(RESERVED, symbol):
        category = "reserved"
    elif is_from(LOGIC, symbol):
        category = "logic"
    elif is_from(OPERATOR, symbol):
        category = "operator"
    elif is_from(BLOCK, symbol):
        category = "block"
    elif is_from(LITERAL, symbol[0]):
        category = "literal"
    elif is_from(SEPARATORS, symbol):
        category = "separator"

    return category


def read_next(line, position):
    """Reads the next word from the line.

    Args:
        line (str): A line of the code given.
        position (int): The starting position of the next word.

    Returns:
        str: The word, its separated depending on the possible categories.
        int: The starting position of the next word to read.
    """

    word = ""
    total_pos = position
    for pos, char in enumerate(line[position:]):
        global_pos = position + pos
        total_pos = global_pos
        if char == " ":
            for temp_pos, temp_char in enumerate(line[global_pos:]):
                if not temp_char == " ":
                    total_pos += temp_pos
                    break
            break
        elif char == "\n" or (char == "/" and line[global_pos + 1] == "/"):
            total_pos = len(line)
            break
        elif char == "\t":
            total_pos = len(line)
            break
        else:
            if is_from(SEPARATORS, char) or is_from(BLOCK, char):
                if word == "":
                    word = char
                    total_pos += 1
                break
            elif is_from(LITERAL, char):
                if word == "":
                    word, total_pos = get_word(char, line, global_pos)
                break
            elif is_from(OPERATOR, char):
                if word == "":
                    word = char
                    total_pos += 1
                    temp_word = char + line[global_pos + 1]
                    if is_from(OPERATOR, temp_word) or is_from(LOGIC, temp_word):
                        word = temp_word
                        total_pos += 2
                break
            elif is_from(LOGIC, char):
                if word == "":
                    word = char
                    total_pos += 1
                    temp_word = char + line[global_pos + 1]
                    if is_from(LOGIC, temp_word):
                        word = temp_word
                        total_pos += 2
                break
            elif char.isdigit():
                if word == "":
                    word, total_pos = get_number(line, global_pos)
                    break
                elif not categorize(word) == "identifier":
                    break
        word += char
    return word, total_pos


def rule_validation(line, pos):
    #! ^constantes .+:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n(.*:=[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?;\n)*\n* regex para bloque constantes
    #! ^variables (.+,|.+\[.+\],).+:.+;\n((.+,|.+\[.+\],).+:.+;\n)* ^variables (.+,|.+\[.+\],).+:.+;\n((.+,|.+\[.+\],).+:.+;\n)* regex para bloque variables (despues de ":" va tipo de variable)
    #! (((?i)funcion .+\(.+:.+\):.+;\n)*((?i)procedimiento .+\(.+:.+\);\n)*)* regex para bloque de protFuncionProc (despues de ":" va tipo de variable)
    for rule in RULES:
        line_check = re.search(rule, line)
        if line_check:
            return True
        else:
            return False


def write_files(table):
    """writes files with the corresponding tables.

    Args:
        table (dict): Table containing all variables and identifiers.

    Returns:
        None
    """
    if not os.path.exists("./classifiers"):
        os.makedirs("./classifiers")
    for key in table.keys():
        with open(f"classifiers/{key}", "w") as f:
            for element in table[key]:
                f.write(f"{element}\n")


code = open("examen.up", "r").read().split("\n")
code = [line + "\n" for line in code]
for line in code:
    pos = 0
    if rule_validation(line, pos):
        print("thx")
        pass
    while not pos == len(line):
        word, pos = read_next(line, pos)
        if word == "constantes":
        if not word == "":
            variable_table[categorize(word)].append(word)

# for key in variable_table.keys():
#    print(key.capitalize())
#    pprint(variable_table[key])
# write_files(variable_table)
