# Generated from pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pascalParser import pascalParser
else:
    from pascalParser import pascalParser

# This class defines a complete listener for a parse tree produced by pascalParser.
class pascalListener(ParseTreeListener):

    # Enter a parse tree produced by pascalParser#program.
    def enterProgram(self, ctx:pascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by pascalParser#program.
    def exitProgram(self, ctx:pascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by pascalParser#program_header.
    def enterProgram_header(self, ctx:pascalParser.Program_headerContext):
        pass

    # Exit a parse tree produced by pascalParser#program_header.
    def exitProgram_header(self, ctx:pascalParser.Program_headerContext):
        pass


    # Enter a parse tree produced by pascalParser#declarations.
    def enterDeclarations(self, ctx:pascalParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by pascalParser#declarations.
    def exitDeclarations(self, ctx:pascalParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by pascalParser#type_declarations.
    def enterType_declarations(self, ctx:pascalParser.Type_declarationsContext):
        pass

    # Exit a parse tree produced by pascalParser#type_declarations.
    def exitType_declarations(self, ctx:pascalParser.Type_declarationsContext):
        pass


    # Enter a parse tree produced by pascalParser#type_decl.
    def enterType_decl(self, ctx:pascalParser.Type_declContext):
        pass

    # Exit a parse tree produced by pascalParser#type_decl.
    def exitType_decl(self, ctx:pascalParser.Type_declContext):
        pass


    # Enter a parse tree produced by pascalParser#record_spec.
    def enterRecord_spec(self, ctx:pascalParser.Record_specContext):
        pass

    # Exit a parse tree produced by pascalParser#record_spec.
    def exitRecord_spec(self, ctx:pascalParser.Record_specContext):
        pass


    # Enter a parse tree produced by pascalParser#const_declarations.
    def enterConst_declarations(self, ctx:pascalParser.Const_declarationsContext):
        pass

    # Exit a parse tree produced by pascalParser#const_declarations.
    def exitConst_declarations(self, ctx:pascalParser.Const_declarationsContext):
        pass


    # Enter a parse tree produced by pascalParser#const_decl.
    def enterConst_decl(self, ctx:pascalParser.Const_declContext):
        pass

    # Exit a parse tree produced by pascalParser#const_decl.
    def exitConst_decl(self, ctx:pascalParser.Const_declContext):
        pass


    # Enter a parse tree produced by pascalParser#var_declarations.
    def enterVar_declarations(self, ctx:pascalParser.Var_declarationsContext):
        pass

    # Exit a parse tree produced by pascalParser#var_declarations.
    def exitVar_declarations(self, ctx:pascalParser.Var_declarationsContext):
        pass


    # Enter a parse tree produced by pascalParser#var_decl.
    def enterVar_decl(self, ctx:pascalParser.Var_declContext):
        pass

    # Exit a parse tree produced by pascalParser#var_decl.
    def exitVar_decl(self, ctx:pascalParser.Var_declContext):
        pass


    # Enter a parse tree produced by pascalParser#type_spec.
    def enterType_spec(self, ctx:pascalParser.Type_specContext):
        pass

    # Exit a parse tree produced by pascalParser#type_spec.
    def exitType_spec(self, ctx:pascalParser.Type_specContext):
        pass


    # Enter a parse tree produced by pascalParser#func_and_proc_declarations.
    def enterFunc_and_proc_declarations(self, ctx:pascalParser.Func_and_proc_declarationsContext):
        pass

    # Exit a parse tree produced by pascalParser#func_and_proc_declarations.
    def exitFunc_and_proc_declarations(self, ctx:pascalParser.Func_and_proc_declarationsContext):
        pass


    # Enter a parse tree produced by pascalParser#func_declaration.
    def enterFunc_declaration(self, ctx:pascalParser.Func_declarationContext):
        pass

    # Exit a parse tree produced by pascalParser#func_declaration.
    def exitFunc_declaration(self, ctx:pascalParser.Func_declarationContext):
        pass


    # Enter a parse tree produced by pascalParser#func_arguments.
    def enterFunc_arguments(self, ctx:pascalParser.Func_argumentsContext):
        pass

    # Exit a parse tree produced by pascalParser#func_arguments.
    def exitFunc_arguments(self, ctx:pascalParser.Func_argumentsContext):
        pass


    # Enter a parse tree produced by pascalParser#func_argument_grp.
    def enterFunc_argument_grp(self, ctx:pascalParser.Func_argument_grpContext):
        pass

    # Exit a parse tree produced by pascalParser#func_argument_grp.
    def exitFunc_argument_grp(self, ctx:pascalParser.Func_argument_grpContext):
        pass


    # Enter a parse tree produced by pascalParser#proc_declaration.
    def enterProc_declaration(self, ctx:pascalParser.Proc_declarationContext):
        pass

    # Exit a parse tree produced by pascalParser#proc_declaration.
    def exitProc_declaration(self, ctx:pascalParser.Proc_declarationContext):
        pass


    # Enter a parse tree produced by pascalParser#block.
    def enterBlock(self, ctx:pascalParser.BlockContext):
        pass

    # Exit a parse tree produced by pascalParser#block.
    def exitBlock(self, ctx:pascalParser.BlockContext):
        pass


    # Enter a parse tree produced by pascalParser#code_block.
    def enterCode_block(self, ctx:pascalParser.Code_blockContext):
        pass

    # Exit a parse tree produced by pascalParser#code_block.
    def exitCode_block(self, ctx:pascalParser.Code_blockContext):
        pass


    # Enter a parse tree produced by pascalParser#statement_list.
    def enterStatement_list(self, ctx:pascalParser.Statement_listContext):
        pass

    # Exit a parse tree produced by pascalParser#statement_list.
    def exitStatement_list(self, ctx:pascalParser.Statement_listContext):
        pass


    # Enter a parse tree produced by pascalParser#statement.
    def enterStatement(self, ctx:pascalParser.StatementContext):
        pass

    # Exit a parse tree produced by pascalParser#statement.
    def exitStatement(self, ctx:pascalParser.StatementContext):
        pass


    # Enter a parse tree produced by pascalParser#case_statement.
    def enterCase_statement(self, ctx:pascalParser.Case_statementContext):
        pass

    # Exit a parse tree produced by pascalParser#case_statement.
    def exitCase_statement(self, ctx:pascalParser.Case_statementContext):
        pass


    # Enter a parse tree produced by pascalParser#case_branch.
    def enterCase_branch(self, ctx:pascalParser.Case_branchContext):
        pass

    # Exit a parse tree produced by pascalParser#case_branch.
    def exitCase_branch(self, ctx:pascalParser.Case_branchContext):
        pass


    # Enter a parse tree produced by pascalParser#case_label.
    def enterCase_label(self, ctx:pascalParser.Case_labelContext):
        pass

    # Exit a parse tree produced by pascalParser#case_label.
    def exitCase_label(self, ctx:pascalParser.Case_labelContext):
        pass


    # Enter a parse tree produced by pascalParser#for_loop.
    def enterFor_loop(self, ctx:pascalParser.For_loopContext):
        pass

    # Exit a parse tree produced by pascalParser#for_loop.
    def exitFor_loop(self, ctx:pascalParser.For_loopContext):
        pass


    # Enter a parse tree produced by pascalParser#repeat_loop.
    def enterRepeat_loop(self, ctx:pascalParser.Repeat_loopContext):
        pass

    # Exit a parse tree produced by pascalParser#repeat_loop.
    def exitRepeat_loop(self, ctx:pascalParser.Repeat_loopContext):
        pass


    # Enter a parse tree produced by pascalParser#if_block.
    def enterIf_block(self, ctx:pascalParser.If_blockContext):
        pass

    # Exit a parse tree produced by pascalParser#if_block.
    def exitIf_block(self, ctx:pascalParser.If_blockContext):
        pass


    # Enter a parse tree produced by pascalParser#while_loop.
    def enterWhile_loop(self, ctx:pascalParser.While_loopContext):
        pass

    # Exit a parse tree produced by pascalParser#while_loop.
    def exitWhile_loop(self, ctx:pascalParser.While_loopContext):
        pass


    # Enter a parse tree produced by pascalParser#function_call.
    def enterFunction_call(self, ctx:pascalParser.Function_callContext):
        pass

    # Exit a parse tree produced by pascalParser#function_call.
    def exitFunction_call(self, ctx:pascalParser.Function_callContext):
        pass


    # Enter a parse tree produced by pascalParser#arg_list.
    def enterArg_list(self, ctx:pascalParser.Arg_listContext):
        pass

    # Exit a parse tree produced by pascalParser#arg_list.
    def exitArg_list(self, ctx:pascalParser.Arg_listContext):
        pass


    # Enter a parse tree produced by pascalParser#logic_expression.
    def enterLogic_expression(self, ctx:pascalParser.Logic_expressionContext):
        pass

    # Exit a parse tree produced by pascalParser#logic_expression.
    def exitLogic_expression(self, ctx:pascalParser.Logic_expressionContext):
        pass


    # Enter a parse tree produced by pascalParser#orExpr.
    def enterOrExpr(self, ctx:pascalParser.OrExprContext):
        pass

    # Exit a parse tree produced by pascalParser#orExpr.
    def exitOrExpr(self, ctx:pascalParser.OrExprContext):
        pass


    # Enter a parse tree produced by pascalParser#andExpr.
    def enterAndExpr(self, ctx:pascalParser.AndExprContext):
        pass

    # Exit a parse tree produced by pascalParser#andExpr.
    def exitAndExpr(self, ctx:pascalParser.AndExprContext):
        pass


    # Enter a parse tree produced by pascalParser#relation.
    def enterRelation(self, ctx:pascalParser.RelationContext):
        pass

    # Exit a parse tree produced by pascalParser#relation.
    def exitRelation(self, ctx:pascalParser.RelationContext):
        pass


    # Enter a parse tree produced by pascalParser#expression.
    def enterExpression(self, ctx:pascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pascalParser#expression.
    def exitExpression(self, ctx:pascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pascalParser#term.
    def enterTerm(self, ctx:pascalParser.TermContext):
        pass

    # Exit a parse tree produced by pascalParser#term.
    def exitTerm(self, ctx:pascalParser.TermContext):
        pass


    # Enter a parse tree produced by pascalParser#factor.
    def enterFactor(self, ctx:pascalParser.FactorContext):
        pass

    # Exit a parse tree produced by pascalParser#factor.
    def exitFactor(self, ctx:pascalParser.FactorContext):
        pass


    # Enter a parse tree produced by pascalParser#assignment.
    def enterAssignment(self, ctx:pascalParser.AssignmentContext):
        pass

    # Exit a parse tree produced by pascalParser#assignment.
    def exitAssignment(self, ctx:pascalParser.AssignmentContext):
        pass


    # Enter a parse tree produced by pascalParser#literal.
    def enterLiteral(self, ctx:pascalParser.LiteralContext):
        pass

    # Exit a parse tree produced by pascalParser#literal.
    def exitLiteral(self, ctx:pascalParser.LiteralContext):
        pass


    # Enter a parse tree produced by pascalParser#array_literal.
    def enterArray_literal(self, ctx:pascalParser.Array_literalContext):
        pass

    # Exit a parse tree produced by pascalParser#array_literal.
    def exitArray_literal(self, ctx:pascalParser.Array_literalContext):
        pass


    # Enter a parse tree produced by pascalParser#array_index_type.
    def enterArray_index_type(self, ctx:pascalParser.Array_index_typeContext):
        pass

    # Exit a parse tree produced by pascalParser#array_index_type.
    def exitArray_index_type(self, ctx:pascalParser.Array_index_typeContext):
        pass



del pascalParser