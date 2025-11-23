"""
Utility functions.
This file has small helpers like cleaning text and safe calculator evaluation.
"""

import re
import ast
import operator

def clean_text(text: str) -> str:

    return re.sub(r"[^\w\s.+\-*/()^]", "", text).strip().lower()

def contains_math_expression(text: str) -> bool:

    return bool(re.search(r"\d\s*[\+\-\*/^]\s*\d", text))

SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _eval_node(node):
    if isinstance(node, ast.Num):
        return node.n
    
    if isinstance(node, ast.Constant):  
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers allowed.")
    
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)

        if op_type not in SAFE_OPS:
            raise ValueError("Unsupported operator.")
        return SAFE_OPS[op_type](left, right)
    
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)

        if op_type not in SAFE_OPS:
            raise ValueError("Unsupported unary operator.")
        return SAFE_OPS[op_type](operand)
    
    if isinstance(node, ast.Expr):
        return _eval_node(node.value)
    raise ValueError("Unsupported expression.")

def evaluate_expression_safely(text: str):
   
    expr_match = re.search(r"([0-9\.\s\+\-\*/\(\)\^]+)", text)
    if not expr_match:
        return "I couldn't find a valid math expression."

    expr = expr_match.group(1).replace("^", "**")

    try:
        node = ast.parse(expr, mode="eval")
        result = _eval_node(node.body)
        return result
    except Exception as e:
        return f"Invalid expression: {e}"
