
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ASIGNAR BINARIO_ESP CADENA CADENA_ABB CIN COMA COMDOB CORDER CORIZQ COUT DISTINTO DIV ENDL ENTERO GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO STD SUMA USING VOIDdeclaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion\n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    expresion : ENTEROexpresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR'
    
_lr_action_items = {'IDENTIFICADOR':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,65,66,67,68,69,70,],[2,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'RESTA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[4,-33,12,4,4,4,4,-31,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-9,-33,12,12,12,12,12,-3,-4,-5,-6,12,12,12,12,12,12,12,12,12,12,12,-10,4,4,4,-11,-12,-32,12,12,12,4,4,4,4,4,4,-28,-29,-30,12,12,12,12,12,12,-19,-20,-21,-22,-23,-24,]),'PARIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,56,57,58,59,60,61,65,66,67,68,69,70,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,65,66,67,68,69,70,5,5,5,5,5,5,]),'LLAIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,65,66,67,68,69,70,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'CORIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,65,66,67,68,69,70,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'ENTERO':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,65,66,67,68,69,70,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'COMDOB':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,65,66,67,68,69,70,71,72,73,80,81,82,83,84,85,],[9,9,9,9,9,-31,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-9,-33,54,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,9,9,9,-11,-12,-32,9,9,9,9,9,9,-28,-29,-30,-19,-20,-21,-22,-23,-24,]),'$end':([1,2,3,8,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,71,72,73,80,81,82,83,84,85,],[0,-33,-2,-31,-9,-33,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,-11,-12,-32,-1,-28,-29,-30,-19,-20,-21,-22,-23,-24,]),'ASIGNAR':([2,],[10,]),'SUMA':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,11,-31,-9,-33,11,11,11,11,11,-3,-4,-5,-6,11,11,11,11,11,11,11,11,11,11,11,-10,-11,-12,-32,11,11,11,-28,-29,-30,11,11,11,11,11,11,-19,-20,-21,-22,-23,-24,]),'MULT':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,13,-31,-9,-33,13,13,13,13,13,13,13,-5,-6,13,13,13,13,13,13,13,13,13,13,13,-10,-11,-12,-32,13,13,13,-28,-29,-30,13,13,13,13,13,13,-19,-20,-21,-22,-23,-24,]),'DIV':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,14,-31,-9,-33,14,14,14,14,14,14,14,-5,-6,14,14,14,14,14,14,14,14,14,14,14,-10,-11,-12,-32,14,14,14,-28,-29,-30,14,14,14,14,14,14,-19,-20,-21,-22,-23,-24,]),'POTENCIA':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,15,-31,-9,-33,15,15,15,15,15,-3,-4,-5,-6,15,15,15,15,15,15,15,15,15,15,15,-10,-11,-12,-32,15,15,15,-28,-29,-30,15,15,15,15,15,15,-19,-20,-21,-22,-23,-24,]),'MODULO':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,16,-31,-9,-33,16,16,16,16,16,-3,-4,-5,-6,16,16,16,16,16,16,16,16,16,16,16,-10,-11,-12,-32,16,16,16,-28,-29,-30,16,16,16,16,16,16,-19,-20,-21,-22,-23,-24,]),'MENORQUE':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,17,-31,-9,-33,17,17,17,17,17,-3,-4,-5,-6,17,17,17,17,17,17,17,17,17,17,17,56,-11,-12,-32,17,17,17,-28,-29,-30,17,17,17,17,17,17,-19,-20,-21,-22,-23,-24,]),'MAYORQUE':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,18,-31,-9,-33,18,18,18,18,18,-3,-4,-5,-6,18,18,18,18,18,18,18,18,18,18,18,57,-11,-12,-32,18,18,18,-28,-29,-30,18,18,18,18,18,18,-19,-20,-21,-22,-23,-24,]),'MENORIGUAL':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,19,-31,-9,-33,19,19,19,19,19,-3,-4,-5,-6,19,19,19,19,19,19,19,19,19,19,19,58,-11,-12,-32,19,19,19,-28,-29,-30,19,19,19,19,19,19,-19,-20,-21,-22,-23,-24,]),'MAYORIGUAL':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,20,-31,-9,-33,20,20,20,20,20,-3,-4,-5,-6,20,20,20,20,20,20,20,20,20,20,20,59,-11,-12,-32,20,20,20,-28,-29,-30,20,20,20,20,20,20,-19,-20,-21,-22,-23,-24,]),'IGUAL':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,21,-31,-9,-33,21,21,21,21,21,-3,-4,-5,-6,21,21,21,21,21,21,21,21,21,21,21,60,-11,-12,-32,21,21,21,-28,-29,-30,21,21,21,21,21,21,-19,-20,-21,-22,-23,-24,]),'DISTINTO':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,22,-31,-9,-33,22,22,22,22,22,-3,-4,-5,-6,22,22,22,22,22,22,22,22,22,22,22,61,-11,-12,-32,22,22,22,-28,-29,-30,22,22,22,22,22,22,-19,-20,-21,-22,-23,-24,]),'AND':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,23,-31,-9,-33,49,23,23,23,23,-3,-4,-5,-6,23,23,23,23,23,23,23,23,23,23,23,-10,-11,-12,-32,23,23,23,-28,-29,-30,23,23,23,23,23,23,-19,-20,-21,-22,-23,-24,]),'OR':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,24,-31,-9,-33,50,24,24,24,24,-3,-4,-5,-6,24,24,24,24,24,24,24,24,24,24,24,-10,-11,-12,-32,24,24,24,-28,-29,-30,24,24,24,24,24,24,-19,-20,-21,-22,-23,-24,]),'NOT':([2,3,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-33,25,-31,-9,-33,51,25,25,25,25,-3,-4,-5,-6,25,25,25,25,25,25,25,25,25,25,25,-10,-11,-12,-32,25,25,25,-28,-29,-30,25,25,25,25,25,25,-19,-20,-21,-22,-23,-24,]),'PARDER':([8,26,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,62,63,64,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,-9,-33,48,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,-11,-12,-32,71,72,73,-28,-29,-30,80,81,82,83,84,85,-19,-20,-21,-22,-23,-24,]),'LLADER':([8,26,27,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,71,72,73,80,81,82,83,84,85,],[-31,-9,-33,52,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,-11,-12,-32,-28,-29,-30,-19,-20,-21,-22,-23,-24,]),'CORDER':([8,26,27,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,71,72,73,80,81,82,83,84,85,],[-31,-9,-33,53,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,-11,-12,-32,-28,-29,-30,-19,-20,-21,-22,-23,-24,]),'PUNTOCOMA':([8,26,27,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,71,72,73,80,81,82,83,84,85,],[-31,-9,-33,55,-3,-4,-5,-6,-7,-8,-13,-14,-15,-16,-17,-18,-25,-26,-27,-10,-11,-12,-32,-28,-29,-30,-19,-20,-21,-22,-23,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,49,50,51,65,66,67,68,69,70,],[3,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,62,63,64,74,75,76,77,78,79,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','analizador_sintactico.py',17),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',21),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',27),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',28),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',29),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',30),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',31),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',32),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizador_sintactico.py',53),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',58),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',59),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',60),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',66),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',67),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',68),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',69),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',70),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',71),
  ('expresion -> PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',72),
  ('expresion -> PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',73),
  ('expresion -> PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',74),
  ('expresion -> PARIZQ expresion PARDER MAYORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',75),
  ('expresion -> PARIZQ expresion PARDER IGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',76),
  ('expresion -> PARIZQ expresion PARDER DISTINTO PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',77),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',103),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',104),
  ('expresion -> expresion NOT expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',105),
  ('expresion -> PARIZQ expresion AND expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',106),
  ('expresion -> PARIZQ expresion OR expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',107),
  ('expresion -> PARIZQ expresion NOT expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',108),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizador_sintactico.py',124),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','analizador_sintactico.py',128),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizador_sintactico.py',132),
]
