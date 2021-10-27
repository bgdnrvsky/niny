#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**8)

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
    "list": "typecastList()",
    "id": "getIndex()",
    "flat": "flatten()",
    "append": "appendTo()",
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


def typecastList():
    global stack
    stack[-1] = list(stack[-1])


def appendTo():
    checkStack(2)
    item = stack.pop()
    if type(stack[-1]) != list:
        errorWithLine("Can only append to object with type \"list\"")

    stack[-1].append(item)


def getIndex():
    global stack, index

    checkStack(1)
    line = f[index]
    line = line.split(' ')
    if len(line) != 2:
        errorWithLine("Wrong command structure")
    line.pop(0)

    in_ = eval(line[0])
    del line
    if type(in_) != int:
        errorWithLine("Can only get index with type \"int\"")

    a = stack[-1]
    if type(a) != list:
        errorWithLine("Can only get index of objects with type \"list\"")

    stack.append(a[in_])


def library(index):
    assert False, "Not implemented"


def errorWithLine(msg):
    line = f[index]
    print(msg)
    print(f"Line {index + 1}\n-> ", end='')
    print(line, end='')
    exit()


def checkStack(length):
    if len(stack) < length:
        errorWithLine("Not enough elements in stack")


def cat(path):
    result = ""
    f = open(path)
    for line in f:
        result += line

    return result


def is_array(array):
    return type(array) == list


def flat_list(array):
    result = []

    for item in array:
        if is_array(item):
            result.extend(flat_list(item))
        else:
            result.append(item)

    return result


def flatten():
    global stack
    if type(stack[-1]) != list:
        errorWithLine("Can only flat objects with \"list\" type")

    a = stack.pop()
    stack.extend(flat_list(a))


def reverse():
    global stack
    stack = stack[::-1]


def full():
    if len(stack) == 0:
        print([])
        return
    
    length = len(stack)
    for index in range(length):
        print(stack[index], end='')
        if index != length - 1:
            print(", ", end='')

    print()


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
    elif type_ == list:
        stack.append("list")


def condition(start_index):
    checkStack(1)
    global index

    line = f[start_index]
    line = ignoreComments(line)
    header = line.split()
    length = len(header)
    if length == 6:
        cond_true = header[2]
        cond_false = header[5]

        if cond_true not in macros or cond_false not in macros:
            errorWithLine("Invalid macros in condition")
            exit()

        cond = stack.pop()
        if cond == 1:
            execLine(cond_true, start_index)
        else:
            execLine(cond_false, start_index)

    elif length == 3:
        cond_true = header[2]

        if cond_true not in macros:
            errorWithLine("Invalid macros in condition")
            exit()

        cond = stack.pop()
        if cond == 1:
            execLine(cond_true, start_index)

    else:
        errorWithLine("Wrong condition structure")


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
        errorWithLine("Syntax Error")

    if type(index) != int:
        errorWithLine(
            "Int type should be provided for getting the element in STACK")

    stack.append(stack[index])


def macro():
    global index

    header = f[index]
    header = ignoreComments(header)
    header = header.split()
    if len(header) != 3:
        errorWithLine("Wrong macro header")
    name = header[1]

    keywords = header[0], header[2]
    if keywords != ("macro", "do"):
        print("Wrong macro header")
        errorWithLine("Wrong macro header")

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
    global index

    line = f[index]
    line = ignoreComments(line)
    line = line.split()
    if len(line) == 1:
        in_ = -1
    elif len(line) == 2:
        line.pop(0)
        in_ = line[0]
        in_ = eval(in_)
        if type(in_) != int:
            errorWithLine("Can take index with type \"int\"")
    else:
        errorWithLine("Wrong command structure")

    stack.pop(in_)


def push(line):
    line.pop(0)
    line = ' '.join(line)
    line = line.strip()
    if line == '':
        errorWithLine("Invalid command structure")

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
    line.pop(0)
    line = ' '.join(line)

    line = line.strip()
    if len(line) != 0:
        line = eval(line)

    print(stack[-1], end=line)


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
            errorWithLine("Unknown command")
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
