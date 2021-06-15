#######################################EQUAL
def equals_or(base, *args):
    for arg in args:
        if base == arg: return True
    return False

def equals_and(base, *args):
    equals = True
    for arg in args:
        if base != arg: equals = False
    return equals
#######################################NOTEQUAL
def notequals_or(base, *args):
    for arg in args:
        if base != arg: return True
    return False

def notequals_and(base, *args):
    equals = True
    for arg in args:
        if base == arg: equals = False
    return equals
#######################################GREATER
def greater_or(base, *args):
    for arg in args:
        if base > arg: return True
    return False

def grater_and(base, *args):
    equals = True
    for arg in args:
        if base > arg: equals = False
    return equals
#######################################LESSER
def lesser_or(base, *args):
    for arg in args:
        if base < arg: return True
    return False

def lesser_and(base, *args):
    equals = True
    for arg in args:
        if base < arg: equals = False
    return equals
#######################################
