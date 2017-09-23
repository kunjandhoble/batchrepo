# Decorators
# from functools import wraps

# 1 basic
"""
def outer_func():
    message = 'new_msg'
    def inner_func():
        print('inside inner func. Message: {}'.format(message))
    return inner_func()


outer_func()
"""
# 2 decorator basic

"""
def outer_func(msg):
    def inner_func():
        print('inside inner func. Message: {}'.format(msg))
    return inner_func


inner_func_var = outer_func('wassup')

inner_func_var()
inner_func_var()

"""
# 3 first decorator
"""
def decorator_func(original_func):
    def wrapper_func():
        print('inside inner func. Function Name: {}'.format(original_func.__name__))
        return original_func()

    return wrapper_func

def show():
    print('Show func called')

decorator_var = decorator_func(show)
decorator_var()

"""
# 4  finished creating first decorator
"""
def decorator_func(original_func):
    def wrapper_func():
        print('inside inner func. Function Name: {}'.format(original_func.__name__))
        return original_func()

    return wrapper_func
@decorator_func
def show():
    print('Show func called')


show()
"""

# 5

"""
def decorator_func(original_func):
    def wrapper_func(*args,**kwargs):
        print('inside inner func. Function Name: {}'.format(original_func.__name__))
        return original_func(*args,**kwargs)

    return wrapper_func

@decorator_func
def show():
    print('Show func called')

#with params
@decorator_func
def show_info(name,age):
    print('Info displayed of {}, Age:{}'.format(name,age))

show()
show_info('kd',24)

"""

#6
"""
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def show_info(name,age):
    print('Info displayed of {}, Age:{}'.format(name,age))

show_info('kd',24)

"""




# ?????????????????????????????????????????????????





"""
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)



class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)


# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper
"""
