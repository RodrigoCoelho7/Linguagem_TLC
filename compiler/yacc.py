import ply.yacc as yacc
from Lex import tokens


def p_prg(p):
    "prg : declarations statements"

#-------------- Declarations ------------------------------

def p_declarations_1(p):
    "declarations : decl"

def p_declarations_mult(p):
    "declarations : declarations decl"

def p_decl_V(p):
    "decl : declV"

def p_decl_F(p):
    "decl : declF"

def p_decl_L(p):
    "decl : declL"

#---------------------------------------------------------------

#----------------- Variable declarations ----------------------------

def p_declV(p):
<<<<<<< HEAD
    "declV : VAR ids ':' tipo ENTER"
=======
    "declV : VAR ids ':' tipo ENTER "
>>>>>>> a15534ef276b07a991a6b22be92dcb6666c86f86

def p_ids_1(p):
    "ids : ID"

def p_ids_mult(p):
    "ids : ids ',' ID"

def p_tipo_int(p):
    "tipo : ENTERO"

def p_tipo_REAL(p):
    "tipo : REAL"

def p_tipo_BOOL(p):
    "tipo : BOOLEANO"

#------------------------------------------------------

#-----------------List Declarations --------------------------

def p_declL(p):
    "declL : LISTA ID '=' lista ENTER"

def p_lista_vazia(p):
    "lista : '[' ']'"

def p_lista_elem(p):
    "lista : '[' elementos ']'"

def p_elementos_1(p):
    "elementos : elemento"

def p_elementos_mult(p):
    "elementos : elementos ',' elemento"

def p_elemento_INT(p):
    "elemento : INT"

def p_elemento_FLOAT(p):
    "elemento : FLOAT"

def p_elemento_BOOL(p):
    "elemento : BOOLEANO"

def p_elemento_STRING(p):
    "elemento : STRING"

def p_elemento_ID(p):
    "elemento : ID"

def p_elemento_lista(p):
    "elemento : lista"

#-------------------------------------------------------

#-------------------Function declarations ------------------

def p_declF_parametros(p):
    "declF : FUNCION ID '(' parametros ')' ':' ENTERO ENTER declarationsF statementsI DEVUELVE return"

def p_declF_vazia(p):
    "declF : FUNCION ID '(' ')' ':' ENTERO ENTER declarationsF statementsI DEVUELVE return"

def p_parametros_1(p):
    "parametros : ID ':' tipo"

def p_parametros_mult(p):
    "parametros : parametros ',' ID ':' tipo"

def p_declarationsF_1(p):
    "declarationsF : TAB decl"

def p_declarationsF_mult(p):
    "declarationsF : declarationsF TAB decl"

def p_return_INT(p):
    "return : INT ENTER"

def p_return_ID(p):
    "return : ID ENTER"

#----------------------------------------------------------------------------

#----------------------STATEMENTS-------------------------------------------

def p_statementsI_1(p):
    "statementsI : TAB stat"

def p_statementsI_mult(p):
    "statementsI : statementsI TAB stat"

def p_statements_1(p):
    "statements : stat"

def p_statements_mult(p):
    "statements : statements stat"

def p_stat_atrib(p):
    "stat : atrib ENTER"

def p_stat_conditions(p):
    "stat : conditions"

def p_stat_ciclos(p):
    "stat : ciclos"

#-----------------ATRIBUIÇÕES-------------------------

def p_atrib(p):
    "atrib : ID '=' exp"

def p_exp_soma(p):
    "exp : exp '+' termo"

def p_exp_sub(p):
    "exp : exp '-' termo"

def p_exp_termo(p):
    "exp : termo"

def p_termo_mul(p):
    "termo : termo '*' fator"

def p_termo_div(p):
    "termo : termo '/' fator"

def p_termo_pot(p):
    "termo : termo '^' fator"

def p_termo_fator(p):
    "termo : fator"

def p_fator_INT(p):
    "fator : INT"

def p_fator_FLOAT(p):
    "fator : FLOAT"

def p_fator_ID(p):
    "fator : ID"

def p_fator_exp(p):
    "fator : '(' exp ')'"

#------------------------------------------------------

#----------------Conditions----------------------------

def p_conditions_si(p):
    "conditions : SI expL ENTONCES ENTER statementsI"

def p_conditions_si_no(p):
    "conditions : SI expL ENTONCES ENTER statementsI SI NO ENTER statementsI"

def p_expL_1(p):
    "expL : termoB"

def p_expL_mult(p):
    "expL : expL 'O' termoB"

def p_termoB_1(p):
    "termoB : fatorB"

def p_termoB_mult(p):
    "termoB : termoB 'y' fatorB"

def p_fatorB_condition(p):
    "fatorB : condition"

def p_fatorB_BOOL(p):
    "fatorB : BOOLEANO"

def p_fatorB_expL(p):
    "fatorB : '(' expL ')'"

def p_condition(p):
    "condition : exp op exp"

def p_op_maior(p):
    "op : '>'"

def p_op_menor(p):
    "op : '<'"

def p_op_IGUAL(p):
    "op : IGUAL"

def p_op_DIFERENTE(p):
    "op : DIFERENTE"

def p_op_maiorIGUAL(p):
    "op : '>' IGUAL"

def p_op_menorIGUAL(p):
    "op : '<' IGUAL"

#---------------------------------------

#------------Ciclos---------------------

def p_ciclos_while(p):
    " ciclos : ENCUANTO expL HACER ENTER statementsI"

def p_ciclos_for_1(p):
    "ciclos : PARA expL SIGUIENTE atrib '.' ENTER"

def p_ciclos_for_mult(p):
    "ciclos : PARA expL SIGUIENTE atrib HACER ENTER statementsI"

def p_error(p):
<<<<<<< HEAD
    print("Syntax error!",p)
=======
    print("Syntax error!")
>>>>>>> a15534ef276b07a991a6b22be92dcb6666c86f86
    parser.success = False

parser = yacc.yacc()
parser.success = True


file = open("Exemplos.txt","r")
content = file.read()

parser.parse(content)
if parser.success == True:
    print("Parsing completed")

