
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND BOOLEANO DEVUELVE DIFERENTE ENCUANTO ENTER ENTERO ENTONCES ESCRIBE FALSO FLOAT FUNCION HACER ID IGUAL INT LISTA NADA NO OR PARA REAL RESTO SI SIGUIENTE STRING TAB VAR VERDADEROprg : declarations statementsdeclarations : decldeclarations : declarations decldecl : declVdecl : declFdecl : declLdeclV : VAR ids ':' tipo ENTER ids : IDids : ids ',' IDtipo : ENTEROtipo : REALtipo : BOOLEANOdeclL : LISTA ID '=' lista ENTERlista : '[' ']'lista : '[' elementos ']'elementos : elementoelementos : elementos ',' elementoelemento : INTelemento : FLOATelemento : BOOLEANOelemento : STRINGelemento : IDelemento : listadeclF : FUNCION ID '(' parametros ')' ':' ENTERO ENTER declarationsF statementsI TAB DEVUELVE returndeclF : FUNCION ID '(' ')' ':' ENTERO ENTER declarationsF statementsI TAB DEVUELVE returnparametros : ID ':' tipoparametros : parametros ',' ID ':' tipodeclarationsF : TAB decldeclarationsF : declarationsF TAB declreturn : INT ENTERreturn : ID ENTERstatementsI : TAB statstatementsI : statementsI TAB statstatements : statstatements : statements statstat : atrib ENTERstat : conditionsstat : ciclosatrib : ID '=' expexp : exp '+' termoexp : exp '-' termoexp : termotermo : termo '*' fatortermo : termo '/' fatortermo : termo '^' fatortermo : fatorfator : INTfator : FLOATfator : IDfator : '(' exp ')'conditions : SI expL ENTONCES ENTER statementsIconditions : SI expL ENTONCES ENTER statementsI SI NO ENTER statementsIexpL : termoBexpL : expL OR termoBtermoB : fatorBtermoB : termoB AND fatorBfatorB : conditionfatorB : BOOLEANOfatorB : '(' expL ')'condition : exp op expop : '>'op : '<'op : IGUALop : DIFERENTEop : '>' IGUALop : '<' IGUAL ciclos : ENCUANTO expL HACER ENTER statementsIciclos : PARA expL SIGUIENTE atrib '.' ENTERciclos : PARA expL SIGUIENTE atrib HACER ENTER statementsI"
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,11,90,95,131,135,145,147,148,149,],[7,7,-2,-4,-5,-6,-3,-7,-13,7,7,-25,-24,-31,-30,]),'FUNCION':([0,2,3,4,5,6,11,90,95,131,135,145,147,148,149,],[8,8,-2,-4,-5,-6,-3,-7,-13,8,8,-25,-24,-31,-30,]),'LISTA':([0,2,3,4,5,6,11,90,95,131,135,145,147,148,149,],[9,9,-2,-4,-5,-6,-3,-7,-13,9,9,-25,-24,-31,-30,]),'$end':([1,10,12,14,15,24,25,105,107,118,119,126,127,137,],[0,-1,-34,-37,-38,-35,-36,-51,-67,-32,-68,-33,-69,-52,]),'ID':([2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,24,25,26,32,42,43,46,48,49,52,53,54,55,56,57,58,59,60,61,63,73,83,84,90,93,95,105,106,107,115,117,118,119,126,127,135,137,139,141,142,143,145,147,148,149,],[16,-2,-4,-5,-6,21,22,23,16,-3,-34,-37,-38,38,38,38,-35,-36,38,38,68,69,38,38,38,38,38,38,-61,-62,-63,-64,38,38,38,16,103,-65,-66,-7,112,-13,-51,16,-67,103,16,-32,-68,-33,-69,16,-52,16,16,144,144,-25,-24,-31,-30,]),'SI':([2,3,4,5,6,10,11,12,14,15,24,25,90,95,105,106,107,117,118,119,126,127,135,137,139,141,145,147,148,149,],[17,-2,-4,-5,-6,17,-3,-34,-37,-38,-35,-36,-7,-13,116,17,-67,17,-32,-68,-33,-69,17,-52,17,17,-25,-24,-31,-30,]),'ENCUANTO':([2,3,4,5,6,10,11,12,14,15,24,25,90,95,105,106,107,117,118,119,126,127,135,137,139,141,145,147,148,149,],[18,-2,-4,-5,-6,18,-3,-34,-37,-38,-35,-36,-7,-13,-51,18,-67,18,-32,-68,-33,-69,18,-52,18,18,-25,-24,-31,-30,]),'PARA':([2,3,4,5,6,10,11,12,14,15,24,25,90,95,105,106,107,117,118,119,126,127,135,137,139,141,145,147,148,149,],[19,-2,-4,-5,-6,19,-3,-34,-37,-38,-35,-36,-7,-13,-51,19,-67,19,-32,-68,-33,-69,19,-52,19,19,-25,-24,-31,-30,]),'TAB':([4,5,6,14,15,25,75,88,90,95,105,107,118,119,120,123,126,127,128,130,132,133,134,136,137,138,140,145,147,148,149,],[-4,-5,-6,-37,-38,-36,106,106,-7,-13,117,117,-32,-68,106,131,-33,117,131,135,106,135,139,-28,117,141,-29,-25,-24,-31,-30,]),'ENTER':([13,34,35,36,37,38,45,47,62,64,65,66,67,72,79,81,82,85,86,87,96,108,109,113,114,121,125,144,146,],[25,-42,-46,-47,-48,-49,-39,75,88,90,-10,-11,-12,95,-50,-40,-41,-43,-44,-45,-14,119,120,123,-15,128,132,148,149,]),'=':([16,23,],[26,44,]),'BOOLEANO':([17,18,19,32,41,48,49,73,91,115,122,],[31,31,31,31,67,31,31,101,67,101,67,]),'(':([17,18,19,22,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,83,84,],[32,32,32,43,46,32,46,32,32,46,46,46,-61,-62,-63,-64,46,46,46,-65,-66,]),'INT':([17,18,19,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,73,83,84,115,142,143,],[36,36,36,36,36,36,36,36,36,36,36,-61,-62,-63,-64,36,36,36,99,-65,-66,99,146,146,]),'FLOAT':([17,18,19,26,32,46,48,49,52,53,54,55,56,57,58,59,60,61,73,83,84,115,],[37,37,37,37,37,37,37,37,37,37,37,-61,-62,-63,-64,37,37,37,100,-65,-66,100,]),':':([20,21,68,69,71,92,112,],[41,-8,-9,91,94,111,122,]),',':([20,21,65,66,67,68,70,96,97,98,99,100,101,102,103,104,110,114,124,129,],[42,-8,-10,-11,-12,-9,93,-14,115,-16,-18,-19,-20,-21,-22,-23,-26,-15,-17,-27,]),'ENTONCES':([27,28,29,30,31,34,35,36,37,38,76,77,78,79,80,81,82,85,86,87,],[47,-53,-55,-57,-58,-42,-46,-47,-48,-49,-54,-56,-59,-50,-60,-40,-41,-43,-44,-45,]),'OR':([27,28,29,30,31,34,35,36,37,38,39,40,50,76,77,78,79,80,81,82,85,86,87,],[48,-53,-55,-57,-58,-42,-46,-47,-48,-49,48,48,48,-54,-56,-59,-50,-60,-40,-41,-43,-44,-45,]),'HACER':([28,29,30,31,34,35,36,37,38,39,45,76,77,78,79,80,81,82,85,86,87,89,],[-53,-55,-57,-58,-42,-46,-47,-48,-49,62,-39,-54,-56,-59,-50,-60,-40,-41,-43,-44,-45,109,]),'SIGUIENTE':([28,29,30,31,34,35,36,37,38,40,76,77,78,79,80,81,82,85,86,87,],[-53,-55,-57,-58,-42,-46,-47,-48,-49,63,-54,-56,-59,-50,-60,-40,-41,-43,-44,-45,]),')':([28,29,30,31,34,35,36,37,38,43,50,51,65,66,67,70,74,76,77,78,79,80,81,82,85,86,87,110,129,],[-53,-55,-57,-58,-42,-46,-47,-48,-49,71,78,79,-10,-11,-12,92,79,-54,-56,-59,-50,-60,-40,-41,-43,-44,-45,-26,-27,]),'AND':([28,29,30,31,34,35,36,37,38,76,77,78,79,80,81,82,85,86,87,],[49,-55,-57,-58,-42,-46,-47,-48,-49,49,-56,-59,-50,-60,-40,-41,-43,-44,-45,]),'+':([33,34,35,36,37,38,45,51,74,79,80,81,82,85,86,87,],[53,-42,-46,-47,-48,-49,53,53,53,-50,53,-40,-41,-43,-44,-45,]),'-':([33,34,35,36,37,38,45,51,74,79,80,81,82,85,86,87,],[54,-42,-46,-47,-48,-49,54,54,54,-50,54,-40,-41,-43,-44,-45,]),'>':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[55,-42,-46,-47,-48,-49,55,-50,-40,-41,-43,-44,-45,]),'<':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[56,-42,-46,-47,-48,-49,56,-50,-40,-41,-43,-44,-45,]),'IGUAL':([33,34,35,36,37,38,51,55,56,79,81,82,85,86,87,],[57,-42,-46,-47,-48,-49,57,83,84,-50,-40,-41,-43,-44,-45,]),'DIFERENTE':([33,34,35,36,37,38,51,79,81,82,85,86,87,],[58,-42,-46,-47,-48,-49,58,-50,-40,-41,-43,-44,-45,]),'.':([34,35,36,37,38,45,79,81,82,85,86,87,89,],[-42,-46,-47,-48,-49,-39,-50,-40,-41,-43,-44,-45,108,]),'*':([34,35,36,37,38,79,81,82,85,86,87,],[59,-46,-47,-48,-49,-50,59,59,-43,-44,-45,]),'/':([34,35,36,37,38,79,81,82,85,86,87,],[60,-46,-47,-48,-49,-50,60,60,-43,-44,-45,]),'^':([34,35,36,37,38,79,81,82,85,86,87,],[61,-46,-47,-48,-49,-50,61,61,-43,-44,-45,]),'ENTERO':([41,91,94,111,122,],[65,65,113,121,65,]),'REAL':([41,91,122,],[66,66,66,]),'[':([44,73,115,],[73,73,73,]),']':([73,96,97,98,99,100,101,102,103,104,114,124,],[96,-14,114,-16,-18,-19,-20,-21,-22,-23,-15,-17,]),'STRING':([73,115,],[102,102,]),'NO':([116,],[125,]),'DEVUELVE':([139,141,],[142,143,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prg':([0,],[1,]),'declarations':([0,],[2,]),'decl':([0,2,131,135,],[3,11,136,140,]),'declV':([0,2,131,135,],[4,4,4,4,]),'declF':([0,2,131,135,],[5,5,5,5,]),'declL':([0,2,131,135,],[6,6,6,6,]),'statements':([2,],[10,]),'stat':([2,10,106,117,135,139,141,],[12,24,118,126,118,126,126,]),'atrib':([2,10,63,106,117,135,139,141,],[13,13,89,13,13,13,13,13,]),'conditions':([2,10,106,117,135,139,141,],[14,14,14,14,14,14,14,]),'ciclos':([2,10,106,117,135,139,141,],[15,15,15,15,15,15,15,]),'ids':([7,],[20,]),'expL':([17,18,19,32,],[27,39,40,50,]),'termoB':([17,18,19,32,48,],[28,28,28,28,76,]),'fatorB':([17,18,19,32,48,49,],[29,29,29,29,29,77,]),'condition':([17,18,19,32,48,49,],[30,30,30,30,30,30,]),'exp':([17,18,19,26,32,46,48,49,52,],[33,33,33,45,51,74,33,33,80,]),'termo':([17,18,19,26,32,46,48,49,52,53,54,],[34,34,34,34,34,34,34,34,34,81,82,]),'fator':([17,18,19,26,32,46,48,49,52,53,54,59,60,61,],[35,35,35,35,35,35,35,35,35,35,35,85,86,87,]),'op':([33,51,],[52,52,]),'tipo':([41,91,122,],[64,110,129,]),'parametros':([43,],[70,]),'lista':([44,73,115,],[72,104,104,]),'elementos':([73,],[97,]),'elemento':([73,115,],[98,124,]),'statementsI':([75,88,120,130,132,133,],[105,107,127,134,137,138,]),'declarationsF':([123,128,],[130,133,]),'return':([142,143,],[145,147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prg","S'",1,None,None,None),
  ('prg -> declarations statements','prg',2,'p_prg','yacc.py',7),
  ('declarations -> decl','declarations',1,'p_declarations_1','yacc.py',12),
  ('declarations -> declarations decl','declarations',2,'p_declarations_mult','yacc.py',18),
  ('decl -> declV','decl',1,'p_decl_V','yacc.py',24),
  ('decl -> declF','decl',1,'p_decl_F','yacc.py',27),
  ('decl -> declL','decl',1,'p_decl_L','yacc.py',30),
  ('declV -> VAR ids : tipo ENTER','declV',5,'p_declV','yacc.py',37),
  ('ids -> ID','ids',1,'p_ids_1','yacc.py',42),
  ('ids -> ids , ID','ids',3,'p_ids_mult','yacc.py',46),
  ('tipo -> ENTERO','tipo',1,'p_tipo_int','yacc.py',50),
  ('tipo -> REAL','tipo',1,'p_tipo_REAL','yacc.py',54),
  ('tipo -> BOOLEANO','tipo',1,'p_tipo_BOOL','yacc.py',58),
  ('declL -> LISTA ID = lista ENTER','declL',5,'p_declL','yacc.py',66),
  ('lista -> [ ]','lista',2,'p_lista_vazia','yacc.py',69),
  ('lista -> [ elementos ]','lista',3,'p_lista_elem','yacc.py',72),
  ('elementos -> elemento','elementos',1,'p_elementos_1','yacc.py',75),
  ('elementos -> elementos , elemento','elementos',3,'p_elementos_mult','yacc.py',78),
  ('elemento -> INT','elemento',1,'p_elemento_INT','yacc.py',81),
  ('elemento -> FLOAT','elemento',1,'p_elemento_FLOAT','yacc.py',84),
  ('elemento -> BOOLEANO','elemento',1,'p_elemento_BOOL','yacc.py',87),
  ('elemento -> STRING','elemento',1,'p_elemento_STRING','yacc.py',90),
  ('elemento -> ID','elemento',1,'p_elemento_ID','yacc.py',93),
  ('elemento -> lista','elemento',1,'p_elemento_lista','yacc.py',96),
  ('declF -> FUNCION ID ( parametros ) : ENTERO ENTER declarationsF statementsI TAB DEVUELVE return','declF',13,'p_declF_parametros','yacc.py',103),
  ('declF -> FUNCION ID ( ) : ENTERO ENTER declarationsF statementsI TAB DEVUELVE return','declF',12,'p_declF_vazia','yacc.py',107),
  ('parametros -> ID : tipo','parametros',3,'p_parametros_1','yacc.py',111),
  ('parametros -> parametros , ID : tipo','parametros',5,'p_parametros_mult','yacc.py',115),
  ('declarationsF -> TAB decl','declarationsF',2,'p_declarationsF_1','yacc.py',119),
  ('declarationsF -> declarationsF TAB decl','declarationsF',3,'p_declarationsF_mult','yacc.py',122),
  ('return -> INT ENTER','return',2,'p_return_INT','yacc.py',125),
  ('return -> ID ENTER','return',2,'p_return_ID','yacc.py',128),
  ('statementsI -> TAB stat','statementsI',2,'p_statementsI_1','yacc.py',135),
  ('statementsI -> statementsI TAB stat','statementsI',3,'p_statementsI_mult','yacc.py',138),
  ('statements -> stat','statements',1,'p_statements_1','yacc.py',141),
  ('statements -> statements stat','statements',2,'p_statements_mult','yacc.py',144),
  ('stat -> atrib ENTER','stat',2,'p_stat_atrib','yacc.py',147),
  ('stat -> conditions','stat',1,'p_stat_conditions','yacc.py',150),
  ('stat -> ciclos','stat',1,'p_stat_ciclos','yacc.py',153),
  ('atrib -> ID = exp','atrib',3,'p_atrib','yacc.py',158),
  ('exp -> exp + termo','exp',3,'p_exp_soma','yacc.py',161),
  ('exp -> exp - termo','exp',3,'p_exp_sub','yacc.py',164),
  ('exp -> termo','exp',1,'p_exp_termo','yacc.py',167),
  ('termo -> termo * fator','termo',3,'p_termo_mul','yacc.py',170),
  ('termo -> termo / fator','termo',3,'p_termo_div','yacc.py',173),
  ('termo -> termo ^ fator','termo',3,'p_termo_pot','yacc.py',176),
  ('termo -> fator','termo',1,'p_termo_fator','yacc.py',179),
  ('fator -> INT','fator',1,'p_fator_INT','yacc.py',182),
  ('fator -> FLOAT','fator',1,'p_fator_FLOAT','yacc.py',185),
  ('fator -> ID','fator',1,'p_fator_ID','yacc.py',188),
  ('fator -> ( exp )','fator',3,'p_fator_exp','yacc.py',191),
  ('conditions -> SI expL ENTONCES ENTER statementsI','conditions',5,'p_conditions_si','yacc.py',198),
  ('conditions -> SI expL ENTONCES ENTER statementsI SI NO ENTER statementsI','conditions',9,'p_conditions_si_no','yacc.py',201),
  ('expL -> termoB','expL',1,'p_expL_1','yacc.py',204),
  ('expL -> expL OR termoB','expL',3,'p_expL_mult','yacc.py',207),
  ('termoB -> fatorB','termoB',1,'p_termoB_1','yacc.py',210),
  ('termoB -> termoB AND fatorB','termoB',3,'p_termoB_mult','yacc.py',213),
  ('fatorB -> condition','fatorB',1,'p_fatorB_condition','yacc.py',216),
  ('fatorB -> BOOLEANO','fatorB',1,'p_fatorB_BOOL','yacc.py',219),
  ('fatorB -> ( expL )','fatorB',3,'p_fatorB_expL','yacc.py',222),
  ('condition -> exp op exp','condition',3,'p_condition','yacc.py',225),
  ('op -> >','op',1,'p_op_maior','yacc.py',228),
  ('op -> <','op',1,'p_op_menor','yacc.py',231),
  ('op -> IGUAL','op',1,'p_op_IGUAL','yacc.py',234),
  ('op -> DIFERENTE','op',1,'p_op_DIFERENTE','yacc.py',237),
  ('op -> > IGUAL','op',2,'p_op_maiorIGUAL','yacc.py',240),
  ('op -> < IGUAL','op',2,'p_op_menorIGUAL','yacc.py',243),
  ('ciclos -> ENCUANTO expL HACER ENTER statementsI','ciclos',5,'p_ciclos_while','yacc.py',250),
  ('ciclos -> PARA expL SIGUIENTE atrib . ENTER','ciclos',6,'p_ciclos_for_1','yacc.py',253),
  ('ciclos -> PARA expL SIGUIENTE atrib HACER ENTER statementsI','ciclos',7,'p_ciclos_for_mult','yacc.py',256),
]
