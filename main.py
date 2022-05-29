from analizador_lexico import lexical_analizer
from analizador_sintactico import sintactic_analyzer
from pprint import pprint

lexemas = lexical_analizer("examen")
sintactic_analyzer(lexemas)