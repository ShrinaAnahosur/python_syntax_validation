import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'try': 'TRY',
    'except': 'EXCEPT',
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
] + list(reserved.values())

t_COLON = r':'
t_TAB = r'\t+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTES = r'\"'
t_SPACE = r'\s+'
t_SPECIAL_CHAR = r'[@$%&!.?=]'




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


def p_try_catch(p):
    '''try_catch : TRY COLON NEWLINE TAB messages 
                | EXCEPT COLON NEWLINE TAB messages ''' 
    print("Valid syntax")


def p_messages(p):
    '''messages : message 
                | message NEWLINE TAB messages
                | message NEWLINE try_catch'''


def p_message(p):
    '''message : ID
            | NUMBER
            | SPACE
            | SPECIAL_CHAR
            | LPAREN
            | RPAREN
            | QUOTES
            | ID message
            | NUMBER message
            | SPACE message
            | SPECIAL_CHAR message
            | LPAREN message
            | RPAREN message
            | QUOTES message'''




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

    # Accumulate lines until an empty line or a termination marker is encountered
    input_lines = [s]
    while True:
        try:
            s = input("   ")
        except EOFError:
            break
        if not s or s.strip() == 'END':
            break
        input_lines.append(s)

    # Join accumulated lines and parse the input
    input_str = '\n'.join(input_lines)

    # Initialize a flag for successful parsing
    parsing_successful = True

    try:
        # Try parsing the input
        parser.parse(input_str)
    except Exception as e:
        # Parsing failed, print an error message
        parsing_successful = False
        print(f"Error during parsing: {e}")


        

    
    
