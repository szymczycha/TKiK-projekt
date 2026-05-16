from antlr4 import *
from antlr.pascalLexer import pascalLexer
from antlr.pascalParser import pascalParser
from antlr.pascalVisitor import pascalVisitor
from helper.functions import print_tree

filename = f"pascal_code/hello_world.pas"
# filename = "pascal_code/9.pas"
print(filename)

input_stream = FileStream(filename)

lexer = pascalLexer(input_stream)
stream = CommonTokenStream(lexer)

parser = pascalParser(stream)

tree = parser.program()

out_filename = "test.c"
with open(out_filename, "w") as out_file:
    visitor = pascalVisitor(out_file)
    tree.accept(visitor)
    
print(tree.toStringTree(recog=parser))
