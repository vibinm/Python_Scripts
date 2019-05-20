n = 123  # global scope


def demo():
    n = 'pip'   # local scope
    print(n)
    print(globals()['n'])

# print(n)
demo()
