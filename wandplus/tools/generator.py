import csv
import sys

typedic = {'v': 'ctypes.c_void_p',
           'i': 'ctypes.c_int',
           'l': 'ctypes.c_long',
           'd': 'ctypes.c_double',
           'b': 'ctypes.c_bool',
           'S': 'ctypes.c_char_p',
           'm': 'ctypes.c_magick_char_p',
           'B': 'ctypes.c_ubyte',
           's': 'ctypes.c_size_t',
           'ss': 'ctypes.c_ssize_t',
           'pv': 'ctypes.POINTER(ctypes.c_void_p)',
           'pi': 'ctypes.POINTER(ctypes.c_int)',
           'pl': 'ctypes.POINTER(ctypes.c_long)',
           'pd': 'ctypes.POINTER(ctypes.c_double)',
           'pb': 'ctypes.POINTER(ctypes.c_bool)',
           'pS': 'ctypes.POINTER(ctypes.c_char_p)',
           'pB': 'ctypes.POINTER(ctypes.c_ubyte)',
           'ps': 'ctypes.POINTER(ctypes.c_size_t)',
           'pss': 'ctypes.POINTER(ctypes.c_ssize_t)',
           'Color': 'ctypes.c_void_p',
           'Drawing': 'ctypes.c_void_p'}


def makedefs(csvfilepath, fout):
    with open(csvfilepath, 'r') as f:
        reader = csv.reader(f)
        for linenumber, line in enumerate(reader):
            name = line[0]
            lib = line[1]
            ret = line[2]
            args = []
            line = line[3:]

            n = len(line)
            if n % 2:
                print('line({0}): argument count error.'.format(linenumber+1))
                sys.exit(-2)
            for i in range(0, n, 2):
                if line[i] != '' and line[i+1] != '':
                    args.append([line[i], line[i+1]])
                else:
                    if line[i] == '' and line[i+1] == '':
                        continue
                    else:
                        print('line({0}): empty argument found.'.format(linenumber+1))
                        sys.exit(-2)

            indent = '    '
            argtypes = lib + '.' + name + '.argtypes = [\n'
            for i, arg in enumerate(args):
                t = typedic[arg[0]]
                argtypes = argtypes + indent + t
                if i != len(args)-1:
                    argtypes = argtypes + ','
                argtypes = argtypes + '\n'
            argtypes = argtypes + ']'
            restype = lib + '.' + name + '.restype = ' + typedic[ret]
            # print(lib, name, ret, args)
            print(restype, file=fout)
            print(argtypes, file=fout)


# replacing image.py
if __name__ == '__main__':
    csvpath = './functionlist.csv'
    scriptpath = '../image.py'

    scriptlines = None
    with open(scriptpath, 'r') as f:
        scriptlines = f.readlines()

    def search(lines, keyword):
        for i, line in enumerate(lines):
            if line.startswith(keyword):
                return i
        return -1

    startline = search(scriptlines, "# %Start Definition%")
    endline = search(scriptlines, "# %End Definition%")
    if startline == -1 or endline == -1:
        raise Exception("Bad Script: Definition area is not found.")
    elif endline <= startline:
        raise Exception("Bad Script: Definition area is not correct.")

    with open(scriptpath, 'w') as f:
        for i in range(startline+1):
            f.write(scriptlines[i])
        makedefs(csvpath, f)
        for i in range(endline, len(scriptlines)):
            f.write(scriptlines[i])
