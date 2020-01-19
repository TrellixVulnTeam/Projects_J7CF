import sys

print('++++++++++++++++++++++++++++++++++++++')
print('Running main_1.py - module name: {0}'.format(__name__))

from Section_9_Importing_Modules.example_1 import module1

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)


print('++++++++++++++++++++++++++++++++++++++')
