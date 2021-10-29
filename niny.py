#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**8)

commands = {
    "push": "push(line)",
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
    "pop": "popS(index)",
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
    "insert": "insertTo()",
    "len": "getLength()",
}

flags = {
    "-d": "debugMode()", "--debug": "debugMode()",
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
    global debug

    checkStack(2)

    item = stack.pop()
    if type(stack[-1]) != list:
        errorWithLine("Can only append to object with type \"list\"")

    stack[-1].append(item)

    if debug:
        full()


def insertTo():
    global debug

    checkStack(1)

    line = f[index]
    line = ignoreComments(line)
    line = line.strip()
    line = line.split(' ')

    line.pop(0)

    if line[0] == '+':
        checkStack(2)

        in_ = stack.pop()
    else:
        in_ = eval(line[0])
    if type(in_) != int:
        errorWithLine("Can only insert to index with type \"int\"")

    item = stack.pop()
    stack.insert(in_, item)

    if debug:
        full()


def getIndex():
    global debug

    global stack, index

    checkStack(1)

    line = f[index]
    line = ignoreComments(line)
    line = line.strip()
    line = line.split(' ')

    if len(line) != 2:
        errorWithLine("Wrong command structure")

    line.pop(0)

    if line[0] == '+':
        checkStack(2)

        in_ = stack.pop()
    else:
        in_ = eval(line[0])

    del line

    if type(in_) != int:
        errorWithLine("Can only get index with type \"int\"")

    a = stack[-1]
    if type(a) != list:
        errorWithLine("Can only get index of objects with type \"list\"")

    stack.append(a[in_])

    if debug:
        full()


def getLength():
    global stack
    stack.append(len(stack))


def errorWithLine(msg):
    line = f[index]

    print(msg)
    print(f"Line {index + 1}\n-> ", end='')
    print(line, end='')

    exit()


def checkStack(length):
    if len(stack) < length:
        errorWithLine("Not enough elements in stack")


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
    global debug

    global stack

    if type(stack[-1]) != list:
        errorWithLine("Can only flat objects with \"list\" type")

    a = stack.pop()
    stack.extend(flat_list(a))

    if debug:
        full()


def reverse():
    global debug

    global stack
    stack = stack[::-1]

    if debug:
        full()


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
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(1 if a == 1 and b == 1 else 0)

    if debug:
        full()


def logicEquals():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(1 if a == b else 0)

    if debug:
        full()


def logicLessThan():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(1 if a < b else 0)

    if debug:
        full()


def logicGreaterThan():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(1 if a > b else 0)

    if debug:
        full()


def logicNot():
    global debug

    checkStack(1)

    cond = stack.pop()
    if cond == 1:
        stack.append(0)
    else:
        stack.append(1)

    if debug:
        full()


def logicOr():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(1 if a == 1 or b == 1 else 0)

    if debug:
        full()


def getType():
    global debug

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

    if debug:
        full()


def condition(index):
    checkStack(1)

    line = f[index]
    line = ignoreComments(line)

    header = line.split()
    length = len(header)

    if length == 6:
        cond_true = header[2]
        cond_false = header[5]

        if cond_true not in macros or cond_false not in macros:
            errorWithLine("Invalid macros in condition")

        cond = stack.pop()

        if cond == 1:
            runMacro(cond_true)
        else:
            runMacro(cond_false)

    elif length == 3:
        cond_true = header[2]

        if cond_true not in macros:
            errorWithLine("Invalid macros in condition")

        cond = stack.pop()

        if cond == 1:
            runMacro(cond_true)

    else:
        errorWithLine("Wrong condition structure")


def divmode():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    first, second = divmod(a, b)

    stack.append(first)
    stack.append(second)

    if debug:
        full()


def root():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a ** (1 / b))

    if debug:
        full()


def powS():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a ** b)

    if debug:
        full()


def dup():
    global debug

    checkStack(1)

    stack.append(stack[-1])

    if debug:
        full()


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
    global debug

    checkStack(1)

    length = len(line)
    if length == 1:
        pass
    elif length == 2:
        if line[1] == '+':
            checkStack(2)

            index = stack.pop()
        else:
            index = eval(line[1])
    else:
        errorWithLine("Syntax Error")

    if type(index) != int:
        errorWithLine("Int type should be provided for getting the element in stack")

    stack.append(stack[index])

    if debug:
        full()


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

    start_index = index
    index += 1

    while True:
        body = f[index].strip()

        if body == "end":
            macros[name] = (start_index + 1, index - 1)
            break

        index += 1


def ignoreComments(line):
    if '$' not in line:
        return line

    return line[:line.index('$')]


def popS(index):
    global debug

    checkStack(1)

    line = f[index]
    line = ignoreComments(line)
    line = line.strip()
    line = line.split()

    if len(line) == 1:
        in_ = -1
    elif len(line) == 2:
        line.pop(0)
        in_ = line[0]
        if in_ == '+':
            checkStack(2)

            in_ = stack.pop()
        else:
            in_ = eval(in_)
        if type(in_) != int:
            errorWithLine("Can take index with type \"int\"")
    else:
        errorWithLine("Wrong command structure")

    stack.pop(in_)

    if debug:
        full()


def push(line):
    global debug

    line.pop(0)

    line = ' '.join(line)
    line = line.strip()

    if line == '':
        errorWithLine("Invalid command structure")

    stack.append(eval(line))

    if debug:
        full()


def deleteM(line):
    line.pop(0)

    line = ' '.join(line)
    line = line.strip()

    del macros[line]


def add():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a + b)

    if debug:
        full()


def mult():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a * b)

    if debug:
        full()


def div():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a / b)

    if debug:
        full()


def sub():
    global debug

    checkStack(2)

    a = stack.pop()
    b = stack.pop()

    stack.append(a - b)

    if debug:
        full()


def swp():
    global debug

    checkStack(2)

    stack[-1], stack[-2] = stack[-2], stack[-1]

    if debug:
        full()


def dump(line, ending=''):
    checkStack(1)

    line.pop(0)
    line = ' '.join(line)
    line = line.strip()

    if len(line) != 0:
        line = eval(line)

    print(stack[-1], end=line)


def runMacro(com_name):
    global debug

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

    if debug:
        full()


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

    global debug

    if debug:
        full()

    while index < len(f):
        line = f[index]
        line = ignoreComments(line)
        line = line.strip()

        if len(line) == 0:
            index += 1
            continue

        execLine(line, index)
        index += 1


def debugMode():
    global debug
    debug = True


if __name__ == "__main__":
    global args

    global debug
    debug = False

    args = sys.argv
    args.pop(0)
    
    index = 0
    while index < len(args):
        arg = args[index]
        if arg in flags:
            eval(flags[arg])

            args.pop(index)
            index -= 1

        index += 1

    if len(args) != 1:
        print("Invalid flags")
        exit()

    main(args[0])

    exit()
