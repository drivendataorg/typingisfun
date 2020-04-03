# Typing is fun

## Static type checking

Can catch bugs before it's too late (mypy).


## Makes code a lot more readable

Treat other coders (including yourself) as you'd like other coders to treat you.


## Demo

 1. Some regular old code. `v1.py`
 1. `flake8` and `black` look fine.
 1. Run `01-scripts-are-fun.py`. Terrible outcome.
 1. Type our code. `v2.py`
 1. Run `mypy` to catch the bug before it's too late.
 1. Fix bug, and type all over. `v3.py`
 1. Run `mypy` again to experience the relief of a clean code bill of health.


## Fancier types with `typing` package

- Typed collections: `typing.List` and `typing.Dict`
- Multiple types: `typing.Union`
- Optional args: `typing.Optional`



# Typing is just the beginning

Other libraries build on the strong foundation of typing everything to make certain hard things easier.


## pydantic

[pydantic](https://pydantic-docs.helpmanual.io/)


## fastapi

[FastAPI](https://fastapi.tiangolo.com/)


## typer

[Typer](https://typer.tiangolo.com/)
