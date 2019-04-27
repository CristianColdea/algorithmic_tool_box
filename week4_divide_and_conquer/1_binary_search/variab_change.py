def foo(a, b = None):
    if b == None:
        b = 0

    if (a < b):
        return (a +b)
    elif (a > b):
        b = a + 1
        return foo(a, b)

a = 4
print foo(a)
