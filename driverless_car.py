# Decorators
from functools import wraps
def logger(orig_func):
    """ This decorator will log which arguments orig_function was called with,
    out to a file called orig_function.log """
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), 
                                                 level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def timer(orig_function):
    """ This decorator will calculate and print how long orig_function took
    to run """
    import time

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} seconds".format(orig_function.__name__, t2))
        return result

    return wrapper

def main():
    pass

if __name__ == "__main__":
    main()
