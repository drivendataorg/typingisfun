def lets_add_these(x: int, y: int, z: int = 1):
    return x + y + z


def lets_add_those(x: str, y: str, z: str = "cool"):
    return x + " " + y + " " + z


def now_were_really_adding(x: int, y: int, z: int = 1):
    a = lets_add_these(x, y, z)

    e: str = str(x)
    f: str = str(y)
    g: str = str(z)
    b = lets_add_those(e, f, g)  # bug set free!

    return a, b
