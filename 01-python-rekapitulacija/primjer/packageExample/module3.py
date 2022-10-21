# Relative importing example
from .module1 import function_a

def function_c() -> str:
    return "Hi from function C!"

def relative_import() -> str:
    return function_a()
