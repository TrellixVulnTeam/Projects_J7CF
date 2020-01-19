import argparse

#
#
# parser = argparse.ArgumentParser(description='This is calculates div a//b and mod a%b of two integers')
# parser.add_argument('a', help='first_integer', type=int)
# parser.add_argument('b', help='second_integer', type=int)
#
#
# args = parser.parse_args()
# a = args.a
# b = args.b
#
#
# print(f'{a}//{b} == {a//b}. {a}%{b}=={a%b}')
#

# import datetime
#
# parser = argparse.ArgumentParser(description='Returns a string containing the name and age of the person')
# parser.add_argument('-f', '--first', help='specify first name', type=str, required=False, dest='first_name')
# parser.add_argument('-l', '--last', help='last name', type=str, required=True, dest='last_name')
# parser.add_argument('-y', help='year of birth', type=int, required=False, dest='birth_name')
#
# args = parser.parse_args()
#
# first_name = args.first_name if args.first_name else ''
# last_name = args.last_name
# full_name = " ".join([last_name, first_name])
#
# current_year = datetime.datetime.now().year
# age = current_year - args.birth_name
#
# print(f'{full_name} is {age} years old')


parser = argparse.ArgumentParser(description='Prints the squares of a list of numbers, and the cubes of another one')
parser.add_argument('--sq', help='list of numbers of square', nargs='*', type=float)
parser.add_argument('--cu', help='list of numbers of cube', nargs='+', type=float, required=True)
args = parser.parse_args()

if args.sq:
    squares = [x**2 for x in args.sq]
    print(squares)

cubes = [x**3 for x in args.cu]
print(cubes)

