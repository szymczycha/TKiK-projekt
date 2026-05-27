from antlr4 import *
from antlr.pascalLexer import pascalLexer
from antlr.pascalParser import pascalParser
from antlr.pascalVisitor import pascalVisitor
import argparse
import os

parser = argparse.ArgumentParser(
    prog="patocc",
    description="Pascal To C Compiler",
    epilog="All remaining arguments will be interpreted as paths to files for compiling."
)
parser.add_argument("path", help="path to Pascal file to compile to C")
parser.add_argument("-d","--directory", 
                    help="interpret path as a directory of .pas files to convert to C",
                    action="store_true")
parser.add_argument("-o", "--outdir",
                    help="path to output directory")
args, list_of_paths = parser.parse_known_args()
paths_to_compile = []
if not args.directory:
    paths_to_compile.append(args.path)
    paths_to_compile += list_of_paths
if args.directory:
    for file in os.listdir(args.path):
        if file.endswith(".pas"):
            paths_to_compile.append(args.path+file)

out_directory = ""
if args.outdir:
    out_directory = args.outdir

for path in paths_to_compile:
    print(path)
    filename, file_extension = os.path.splitext(os.path.basename(path))

    input_stream = FileStream(path)

    lexer = pascalLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = pascalParser(stream)

    tree = parser.program()

    out_filename = f"{out_directory}{filename}.c"
    with open(out_filename, "w") as out_file:
        visitor = pascalVisitor(out_file)
        tree.accept(visitor)
