# -*-coding:utf-8-*-
__author__ = 'wb'

source = [[1, 50.3], [2, 30.2], [3, 10.6], [4, 12.5], [5, 12.5]]
target = [[1, 50.3], [2, 30.2], [3, 10.6], [4, 12.5], [5, 12.5]]


def test01():
    print(source)
    y = [x for x in source if x[1] != 50.3]
    print(y)

test01()

def findx(x, items):
    for i in items:
        if x == i[1]:
            return i
        else:
            if x > i[1]:
                # arr = filter(lambda x: x == i, items)
                arr = [k for k in items if (i[1] != x)]
                # print(arr)
                j = findx(x - i[1], arr)
                f = 0.0 + i[1] + j[1]
                if (x == f):
                    return j


def run():
    for x in source:
        print(findx(x[1], target))
