import concurrent.futures
from typing import Callable, Iterator
import os
import threading
import functools


def run_python_function_in_parallel(
    func: Callable,
    input_tuple: tuple,
    parallel_method: str,
    verbose: bool,
    **kwargs,
) -> Iterator:
    """Convenience function for running a python function in parallel on multiple cores or threads

    Notes
    -----
    If your function has multiple input parameters, you need to wrap these within the single input argument [x]...
    ...and then unpack [x] within the function itself.
    e.g. [x] could be a dictionary, namedtuple or list (refer to the examples below)

    Parameters
    ----------
    func: Callable
        A function taking a single argument (x)
    input_tuple: tuple
        A tuple (immutable list) containing the list of input objects to process by the function
    parallel_method: str
        The method to use for parallelisation: one of ['multi_core', 'multi_thread']
    verbose: bool
        Whether to print worker information during the run or not
    **kwargs
        Additional keyword arguments to pass to concurrent.futures.ProcessPoolExecutor() or concurrent.futures.ThreadPoolExecutor()

    Returns
    -------
    Iterator
        Returns the function outputs as an iterator

    Example Usage
    -------------
    >>> def sum_squares(x): return sum([num**2 for num in x])
    >>> run_test = run_python_function_in_parallel(
    ...     func = sum_squares,
    ...     input_tuple = ( [1,2], [3,4], [5,6,7] ),
    ...     parallel_method = "multi_thread",
    ...     verbose = True,
    ...     max_workers = 10,
    ... )
    >>> list(run_test)
    [5, 25, 110]
    >>> import time
    >>> def num_exp(x):
    ...     time.sleep(1)
    ...     return (x["value"]**x["exponent"])
    >>> run_test = run_python_function_in_parallel(
    ...     func = num_exp,
    ...     input_tuple = (
    ...         {"value": 3, "exponent":1},
    ...         {"value": 3, "exponent":2},
    ...         {"value": 3, "exponent":3},
    ...         {"value": 3, "exponent":4},
    ...         {"value": 3, "exponent":5},
    ...     ),
    ...     parallel_method = "multi_thread",
    ...     verbose = True
    ...     max_workers = 3
    ... )
    >>> list(run_test)
    [3, 9, 27, 81, 243]
    """
    if parallel_method not in [
        "multi_core",
        "multi_thread",
    ]:
        raise ValueError(
            "parallel_method must be one of ['multi_core', 'multi_thread']"
        )

    def make_verbose(func):
        """A decorator to make a function print process and thread information before and after running"""

        @functools.wraps(func)
        def verbose_func(*args, **kwargs):
            print(
                f"\nSTARTED: process_ID={os.getpid()} thread_ID={threading.get_native_id()}"
            )
            result = func(*args, **kwargs)
            print(
                f"\nCOMPLETED: process_ID={os.getpid()} thread_ID={threading.get_native_id()}"
            )
            return result

        return verbose_func

    if verbose:

        @make_verbose
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

    else:
        wrapped_func = func

    if parallel_method == "multi_core":
        with concurrent.futures.ProcessPoolExecutor(**kwargs) as executor:
            result = executor.map(wrapped_func, input_tuple)

    elif parallel_method == "multi_thread":
        with concurrent.futures.ThreadPoolExecutor(**kwargs) as executor:
            result = executor.map(wrapped_func, input_tuple)

    else:
        raise ValueError(
            "parameter 'parallel_method' must be one of ['multi_core', 'multi_thread']"
        )

    return result
