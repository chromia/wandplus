#!/usr/bin/env python

import inspect
import wandplus.image
import wandplus.misc
import wandplus.numpy
import wandplus.textutil


def exportsummary(f, module):
    modname = module.__name__

    def isprivate(name):
        return name.startswith('_')

    consts = []
    funcs = []
    members = inspect.getmembers(module)
    for (name, mem) in members:
        if inspect.isfunction(mem):
            if not isprivate(name):
                funcs.append(name)
        elif isinstance(mem, tuple) or isinstance(mem, dict):
            if not isprivate(name):
                consts.append(name)

    idt = '    '

    if consts:
        print('Constants', file=f)
        print('=========', file=f)
        for const in consts:
            print(idt + '* :const:`' + const +
                  ' <' + modname + '.' + const + '>`', file=f)
        print('', file=f)
    if funcs:
        print('Functions', file=f)
        print('=========', file=f)
        for func in funcs:
            print(idt + '* :meth:`' + func +
                  ' <' + modname + '.' + func + '>`', file=f)
        print('', file=f)


docpath = '../docs/summary/'
with open(docpath + 'image.txt', 'w') as f:
    exportsummary(f, wandplus.image)
with open(docpath + 'misc.txt', 'w') as f:
    exportsummary(f, wandplus.misc)
with open(docpath + 'numpy.txt', 'w') as f:
    exportsummary(f, wandplus.numpy)
with open(docpath + 'textutil.txt', 'w') as f:
    exportsummary(f, wandplus.textutil)
