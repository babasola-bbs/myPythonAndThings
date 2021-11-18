import sys

stack = []
min = sys.maxsize


def add(elem):
    global stack, min
    pair = [elem, min]
    if len(stack) == 0 or elem < min:
        min = elem
    stack.append(pair)


def get_last_element():
    if len(stack) == 0:
        print("Underflow")
        return -1
    else:
        return stack[-1][0]


def remove_last_element():
    if len(stack) == 0:
        print("Underflow")
    elif len(stack) > 1:
        min = stack[-2][1]
    else:
        min = sys.maxsize
    stack.pop()
    print("Last Object Removed")


def get_minimum():
    theMinimum = stack[-1][1]
    print(theMinimum)
    return stack[-1][1]


if __name__ == '__main__':
    add(7)
    add(64)
    add(34)
    for x in stack:
        print(x)

    get_minimum()
