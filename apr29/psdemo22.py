def compute(a, b, c):
    print(a + b + c)


items = [22, 33, 44, 55]

compute(items[0], items[1], items[2])
compute(*items[:3])