# Generated from pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pascalParser import pascalParser
else:
    from pascalParser import pascalParser
from antlr.pascalParser import pascalParser as pascalP
from antlr.pascalLexer import pascalLexer
# This class defines a complete generic visitor for a parse tree produced by pascalParser.

class pascalVisitor(ParseTreeVisitor):
    
    def __init__(self, file):
        self.file = file
        self.declared_variables = dict()
        self.declared_constants = dict()
        self.ind_count = 0
        self.add_indent = True
        self.indent = "    "
        super().__init__()

    def write_to_file(self, text):
        self.file.write(f"{self.ind_count * self.indent if self.add_indent else ""}{text}")
        if self.add_indent:
            self.add_indent = False
        if "\n" in text:
            self.add_indent = True

    # Visit a parse tree produced by pascalParser#program.
    def visitProgram(self, ctx:pascalParser.ProgramContext):
        self.write_to_file("#include <stdio.h>\n")
        self.visit(ctx.getChild(0))
        self.visit(ctx.block().declarations())
        self.write_to_file("int main(){\n")
        self.ind_count += 1
        self.visit(ctx.block().statement_list())
        self.ind_count -= 1
        self.write_to_file("}")
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#program_header.
    def visitProgram_header(self, ctx:pascalParser.Program_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#declarations.
    def visitDeclarations(self, ctx:pascalParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#type_declarations.
    def visitType_declarations(self, ctx:pascalParser.Type_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#type_decl.
    def visitType_decl(self, ctx:pascalParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#record_spec.
    def visitRecord_spec(self, ctx:pascalParser.Record_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#const_declarations.
    def visitConst_declarations(self, ctx:pascalParser.Const_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#const_decl.
    def visitConst_decl(self, ctx:pascalParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#var_declarations.
    def visitVar_declarations(self, ctx:pascalParser.Var_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#var_decl.
    def visitVar_decl(self, ctx:pascalParser.Var_declContext):
        variable_names = [id.getText() for id in ctx.IDENTIFIER()]
        variable_type = None
        if ctx.type_spec().KW_INTEGER() is not None:
            variable_type = "int"
        if ctx.type_spec().KW_REAL() is not None:
            variable_type = "double"
        if ctx.type_spec().KW_STRING() is not None:
            variable_type = "char[]"#?
        if ctx.type_spec().KW_BOOLEAN() is not None:
            variable_type = "bool"
        if ctx.type_spec().IDENTIFIER() is not None:
            print("DECLARING RECORD TYPES NOT IMPLEMENTED")
        if ctx.type_spec().KW_ARRAY() is not None: 
            print("DECLARING ARRAY TYPES NOT IMPLEMENTED")
        print(variable_names)
        print(variable_type)
        for var_name in variable_names:
            self.declared_variables[var_name] = variable_type
            self.write_to_file(f"{variable_type} {var_name};\n")

        print(self.declared_variables)


    # Visit a parse tree produced by pascalParser#type_spec.
    def visitType_spec(self, ctx:pascalParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#func_and_proc_declarations.
    def visitFunc_and_proc_declarations(self, ctx:pascalParser.Func_and_proc_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#func_declaration.
    def visitFunc_declaration(self, ctx:pascalParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#func_arguments.
    def visitFunc_arguments(self, ctx:pascalParser.Func_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#func_argument_grp.
    def visitFunc_argument_grp(self, ctx:pascalParser.Func_argument_grpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#proc_declaration.
    def visitProc_declaration(self, ctx:pascalParser.Proc_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#block.
    def visitBlock(self, ctx:pascalParser.BlockContext):
        self.ind_count += 1
        self.visitChildren(ctx)
        self.ind_count -= 1


    # Visit a parse tree produced by pascalParser#code_block.
    def visitCode_block(self, ctx:pascalParser.Code_blockContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText().lower() == "begin":
                self.write_to_file("{\n")
                self.ind_count += 1
                continue       
            if child.getText().lower() == "end":
                self.ind_count -= 1
                self.write_to_file("}")
                continue       
            self.visit(child)


    # Visit a parse tree produced by pascalParser#statement_list.
    def visitStatement_list(self, ctx:pascalParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#statement.
    def visitStatement(self, ctx:pascalParser.StatementContext):
        self.visit(ctx.getChild(0))
        if ctx.function_call() is not None or ctx.assignment() is not None:
            self.write_to_file(";")
        self.write_to_file("\n")


    # Visit a parse tree produced by pascalParser#case_statement.
    def visitCase_statement(self, ctx:pascalParser.Case_statementContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText().lower() == "case":
                self.write_to_file("switch(")
                self.ind_count += 1
                continue       
            if child.getText().lower() == "of":
                self.write_to_file(") {\n")
                continue       
            if child.getText().lower() == "else":
                self.write_to_file("default: ")
                continue
            if child.getText().lower() == "end":
                self.ind_count -= 1
                self.write_to_file("}")
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#case_branch.
    def visitCase_branch(self, ctx:pascalParser.Case_branchContext):
        for i, child in enumerate(ctx.getChildren()):
            if isinstance(child, pascalP.Case_labelContext):
                self.write_to_file("case ")
                self.visit(child)
                self.write_to_file(":\n")
                continue     
            if child.getText() == ":":
                self.ind_count += 1
                continue  
            self.visit(child)
        self.write_to_file("break;\n")
        self.ind_count -= 1




    # Visit a parse tree produced by pascalParser#case_label.
    def visitCase_label(self, ctx:pascalParser.Case_labelContext):
        self.write_to_file(ctx.getText())


    # Visit a parse tree produced by pascalParser#for_loop.
    def visitFor_loop(self, ctx:pascalParser.For_loopContext):
            self.write_to_file("for(int ")
            var_name = ctx.getChild(1).getText()
            self.write_to_file(f"{var_name} = ")
            self.visit(ctx.getChild(3))
            self.write_to_file("; ")
            if ctx.KW_TO() is not None:
                self.write_to_file(f"{var_name} <= ")
                self.visit(ctx.getChild(5))
                self.write_to_file("; ")
                self.write_to_file(f"{var_name}++")

            if ctx.KW_DOWNTO() is not None:
                self.write_to_file(f"{var_name} >= ")
                self.visit(ctx.getChild(5))
                self.write_to_file("; ")
                self.write_to_file(f"{var_name}--")
            
            self.write_to_file(")")
            self.visit(ctx.getChild(7))

    # Visit a parse tree produced by pascalParser#repeat_loop.
    def visitRepeat_loop(self, ctx:pascalParser.Repeat_loopContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText().lower() == "repeat":
                self.write_to_file("do{\n")
                continue       
            if child.getText().lower() == "until":
                self.write_to_file("}while(")
                continue
            self.visit(child)
        self.write_to_file(");")



    # Visit a parse tree produced by pascalParser#if_block.
    def visitIf_block(self, ctx:pascalParser.If_blockContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText().lower() == "if":
                self.write_to_file("if(")
                continue       
            if child.getText().lower() == "then":
                self.write_to_file(")")
                continue       
            if child.getText().lower() == "else":
                self.write_to_file("else ")
                continue       
            self.visit(child)


    # Visit a parse tree produced by pascalParser#while_loop.
    def visitWhile_loop(self, ctx:pascalParser.While_loopContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText().lower() == "while":
                self.write_to_file("while(")
                continue       
            if child.getText().lower() == "do":
                self.write_to_file(")")
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#function_call.
    def visitFunction_call(self, ctx:pascalParser.Function_callContext):
        # ctx.getToken(pascalParser.IDENTIFIER, 0)
        function_name = ctx.IDENTIFIER().getText()
        if function_name == "writeLn":
            function_name = "printf"
        self.write_to_file(f"{function_name}(")
        self.visit(ctx.arg_list())        
        self.write_to_file(f")")


    # Visit a parse tree produced by pascalParser#arg_list.
    def visitArg_list(self, ctx:pascalParser.Arg_listContext):
        # print(ctx.getChildren())
        for child in ctx.getChildren():
            if child.getText() == ',':
                self.write_to_file(',')
            else: 
                self.visit(child)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#logic_expression.
    def visitLogic_expression(self, ctx:pascalParser.Logic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#orExpr.
    def visitOrExpr(self, ctx:pascalParser.OrExprContext):
        for i, child in enumerate(ctx.getChildren()):
            if isinstance(child, TerminalNode) and child.getSymbol().type == pascalLexer.KW_OR:
                self.write_to_file(child.getText())
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#andExpr.
    def visitAndExpr(self, ctx:pascalParser.AndExprContext):
        for i, child in enumerate(ctx.getChildren()):
            if isinstance(child, TerminalNode) and child.getSymbol().type == pascalLexer.KW_AND:
                self.write_to_file(child.getText())
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#relation.
    def visitRelation(self, ctx:pascalParser.RelationContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText() in "()":
                self.write_to_file(child.getText())
                continue
            if child.getText() == "=":
                self.write_to_file("==")
                continue       
            if child.getText() == "<>":
                self.write_to_file("!=")
                continue
            if child.getText() == "<":
                self.write_to_file("<")
                continue       
            if child.getText() == "<=":
                self.write_to_file("<=")
                continue       
            if child.getText() == ">=":
                self.write_to_file(">=")
                continue       
            if child.getText() == ">":
                self.write_to_file(">")
                continue       
            if child.getText().lower() == "not":
                self.write_to_file("!")
                continue       
            self.visit(child)


    # Visit a parse tree produced by pascalParser#expression.
    def visitExpression(self, ctx:pascalParser.ExpressionContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText() in "+-":
                self.write_to_file(child.getText())
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#term.
    def visitTerm(self, ctx:pascalParser.TermContext):
        for i, child in enumerate(ctx.getChildren()):
            # print(i, child.getText())
            if child.getText() in "*/":
                self.write_to_file(child.getText())
                continue
            if child.getText().lower() == "div":
                self.write_to_file("/")
                continue       
            if child.getText().lower() == "mod":
                self.write_to_file("%")
                continue       
            # self.write_to_file(child.getText())
            self.visit(child)


    # Visit a parse tree produced by pascalParser#factor.
    def visitFactor(self, ctx:pascalParser.FactorContext):
        for i, child in enumerate(ctx.getChildren()):
            if child.getText() in "+-[].":
                self.write_to_file(child.getText())
                continue
            if isinstance(child, TerminalNode) and child.getSymbol().type == pascalLexer.IDENTIFIER:
                self.write_to_file(child.getText())
                continue       
            self.visit(child)


    # Visit a parse tree produced by pascalParser#assignment.
    def visitAssignment(self, ctx:pascalParser.AssignmentContext):
        # self.write_to_file(ctx.IDENTIFIER(0).getText())
        if ctx.IDENTIFIER(0).getText().lower() == "result":
            self.write_to_file("return ")
            self.visit(ctx.getChild(2)) # 1st is identifier 2nd is assign
            return
        for i, child in enumerate(ctx.getChildren()):
            if child.getText() in "[].":
                self.write_to_file(child.getText())
                continue
            if child.getText() == ":=":
                self.write_to_file("=")
                continue            
            if isinstance(child, TerminalNode) and child.getSymbol().type == pascalLexer.IDENTIFIER:
                self.write_to_file(child.getText())
                continue
            self.visit(child)


    # Visit a parse tree produced by pascalParser#literal.
    def visitLiteral(self, ctx:pascalParser.LiteralContext):
        if ctx.array_literal() is not None:
            self.visit(ctx.array_literal())
            pass
        if ctx.NUMBER() is not None:
            self.write_to_file(ctx.getText())
        if ctx.STRING() is not None:
            self.write_to_file(ctx.getText())
        if ctx.LOGIC_LITERAL() is not None:
            self.write_to_file(ctx.getText())
        if ctx.KW_NIL() is not None:
            self.write_to_file("NULL")
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by pascalParser#array_literal.
    def visitArray_literal(self, ctx:pascalParser.Array_literalContext):
        for child in ctx.getChildren():
            if child.getText() == ",":
                self.write_to_file(",")
                continue
            if child.getText() == "(":
                self.write_to_file("[")
                continue
            if child.getText() == ")":
                self.write_to_file("]")
                continue
            self.visit(child)
            


    # Visit a parse tree produced by pascalParser#array_index_type.
    def visitArray_index_type(self, ctx:pascalParser.Array_index_typeContext):
        return self.visitChildren(ctx)



del pascalParser