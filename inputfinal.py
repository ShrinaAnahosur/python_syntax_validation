import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'input': 'INPUT',  
}


tokens = [
    'LPAREN',
    'RPAREN',
    'ID',
    'QUOTES',
    'NUMBER',
    'COLON',
    'SPACE',
    'SPECIAL_CHAR',
    'NEWLINE',
    'TAB',
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTES = r'\"'
t_COLON = r':'
t_SPACE = r'\s+'
t_SPECIAL_CHAR = r'[@$%&!.?]'
t_NEWLINE = r'\\n'
t_TAB = r'\\t'


def t_NUMBER(t) :
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t



def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

def p_input_statement(p):
    '''input_statement : INPUT LPAREN QUOTES message QUOTES RPAREN
                | INPUT LPAREN RPAREN''' 
    print("Found 'input' statement")

def p_message(p):
    'message : msg_content'
    p[0] = p[1]

def p_msg_content(p):
    '''msg_content : ID
                       | NUMBER
                       | COLON
                       | SPACE
                       | SPECIAL_CHAR
                       | NEWLINE
                       | TAB
                       | ID msg_content
                       | NUMBER msg_content
                       | COLON msg_content
                       | SPACE msg_content
                       | SPECIAL_CHAR msg_content
                       | NEWLINE msg_content
                       | TAB msg_content'''


def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print(f"Syntax error: Unexpected EOF")

parser = yacc.yacc()

def parse_input(input_str):
    return parser.parse(input_str) 


while True:
    try:
        s=input(">>")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)


