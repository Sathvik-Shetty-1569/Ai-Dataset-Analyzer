import ast

FORBIDDEN_FUNCTIONS = {"exec", "eval", "open", "__import__"}

def validate_code(code):
    tree = ast.parse(code)

    for node in ast.walk(tree):

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise ValueError("Imports are not allowed")

        if isinstance(node, ast.Call):
            if hasattr(node.func, "id") and node.func.id in FORBIDDEN_FUNCTIONS:
                raise ValueError(f"Forbidden function used: {node.func.id}")