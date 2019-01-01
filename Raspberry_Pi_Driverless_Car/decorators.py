# Decorators
from functools import wraps
def logger(orig_func):
    ''' 
    Logs orig_func out to a file called orig_func.log
    
    Parameters
    ----------
    orig_func : function
        The function to be logged

    Returns
    ----------
    wrapper : function
        The un-executed form of orig_func
    '''
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), 
                                                 level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        '''
        Using the wraps decorator allows for using multiple decorators on a 
        single function.
        '''
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def timer(orig_func):
    '''
    Calculates and prints how long orig_func took to run.

    Parameters
    ----------
    orig_func : function
        The function to be timed

    Returns
    ---------
    wrapper : function
        The un-executed form of orig_func
    '''

    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t = time.time()
        result = orig_func(*args, **kwargs)
        t = time.time() - t
        print('{} ran in: {} seconds'.format(orig_func.__name__, t))
        return result

    return wrapper
