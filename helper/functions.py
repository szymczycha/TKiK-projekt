from antlr4.tree.Tree import TerminalNode

def print_tree(node, parser, indent=0):
    prefix = "  " * indent

    if isinstance(node, TerminalNode):
        print(prefix + node.getText())
        return

    rule_name = parser.ruleNames[node.getRuleIndex()]
    print(prefix + rule_name)

    for child in node.getChildren():
        print_tree(child, parser, indent + 1)