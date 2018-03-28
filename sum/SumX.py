#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itertools

class my_Struct:
    id = 0
    num = 0.0

    def __init__(self):
        self.id = 0
        self.num = 0.0

    def setItem(self, vid, vnum):
        self.id = vid
        self.num = vnum

    def __str__(self):
        return ('%d,%.2f' % (self.id, self.num))

    def __eq__(self, other):
        return (self.id == other.id and self.num == other.num)


def getFile2List(fileName):
    f = open(fileName)
    ls = f.readlines()
    result = []
    for line in ls:
        # print(line)
        l_array = line.split('\t')
        if '#' in l_array[0]:
            continue
        else:
            vid = int(l_array[0])
            vnum = float(l_array[1].replace(',', ''))
            it = my_Struct()
            it.setItem(vid, vnum)
            result.append(it)
    f.close()
    return result


def duoEqual(nums):
    v = list(itertools.combinations(nums, 2))
    m = filter(lambda x: x[0] == x[1], v)
    return not m


def printList(items):
    print('[', end='')
    for it in items:
        print("[%s]"%it, end=',')
    print(']', end='\n')


def findItems2(v, items):
    for it in items:
        if (v == it.num):
            return it
        else:
            if v > it.num:
                x = v - it.num
                tmp = [g for g in items if (g != it)]
                printList(tmp)
                b = findItems2(x, tmp)
                if v == (it.num + b.num):
                    return b
    return None



print('=====================start============================')
source = getFile2List('SumX_Data.txt')
printList(source)
print(len(source))
target = getFile2List('SumX_Data2.txt')
print(len(target))
printList(target)
# print('=====================start============================')
# for item in target:
#     f = findItems2(item.num, source)
#     if f != None:
#         print(f)
print('=======================end============================')
