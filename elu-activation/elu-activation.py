import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    out = []

    for i in x:
        if i > 0:
            out.append(i)
        else:
            out.append(alpha * (math.exp(i) - 1))

    return out