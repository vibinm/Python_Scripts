"""variable len arguments"""


def demo(*args):
    print(args)


# demo()
# demo(123)
# demo(1, 2, 'iii', 4, 5.5)
items = [1, 2, 3, 4, 5]
demo(items)
demo(*items)
print()
items = (1, 2, 3, 4, 5)
demo(items)
demo(*items)
