def lets_add_these(x, y, z=1):
    return x + y + z


def lets_add_those(x: str, y: str, z: str = "cool"):
    return x + " " + y + " " + z


def now_were_really_adding(x, y, z=1):
    a = lets_add_these(x, y, z)
    b = lets_add_those(x, y, z)  # this is a bug!

    return a, b
