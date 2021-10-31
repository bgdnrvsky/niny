#!/usr/bin/python3
import sys
sys.setrecursionlimit(10 ** 8)

commands = {
    # Basic commands for working with stack
    "full": "full(index)",
    "push": "push(line, index)",
    "dump": "dump(line, index)",
    "dup": "duplicateItemInStack(line, index)",
    "pop": "popFromStack(line, index)",
    "swp": "swapElsInStack(line, index)",
    "change": "changePlaces(line, index)",
    "rev": "reverseStack(index)",
    "len": "stackLength()",

    # Arithmetic commands
    "add": "arithmeticAddition(line, index)",
    "sub": "arithmeticSubstraction(line, index)",
    "mult": "arithmeticMultiplication(line, index)",
    "div": "arithmeticDivision(line, index)",
    "pow": "arithmeticExponentiation(line, index)",
    "root": "arithmeticRoot(line, index)",
    "divmod": "arithmeticRemainderDivision(line, index)",

    # Logic commands
    "if": "logicIf(line, index)",
    "or": "logicOr(line, index)",
    "and": "logicAnd(line, index)",
    "not": "logicNot(line, index)",
    "==": "logicEquals(line, index)",
    '<': "logicGreaterThan(line, index)",
    '>': "logicLessThan(line, index)",

    # Typecasting commands
    "type": "getType(line, index)",
    "int": "typecastToInt(index)",
    "bool": "typecastToBool(line, index)",
    "float": "typecastToFloat(line, index)",
    "string": "typecastToString(line, index)",
    "list": "typecastToList(line, index)",

    # Commands for working with arrays
    "append": "appendTo(line, index)",
    "insert": "insertTo(line, index)",
    "id": "getIndex(line, index)",
    "flat": "flatList(line, index)",

    # Other commands
    "inp": "getInput()",
    "get": "getItem(line, index)",

    # Commands for operations with macros
    "macro": "createMacro(line, index)",
    "del": "deleteMacro(line, index)",
}

flags = {
    "-d": "debugMode()", "--debug": "debugMode()",
    "-ndms": "ignoreDebugMessages()", "--ignoredebugmsgs": "ignoreDebugMessages()",
}


# Functions for basic commands
def full(index):
    """ Command for printing current stack condition """
    global stack
    global debug
    
    if debug:
        print(index + 1, ": ", sep='', end='')

    print(stack)


def push(line, index):
    """ Command for appending value to the stack """
    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    line = line.strip().split(' ')

    line.pop(0)  # Removing the command itself
    line = ' '.join(line)

    if line == '':
        errorWithLine("Invalid command structure", line_copy, index)
    
    del line_copy
    stack.append(eval(line))

    if debug:
        full(index)


def dump(line, index):
    """ Command for printing the last item in stack """
    checkStack(1, line, index)

    line = line.strip().split(' ')

    line.pop(0)  # Removing the command itself
    line = ' '.join(line)

    if len(line) == 0:
        ending = ''
    else:
        ending = eval(line)

    print(stack[-1], end=ending)


def duplicateItemInStack(line, index):
    """ Command for duplicating last element in stack """
    checkStack(1, line, index)

    global stack
    global debug

    stack.append(stack[-1])

    if debug:
        full(index)


def popFromStack(line, index):
    """ Command for removing element in stack by it's index """
    checkStack(1, line, index)

    global stack
    global debug

    line = line.strip().split(' ')

    if len(line) == 1:
        indexForRemoving = -1 # For removing last element from stack
    elif len(line) == 2:
        line.pop(0) # Removing the command itself
        indexForRemoving = line[0]
        
        if indexForRemoving == '+': # In this case, index for removing will be taken from last element in stack
            checkStack(2, line, index)
            indexForRemoving = stack.pop()
        else:
            indexForRemoving = eval(indexForRemoving)

    stack.pop(indexForRemoving)

    if debug:
        full(index)


