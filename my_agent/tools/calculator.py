def calculator(operation: str, a: float, b: float) -> str:
    """Perform basic arithmetic on two numbers.

    Use this tool whenever you need to compute a mathematical result.
    Do NOT attempt mental math — always delegate to this tool.

    Args:
        operation: The arithmetic operation to perform.
                   One of: "add", "subtract", "multiply", "divide".
        a: The first operand (left-hand side).
        b: The second operand (right-hand side).

    Returns:
        A string describing the result, e.g. "1457 * 38 = 55366".
    """
    ops = {
        "add":      ("+", lambda x, y: x + y),
        "subtract": ("-", lambda x, y: x - y),
        "multiply": ("*", lambda x, y: x * y),
        "divide":   ("/", lambda x, y: x / y),
    }

    if operation not in ops:
        return f"Error: unknown operation '{operation}'. Supported: {', '.join(ops)}"

    if operation == "divide" and b == 0:
        return "Error: division by zero."

    symbol, fn = ops[operation]
    result = fn(a, b)

    # Display integers cleanly (55366 instead of 55366.0)
    fmt = lambda v: str(int(v)) if isinstance(v, float) and v == int(v) else str(v)

    return f"{fmt(a)} {symbol} {fmt(b)} = {fmt(result)}"