print('====== Running {0} ======'.format(__name__))


def pprint_dict(header, d):
    print('\n\n------------------------------------------')
    print('**************** {0} ********************'.format(header))

    [print(k, v) for k, v in d.items()]
    print('-----------------------------------------')


pprint_dict('module1.globals', globals())

print('====== End of {0} ======'.format(__name__))
