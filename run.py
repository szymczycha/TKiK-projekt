from antlr4 import *
from antlr.pascalLexer import pascalLexer
from antlr.pascalParser import pascalParser

from helper.functions import print_tree

for i in range(1, 18):
    filename = f"pascal_code/{i}.pas"
    # filename = "pascal_code/9.pas"
    print(filename)

    input_stream = FileStream(filename)

    lexer = pascalLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = pascalParser(stream)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))
# print_tree(tree, parser)