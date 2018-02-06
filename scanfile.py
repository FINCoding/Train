def sacnner(name, function):
    list(map(function,open(name, 'r')))
