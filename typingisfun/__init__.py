def lets_add_this(x: int, y: int):
    return x + y


def lets_add_that(x: str, y: str):
    return x.upper() + y.upper()


def now_were_really_adding(x: int, y: int):
    z1 = lets_add_this(x, y)
    x_str = str(x)
    y_str = str(y)
    z2 = lets_add_that(x_str, y_str)

    return z1, z2
