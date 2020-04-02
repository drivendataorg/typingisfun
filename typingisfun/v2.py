def lets_add_these(x: int, y: int, z: int = 1):
    return x + y + z


def lets_add_those(x: str, y: str, z: str = "cool"):
    return x.upper() + y.upper() + z.upper()


def now_were_really_adding(x: int, y: int, z: int = 1):
    a = lets_add_these(x, y, z)
    b = lets_add_those(x, y, z)  # still a bug! but since we're typing, we catch it

    return a, b
