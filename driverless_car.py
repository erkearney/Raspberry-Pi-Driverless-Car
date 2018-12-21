# Decorators
from functools import wraps
def logger(orig_func):
    """ This decorator will log which arguments orig_func was called with out 
    to a file called orig_func.log """
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), 
                                                 level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def timer(orig_func):
    """ This decorator will calculate and print how long orig_func took
    to run """
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t = time.time()
        result = orig_func(*args, **kwargs)
        t = time.time() - t
        print("{} ran in: {} seconds".format(orig_func.__name__, t))
        return result

    return wrapper

def main():
    pass

if __name__ == "__main__":
    main()