def swapElsInStack(line, index):
    """ Command for changing places of 2 last elements in stack """
    checkStack(2, line, index)

    global stack
    global debug

    stack[-1], stack[-2] = stack[-2], stack[-1]

    if debug:
        full(index)


def changePlaces(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    line = line.strip().split(' ')

    line.pop(0) # Removing command itself

    if line[0] == '+':
        checkStack(2, line, index)
        
        insertIndex = stack.pop()
    else:
        insertIndex = eval(line[0])

    if type(insertIndex) != int:
        errorWithLine("Can only insert to index with type \"int\"")

    item = stack.pop()

    stack.insert(insertIndex, item)

    if debug:
        full(index)

    del line_copy


def reverseStack(index):
    global stack
    global debug

    stack = stack[::-1]

    if debug:
        full(index)


def stackLength():
    global stack
    global debug

    stack.append(len(stack))

    if debug:
        full(index)


# Functions for arithmetic commands
def arithmeticAddition(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a + b)

    if debug:
        full(index)


def arithmeticSubstraction(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a - b)

    if debug:
        full(index)


def arithmeticMultiplication(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a * b)

    if debug:
        full(index)


def arithmeticDivision(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a / b)

    if debug:
        full(index)


def arithmeticExponentiation(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a ** b)

    if debug:
        full(index)


def arithmeticRoot(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.append(a ** (1 / b))

    if debug:
        full(index)


def arithmeticRemainderDivision(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    a = stack.pop()
    b = stack.pop()

    stack.extend(divmod(a, b))
    
    if debug:
        full(index)


# Functions for logic commands
def logicIf(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    if debug:
        print(f"{index + 1}: Inside the condition'")

    header = line.strip().split()
    length = len(header)

    if length == 6: # if do macro_true else do macro_false
        macro_true = header[2]
        macro_false = header[5]

        if macro_true not in macros or macro_false not in macros:
            errorWithLine("Undefined macros in condition", line_copy, index)

        condition = stack.pop()

        if condition == 1: # True
            if debug:
                print("The condition result is True")
                full(index)

            runMacro(macro_true, line)
        elif condition == 0: # False
            if debug:
                print("The condition result is False")
                full(index)

            runMacro(macro_false, line)

        else:
            errorWithLine("Wrong input for \"if\" structure, should be 1(true) or 0(false)", line, index)
        

    elif length == 3: # if do macro_true
        macro_true = header[2]

        if macro_true not in macros:
            errorWithLine("Undefined macro in condition", line, index)

        condition = stack.pop()

        if condition == 1: # True
            if debug:
                print("The condition is True")
                full(index)

            runMacro(macro_true, line)

    else:
        errorWithLine("Wrong condition structure", line, index)

    del line_copy


def logicOr(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    condition1 = stack.pop()
    condition2 = stack.pop()

    if condition1 not in [0, 1] or condition2 not in [0, 1]:
        errorWithLine("Wrong input for \"or\" structure, should be 1(true) or 0(false)")

    stack.append(1 if condition1 or condition2 else 0)

    if debug:
        full(index)

    del line_copy


def logicAnd(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    condition1 = stack.pop()
    condition2 = stack.pop()

    if condition1 not in [0, 1] or condition2 not in [0, 1]:
        errorWithLine("Wrong input for \"and\" command, should be 1(true) or 0(false)")

    stack.append(condition1 and condition2)

    if debug:
        full(index)

    del line_copy


def logicNot(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    condition1 = stack.pop()

    if condition1 not in [0, 1]:
        errorWithLine("Wrong input for \"not\" command, should be 1(true) or 0(false)")

    stack.append(not condition1)
    stack[-1] = 0 if stack[-1] == False else 1

    if debug:
        full(index)

    del line_copy

def logicEquals(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    item1 = stack.pop()
    item2 = stack.pop()

    stack.append(1 if item1 == item2 else 0)

    if debug:
        full(index)


def logicGreaterThan(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    item1 = stack.pop()
    item2 = stack.pop()

    stack.append(0 if item1 > item2 else 1)

    if debug:
        full(index)


def logicLessThan(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    item1 = stack.pop()
    item2 = stack.pop()

    stack.append(0 if item1 < item2 else 1)

    if debug:
        full(index)


# Functions for typecasting commands
def getType(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()
    typeOfItem = type(item)

    if typeOfItem == int:
        stack.append("int")
    elif typeOfItem == str:
        stack.append("str")
    elif typeOfItem == float:
        stack.append("float")
    elif typeOfItem == list:
        stack.append("list")

    if debug:
        full(index)


def typecastToInt(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()
    
    stack.append(int(item))

    if debug:
        full(index)


def typecastToBool(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()

    stack.append(bool(item))

    if debug:
        full(index)


def typecastToFloat(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()

    stack.append(float(item))

    if debug:
        full(index)


def typecastToString(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()

    stack.append(str(item))

    if debug:
        full(index)


def typecastToList(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    item = stack.pop()

    stack.append(list(item))

    if debug:
        full(index)

# Functions for working with arrays
def appendTo(line, index):
    checkStack(2, line, index)

    global stack
    global debug

    item = stack.pop()

    if type(stack[-1]) != list:
        errorWithLine("Can only append to object with type \"list\"", line, index)

    stack[-1].append(item)

    if debug:
        full(index)



def insertTo(line, index):
    checkStack(3, line, index)

    global stack
    global debug

    indexToInsert = stack.pop()
    item = stack.pop()

    if type(stack[-1]) != list:
        errorWithLine("Can only insert to object with type \"list\"", line, index)

    if type(indexToInsert) != int:
        errorWithLine("Can only insert to object with index type of \"int\"", line, index)

    stack[-1].insert(indexToInsert, item)

    if debug:
        full(index)


def getIndex(line, index):
    """ Command for getting element in an array by it's index """
    checkStack(1, line, index)
    global stack
    global debug

    line_copy = line # Need this for throwing ann error

    line = line.strip().split(' ')

    line.pop(0) # Removing the command itself

    if line[0] == '+':
        checkStack(2, line, index)

        indexToGet = eval(stack.pop())
    else:
        indexToGet = eval(line[0])
    
    if type(stack[-1]) != list:
        errorWithLine("Can only get an element of type \"list\"", line, index)

    stack.append(stack[-1][indexToGet])

    if debug:
        full(index)

    del line_copy


def flatten(array):
    result = []

    for item in array:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


def flatList(line, index):
    checkStack(1, line, index)

    global stack
    global debug

    stack.extend(flatten(stack.pop()))

    if debug:
        full(index)


# Other commands 
def getInput():
    user_input = input()

    try:
        stack.append(eval(user_input))
    except (NameError, SyntaxError):
        # In case when user enters a string
        user_input += "\""
        user_input = user_input[::-1]

        user_input += "\""
        user_input = user_input[::-1]

    stack.append(eval(user_input))


def getItem(line, index):
    """ Function for getting an item in stack by it's index """
    global stack
    global debug

    line_copy = line

    line = line.strip().split(' ')

    line.pop(0) # Removing the command itself

    if line == []:
        indexToGet = -1
    elif line[0] == '+':
        checkStack(1, line, index)

        indexToGet = stack.pop()
    else:
        indexToGet = eval(line[0])
    
    if type(indexToGet) != int:
        errorWithLine("Can only get item in stack with index type of \"int\"", line_copy, index)

    stack.append(stack[indexToGet])

    if debug:
        full(index)

    del line_copy


# Macro functions
def createMacro(line, index): 
    global debug
    global document, macros
    global line_index
    
    header = line.strip().split(' ')

    if len(header) != 3:
        errorWithLine("Wrong macro header", line, index)

    name = header[1]
    keywords = header[0], header[2] # For checking the structure

    if debug:
        print(f"Definition of \"{name}\" macro")

    if keywords != ("macro", "do"):
        errorWithLine("Invalid macro header", line, index)

    del keywords

    start_index = index + 1

    while True:
        body = ignoreComments(document[index + 1])

        if body.strip() == "end":
            macros[name] = (start_index, index)
            break
        
        index += 1

    line_index = index + 1

    if debug:
        print(macros)


def runMacro(name, line):
    global debug
    global macros, document

    if debug:
        print(f"Running macro {name}")

    if name not in macros:
        errorWithLine("Undefined macro", line, index)

    start_index, stop_index = macros[name]

    while start_index <= stop_index:
        m_line = ignoreComments(document[start_index])

        if len(m_line.strip()) != 0:
            execLine(m_line, start_index)

        start_index += 1

    if debug:
        full(index)


def deleteMacro(line, index):
    global debug
    global macros

    line = line.strip().split(' ')

    line.pop(0) # Removing the command itself
    
    if len(line) != 1:
        errorWithLine("Wrong command structure", line, index)

    name = line[0]

    if name not in macros:
        errorWithLine("Undefined macro", line, index)

    del macros[name]

    if debug:
        print(macros)


# Flags functions
def debugMode():
    """ Turning on the debug mode """
    global debug
    global ignoreDebugMessage

    if not ignoreDebugMessage:
        print("DEBUG MODE")
        print("FORMAT: line_number: stack_condition")

    debug = True


def ignoreDebugMessages():
    global ignoreDebugMessage

    ignoreDebugMessage = True


# Basic functions
def checkStack(length, line, index):
    """ Basic function for checking amount of items in stack """
    global stack

    if len(stack) < length:
        errorWithLine("Not enough elements in stack", line, index)
        exit()


def ignoreComments(line):
    return line if '$' not in line else line[:line.index('$')]


def errorWithLine(message, line, index):
    """ Basic function for throwing errors """
    print(message)
    print(f"Line {index + 1}\n-> ", end='')
    print(line, end='')

    exit()


def execLine(line, index):
    """ Main line computing func """
    command_name = line.strip().split(' ')[0]  # Getting main command through extra spaces

    if command_name in commands:
        eval(commands[command_name])
    elif command_name in macros:
        runMacro(command_name, line)
    else:
        errorWithLine("Invalid command", line, index)


def main(path):
    # Checking for the right file extension
    filename = path.split('/')[-1]
    if filename.split('.')[1] != "nn":
        print("Invalid file extension")
        usage()

    global document, stack, macros  # Some basic structures

    document = open(path).readlines()
    stack = []
    macros = {}  # Pattern - {"macro_name": (header_index, end_index)}

    # Reading the file
    global line_index

    line_index = 0

    while line_index < len(document):
        line = ignoreComments(document[line_index])

        if len(line.strip()) != 0:
            execLine(line, line_index)

        line_index += 1


def usage():
    print("Usage: python3 niny.py [-d | --debug] [filename]")
    print("Some arguments:")
    print("-d, --debug\tTo turn on debug mode, after this you will see stack condition after almost each operation, that affects stack.")
    print("-ndms, --ignoredebugmsgs\tTo turn off the debug startup message.")
    
    exit()


if __name__ == "__main__":
    args = sys.argv
    args.pop(0) # Removing python file

    global debug
    debug = False # Debug mode

    global ignoreDebugMessage
    ignoreDebugMessage = False # Mode for ignoring debug startup message

    # Going through the launch arguments
    index = 0

    while index < len(args):
        arg = args[index]
        if arg in flags:
            eval(flags[arg])

            args.pop(index)
            index -= 1

        index += 1

    if len(args) != 1:  # Must contain only name of file, but I think I will remove this dumb check in future
        print("Invalid flags")
        usage()

    main(args[0])
    exit()
