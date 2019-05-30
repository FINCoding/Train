# # import itertools
# import sys
#
# import imp

# [print(module) for module in sys.builtin_module_names]
# print(imp.find_module('os'))
# print('\n'.join(sys.path))
# print(itertools)
# print(__loader__.fullname)

def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

if __name__ == '__main__':
    a = cycle('abc')
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())

