# Decorators
from functools import wraps
def logger(orig_func):
    """ 
    Logs orig_func out to a file called orig_func.log
    
    Args:
        orig_func (function): The function to be logged

    Returns:
        wrapper (function): The un-executed form of orig_func

    Examples:
        @logger
        def main():
            print("Hello world!")

    Whenever main is called, a file called main.log will be created, if it
    doesn't already exist, each line in main.log will read as:
    "Ran with args: (), and kwargs: {}"

    @logger
    def sum(x, y):
        return x + y

    sum(2, 3)
    
    A file called sum.log will be created, which will read as:
    "Ran with args: (2, 3), and kwargs: {}"

    @logger
    def square(num)
        return num ** 2

    sqaure(num=5)

    A file called square.log will be created, which will read as:
    "Ran with args: (), and kwargs: {'num', 5}
    """
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), 
                                                 level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        """
        Using the wraps decorator allows for using multiple decorators on a 
        single function.
        """
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def timer(orig_func):
    """
    Calculates and prints how long orig_func took to run.

    Args:
        orig_func (function): The function to be timed

    Returns:
        wrapper (function): The un-executed form of orig_func

    Example
        @timer
        def main():
            pass

        main()

    prints "main ran in: 4.76837158203125e-07 seconds"
    """

    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t = time.time()
        result = orig_func(*args, **kwargs)
        t = time.time() - t
        print("{} ran in: {} seconds".format(orig_func.__name__, t))
        return result

    return wrapper
