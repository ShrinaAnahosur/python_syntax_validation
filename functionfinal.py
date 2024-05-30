import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'def': 'FUNCTION',
}

tokens = [
    'COLON',
    'ID',
    'NEWLINE',
    'TAB',
    'LPAREN',
    'RPAREN',
    'QUOTES',
    'NUMBER',
    'SPACE',
    'SPECIAL_CHAR',
    'COMMA',
    'EQUAL',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
] + list(reserved.values())


t_COLON = r':'
t_TAB = r'\t+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTES = r'\"'
t_SPACE = r'\s+'
t_SPECIAL_CHAR = r'[@$%&!.?=]'
t_COMMA = r','
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'




def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t) :
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


def p_function_declaration(p):
    '''function_declaration : FUNCTION SPACE ID LPAREN RPAREN COLON NEWLINE TAB messages
                            | FUNCTION SPACE ID LPAREN parameters RPAREN COLON NEWLINE TAB messages'''
    print("Found function")

def p_messages(p):
    '''messages : message 
                | message NEWLINE TAB messages'''

def p_message(p):
    '''message : ID
                       | NUMBER
                       | SPACE
                       | SPECIAL_CHAR
                       | LPAREN
                       | RPAREN
                       | QUOTES
                       | EQUAL
                       | PLUS
                       | MINUS
                       | MULT
                       | DIV
                       | ID message
                       | NUMBER message
                       | SPACE message
                       | SPECIAL_CHAR message
                       | LPAREN message
                       | RPAREN message
                       | QUOTES message
                       | EQUAL message
                       | PLUS message
                       | MINUS message
                       | MULT message
                       | DIV message'''
    
def p_parameters(p):
    '''parameters : parameter
                | parameter COMMA parameters'''

def p_parameter(p):
    '''parameter : ID
                | ID parameter'''
 


def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print(f"Syntax error: Unexpected EOF")


parser = yacc.yacc()


while True:
    try:
        s = input(">> ")
    except EOFError:
        break
    if not s:
        continue

    input_lines = [s]   
    while True:
        try:
            s = input("   ")
        except EOFError:
            break
        if not s or s.strip() == 'END':  
            break
        input_lines.append(s)

    input_str = '\n'.join(input_lines)
    parser.parse(input_str)

