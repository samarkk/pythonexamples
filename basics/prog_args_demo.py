# we import argv from sys
# argv can handle nothing more than positinal arguments
# for any thing a little further we use the argparse package
# there are three options to choose from - argparse, getopt or optparse
# argparse is the most versatile and the default preferred option
import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)

# New keyword action  given value "store_true". This means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False 

# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)

# short arguments added
# action = count - number of times the argument is specified
# default value for the argument
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# multiple arguments
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbosity >= 2:
#     print(f"{args.x} to the power {args.y} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.x}^{args.y} == {answer}")
# else:
#     print(answer)

parser.add_argument('--input', type=int, action='store', nargs='+')
parser.add_argument('-v', action='count', default=0)
args = parser.parse_args()
from functools import reduce
if args.v > 0:
    print(f'The sum of the arguments is: {reduce(lambda x, y: x + y, args.input)}')
else:
    print(sum(args.input))


