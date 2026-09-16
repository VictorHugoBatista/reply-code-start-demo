import ast


def remove_comments(source: str) -> str:
    tree = ast.parse(source)
    scopes = (
        ast.Module,
        ast.ClassDef,
        ast.FunctionDef,
        ast.AsyncFunctionDef,
    )

    for node in ast.walk(tree):
        if not isinstance(node, scopes):
            continue

        while (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, str)
        ):
            node.body.pop(0)

        if not node.body and not isinstance(node, ast.Module):
            node.body.append(ast.Pass())

    ast.fix_missing_locations(tree)
    result = ast.unparse(tree)
    return result + "\n" if result else ""
