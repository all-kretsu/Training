def print_sep(sep, *args):
    print(sep , args)

print_sep('Hello', 'Max', 'Jane')

def kwargs_test(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_test(Name = 'Alex', Age = 30)