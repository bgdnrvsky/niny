#!/usr/bin/python3
import sys

commands = {
    "push": "push(line)",
    "include": "library(index)",
    "del": "deleteM(line)",
    "add": "add()",
    "sub": "sub()",
    "mult": "mult()",
    "pow": "powS()",
    "root": "root()",
    "div": "div()",
    "type": "getType()",
    "or": "logicOr()",
    "not": "logicNot()",
    "and": "logicAnd()",
    '==': "logicEquals()",
    '<': "logicLessThan()",
    '>': "logicGreaterThan()",
    "pop": "popS()",
    "dup": "dup()",
    "divmod": "divmode()",
    "dump": "dump(line)",
    "inp": "inp()",
    "full": "full()",
    "if": "condition(index)",
    "get": "getVal(line)",
    "swp": "swp()",
    "macro": "macro()",
    "rev": "reverse()",
    "int": "typecastInt()",
    "bool": "typecastBool()",
    "float": "typecastFloat()",
    "string": "typecastString()",
}


def typecastInt():
    global stack
    stack[-1] = int(stack[-1])


def typecastBool():
    global stack
    stack[-1] = bool(stack[-1])


def typecastFloat():
    global stack
    stack[-1] = float(stack[-1])


def typecastString():
    global stack
    stack[-1] = str(stack[-1])


def library(index):
    # Making input file readable
    """
    line = f[index]
    line = line.strip()
    line = line.split()
    line.pop(0)
    line = ' '.join(line)
    line = line.strip()
    line = list(line)
    line.pop(0)
    line.pop()
    line = ''.join(line)
    line += ".nn"

    content = cat(line)
    f[index] = content
    """
    assert False, "Not implemented"


def errorWithLine():
    line = f[index]
    print(f"Line {index + 1}\n-> ", end='')
    print(line, end='')
    exit()


def checkStack(length):
    if len(stack) < length:
        print("Not enough elements in stack")
        errorWithLine()


def cat(path):
    result = ""
    f = open(path)
    for line in f:
        result += line

    return result


def reverse():
    global stack
    stack = stack[::-1]


def full():
    if len(stack) == 0:
        print([])
        return

    for item in stack:
        print(item)


def logicAnd():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(1 if a == 1 and b == 1 else 0)


def logicEquals():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(1 if a == b else 0)


def logicLessThan():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(1 if a < b else 0)


def logicGreaterThan():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(1 if a > b else 0)


def logicNot():
    checkStack(1)
    cond = stack.pop()
    if cond == 1:
        stack.append(0)
    else:
        stack.append(1)


def logicOr():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(1 if a == 1 or b == 1 else 0)


def getType():
    checkStack(1)
    a = stack.pop()
    type_ = type(a)

    if type_ == int:
        stack.append("int")
    elif type_ == str:
        stack.append("str")
    elif type_ == float:
        stack.append("float")


def condition(start_index):
    global index

    line = f[start_index]
    header = line.split()
    length = len(header)
    if length == 6:
        cond_true = header[2]
        cond_false = header[5]

        if cond_true not in macros or cond_false not in macros:
            print("Invalid macros in condition")
            errorWithLine()
            exit()

        cond = stack.pop()
        if cond == 1:
            execLine(cond_true, start_index)
        else:
            execLine(cond_false, start_index)

    elif length == 3:
        cond_true = header[2]

        if cond_true not in macros:
            print("Invalid macros in condition")
            errorWithLine()
            exit()

        cond = stack.pop()
        if cond == 1:
            execLine(cond_true, start_index)

    else:
        errorWithLine()
        assert False, "Wrong condition structure"


def divmode():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    first, second = divmod(a, b)
    stack.append(first)
    stack.append(second)


def root():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a ** (1 / b))


def powS():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a ** b)


def dup():
    checkStack(1)
    stack.append(stack[-1])


def inp():
    inp_ = input()
    try:
        stack.append(eval(inp_))
    except NameError:
        try:
            inp_ += "\""
            inp_ = inp_[::-1]
            inp_ += "\""
            inp_ = inp_[::-1]
        except NameError:
            stack.append(eval(inp_))
            return
        stack.append(eval(inp_))


def getVal(line, index=-1):
    checkStack(1)
    length = len(line)
    if length == 1:
        pass
    elif length == 2:
        index = eval(line[1])
    else:
        print("Syntax Error")
        errorWithLine()
        exit()

    if type(index) != int:
        print("Int type should be provided for getting the element in STACK")
        errorWithLine()

    stack.append(stack[index])


def macro():
    global index

    header = f[index]
    header = ignoreComments(header)
    header = header.split()
    if len(header) != 3:
        print("Wrong macro header")
        errorWithLine()
    name = header[1]

    keywords = header[0], header[2]
    if keywords != ("macro", "do"):
        print("Wrong macro header")
        errorWithLine()

    del keywords

    stop_index = index + 1
    while True:
        body = f[stop_index].strip()
        break_index = -1

        if body == "break":
            break_index = stop_index

        if body == "end":
            macros[name] = (index + 1, stop_index - 1)
            index = stop_index
            break

        stop_index += 1


def ignoreComments(line):
    if '$' not in line:
        return line

    return line[:line.index('$')]


def popS():
    checkStack(1)
    stack.pop()


def push(line):
    line.pop(0)
    line = ' '.join(line)
    line = line.strip()
    stack.append(eval(line))


def deleteM(line):
    line.pop(0)
    line = ' '.join(line)
    line = line.strip()

    del macros[line]


def add():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)


def mult():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)


def div():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a / b)


def sub():
    checkStack(2)
    a = stack.pop()
    b = stack.pop()
    stack.append(a - b)


def swp():
    checkStack(2)
    stack[-1], stack[-2] = stack[-2], stack[-1]


def dump(line, ending=''):
    checkStack(1)
    try:
        print(stack[-1], end=eval(line[1]))
    except IndexError:
        print(stack[-1], end=ending)


def runMacro(com_name):
    start_index, stop_index = macros[com_name]
    while start_index <= stop_index:
        m_line = f[start_index]
        m_line = ignoreComments(m_line)
        m_line = m_line.strip()

        if len(m_line) == 0:
            start_index += 1
            continue

        execLine(m_line, start_index)
        start_index += 1



def execLine(line, index):
    line = line.strip()
    line = line.split()
    com_name = line[0]

    if com_name in commands:
        eval(commands[com_name])
    else:
        if com_name in macros:
            runMacro(com_name)
        else:
            print("Unknown command")
            errorWithLine()
            exit()


def main(path):
    filename = path.split('/')[-1]
    if filename.split('.')[-1] != "nn":
        print("Invalid file extension")
        exit()

    global f, stack, macros
    stack = []
    macros = {}
    f = open(path).readlines()

    global index
    index = 0

    while index < len(f):
        line = f[index]
        line = ignoreComments(line)
        line = line.strip()

        if len(line) == 0:
            index += 1
            continue

        execLine(line, index)

        index += 1


if __name__ == "__main__":
    global args
    args = sys.argv
    main(args[1])

    exit()

