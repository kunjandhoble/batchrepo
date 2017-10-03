
# name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
# action - The basic type of action to be taken when this argument is encountered at the command line.
# nargs - The number of command-line arguments that should be consumed.
# const - A constant value required by some action and nargs selections.
# default - The value produced if the argument is absent from the command line.
# type - The type to which the command-line argument should be converted.
# choices - A container of the allowable values for the argument.
# required - Whether or not the command-line option may be omitted (optionals only).
# help - A brief description of what the argument does.
# metavar - A name for the argument in usage messages.
# dest - The name of the attribute to be added to the object returned by parse_args().


import argparse,time
"""
parser = argparse.ArgumentParser(prog='nameofprog')
parser.add_argument('-optionalargsssss','--optionalarg')
parser.add_argument('necessaryargs')

print(parser.parse_args(['input']))
print(parser.parse_args(['-optional','optional','input']))
time.sleep(2)
print(parser.parse_args(['-input']))

# >>>>>>>>ACTION>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.parse_args('--foo 1'.split())
#Namespace(foo='1')

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)
parser.parse_args(['--foo'])
# Namespace(foo=42)

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
parser.parse_args('--foo --bar'.split())
# Namespace(foo=True, bar=False, baz=True)


parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
parser.parse_args('--foo 1 --foo 2'.split())
# Namespace(foo=['1', '2'])

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')
parser.parse_args(['-vvv'])
# Namespace(verbose=3)
"""
# >>>>>>>>>NARGS>>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=2)
parser.add_argument('bar', nargs=1)
# parser.parse_args('c --foo a b'.split())
# Namespace(bar=['c'], foo=['a', 'b'])
args = parser.parse_args()
print(args.bar)
print(args.foo)


parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?', default='d')
parser.parse_args(['XX', '--foo', 'YY'])
# Namespace(bar='XX', foo='YY')
parser.parse_args(['XX', '--foo'])
# Namespace(bar='XX', foo='c')
parser.parse_args([])
# Namespace(bar='d', foo='d')


parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')
parser.add_argument('--bar', nargs='*')
parser.add_argument('baz', nargs='*')
parser.parse_args('a b --foo x y --bar 1 2'.split())
# Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

# >>>>>>>>>>default>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs='?', default=42)
parser.parse_args(['a'])
# Namespace(foo='a')
parser.parse_args([])
# Namespace(foo=42)


# >>>>>>>type>>>>>>>>>
parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)
parser.add_argument('bar', type=open)
parser.parse_args('2 temp.txt'.split())
# Namespace(bar=<_io.TextIOWrapper name='temp.txt' encoding='UTF-8'>, foo=2)

import math
def perfect_square(string):
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = "%r is not a perfect square" % string
        raise argparse.ArgumentTypeError(msg)
    return value

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=perfect_square)
parser.parse_args(['9'])
# Namespace(foo=9)
parser.parse_args(['7'])
# usage: PROG [-h] foo
# PROG: error: argument foo: '7' is not a perfect square

# >>>>>>>>choices>>>>>>>>>>>>.

parser = argparse.ArgumentParser(prog='doors.py')
parser.add_argument('door', type=int, choices=range(1, 4))
print(parser.parse_args(['3']))
# Namespace(door=3)
parser.parse_args(['4'])
# usage: doors.py [-h] {1,2,3}
# doors.py: error: argument door: invalid choice: 4 (choose from 1, 2, 3)

# Any object that supports the in operator can be passed as the choices

# dest, required

# READ MORE: https://docs.python.org/dev/library/argparse.html
