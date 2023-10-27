def lower_output(func):
    def wrapper():
        return func().lower()
    return wrapper


def f():
    a = input()
    return a


f = lower_output(f)
print(f())
