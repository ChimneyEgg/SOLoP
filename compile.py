import re
import sys

stack = []
procs = {}

def push(x):
    global stack
    stack = [x] + stack
def pop():
    global stack
    stack = stack[1:]

procmake = False
procname = None
procdata = []

conditional = False
shouldCond = True
negated = False

def tokenize(x):
    global stack 

    global procmake
    global procname
    global procdata

    global conditional
    global shouldCond
    global negated

    if not shouldCond:
        shouldCond = True
        return

    # Used to evaluate conditionals (TODO: Find a better solution)
    if conditional:
        conditional = False
        if negated:                   
            if not stack[0] == int(x):
                shouldCond = True
                return
            else:
                shouldCond = False
                return
        else:
            if stack[0] == int(x):
                shouldCond = True
                return
            else:
                shouldCond = False
                return            

    # Used to create procedures and pushes the result into a dictionary
    if procmake:
        if procname == None:
            procname = x
            return
        elif not x == '}':
            procdata = procdata + [x]
            return
        else:
            procs[procname] = procdata
            procmake = False
            procname = None
            procdata = []
            return

    match x:
        # Adds together the last two numbers pushed onto the stack
        case '+':
            stack[1] = stack[1] + stack[0]
            pop()
            return
        # Subtracts the last two numbers pushed onto the stack
        case '-':
            stack[1] = stack[1] - stack[0]
            pop()
            return
        # Mutliplies the last two numbers pushed onto the stack
        case '*':
            stack[1] = stack[1] * stack[0]
            pop()
            return
        # Divides the last two numbers pushed onto the stack
        case '/':
            stack[1] = stack[1] / stack[0]
            pop()
            return
        # Prints out the last number pushed onto the stack
        case '!':
            print(int(stack[0]))
            return
        # Prints out the ACII value of the last number pushed onto the stack
        case '.':
            print(chr(int(stack[0])), end='')
            return
        # Prints out the entire stack
        case '=':
            for i in (stack):
                print(i, end=' ')
            print(f'\nLength: {len(stack)}')
            return
        # Accepts input, tokenizing it
        case '?':
            tokenize(input())
            return
        # Pops the last number pushed onto the stack
        case '~':
            pop()
            return
        # Duplicates the last number pushed onto the stack
        case ':':
            push(stack[0])
            return
        # Swaps the last number with the second to last number pushed onto the stack
        case ';':
            s0 = stack[0]
            s1 = stack[1]

            stack[0] = s1
            stack[1] = s0
            return
        # Used to create procedures
        case '@':
            procmake = True
            return
        # Used to check if the last number pushed onto the stack is the same as the condition
        case '&':
            conditional = True
            negated = False
            return
        # Used to check if the last number pushed onto the stack is not the same as the condition    
        case '#':
            conditional = True
            negated = True
            return
        # Rolls the stack once, down
        case '>':
            stack = [stack[-1]] + stack[0:-1]
            return
        # Rolls the stack once, up
        case '<':
            stack = stack[1:] + [stack[0]]
            return
        case other:
            # Checks if the string is in procedures, executing it if it is
            if x in procs:
                for i in procs[x]:
                    tokenize(i)
                return
            push(int(x))
            return

inpu = list(filter(lambda x: x != '', re.split(r'[{|%|\s|\n]', re.sub(r'[@|+|-|*|/|?|!|$|#|=|:|;|{|}|&|.|~]', lambda y: ' ' + y[0] + ' ', ' '.join(re.split(r'([%]).*\1(?![^\s])', open(sys.argv[1]).read())))))) # Scary regex shit

# print(inpu, end='\n\n')

for i in inpu:
    tokenize(i)