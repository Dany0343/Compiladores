import ast

def astGen(code):
    tree = ast.parse(code)

    return tree