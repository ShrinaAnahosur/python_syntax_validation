import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'list': 'LIST',
    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE',
}

tokens = [
    'NUMBER',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'IDENTIFIER',
    'DQUOTE',
    'LPAREN',
    'RPAREN',
    'DOT',
] + list(reserved.values())


t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DQUOTE = r'\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

def p_list(p):
    '''list : LBRACKET elements RBRACKET 
            | LIST LPAREN LPAREN elements RPAREN RPAREN
            | LIST LPAREN RPAREN''' 
    print("Valid syntax")
  

def p_empty(p):
    'empty :'
    pass  

def p_elements_single(p):
    'elements : element'


def p_elements_multiple(p):
    'elements : element COMMA elements'


def p_element(p):
    '''element : NUMBER
               | DQUOTE IDENTIFIER DQUOTE
               | empty
               | TRUE
               | FALSE
               | NUMBER DOT NUMBER
               | DOT NUMBER
               | NONE
               | list'''




def p_error(p):
    print(f"Syntax error")


parser = yacc.yacc()

def parse_input(input_str):
    try:
        result = parser.parse(input_str)
        if result is not None:
            print("Valid syntax")
    except Exception as e:
        p_error(input_str)


while True:
    try:
        s = input(">> ")
    except EOFError:
        break
    if not s:
        continue
    parse_input(s)