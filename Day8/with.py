from timeit import timeit
code1 = """
def x_fact(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")
    return 10/age


try:
    x_fact(-1)
except ValueError as err:
    pass
"""
print("first code", timeit(code1, number=10000))
