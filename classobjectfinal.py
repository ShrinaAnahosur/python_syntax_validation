import ply.lex as lex
import ply.yacc as yacc


reserved= {
 'class' : 'CLASS',
}



tokens = [
    'COLON',
    'ID',
    'NEWLINE',
    'TAB',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'SPACE',
    'EQUAL',
    'SPECIAL_CHAR',
    'QUOTES',
] + list(reserved.values())


t_COLON = r':'
t_TAB = r'\t+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SPACE = r'\s+'
t_QUOTES = r'\"'
t_SPECIAL_CHAR = r'[@$%&!.?=]'



def t_EQUAL(t):
    r'='
    return t


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



def p_class_object(p):
    'class_object : CLASS SPACE ID COLON NEWLINE TAB elements'
    print("Valid syntax")

def p_elements(p):
    '''elements : element NEWLINE object
                | element NEWLINE TAB elements '''


def p_element(p):
    '''element : ID
                | NUMBER
                | SPACE
                | SPECIAL_CHA
                | LPAREN
                | RPAREN
                | QUOTES
                | EQUAL
                | ID element
                | NUMBER element
                | SPACE element
                | SPECIAL_CHAR element
                | LPAREN element
                | RPAREN element
                | QUOTES element
                | EQUAL element'''
    
def p_object(p):
    '''object : ID EQUAL ID LPAREN RPAREN
                | ID SPACE EQUAL ID LPAREN RPAREN
                | ID SPACE EQUAL SPACE ID LPAREN RPAREN
                | ID EQUAL SPACE ID LPAREN RPAREN'''



    

def p_error(p):
    print("Syntax error")


parser = yacc.yacc()


while True:
    try:
        s = input(">> ")
    except EOFError:
        break
    if not s:
        continue

    # Accumulate lines until an empty line or a termination marker is encountered
    input_lines = [s]   
    while True:
        try:
            s = input("   ")
        except EOFError:
            break
        if not s or s.strip() == 'END':  # You can use any termination condition
            break
        input_lines.append(s)

    # Join accumulated lines and parse the input
    input_str = '\n'.join(input_lines)
    parser.parse(input_str)
