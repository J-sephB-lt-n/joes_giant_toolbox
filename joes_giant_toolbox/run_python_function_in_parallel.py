import concurrent.futures
from typing import Callable, Iterator


def run_python_function_in_parallel(
    func: Callable, input_tuple: tuple, parallel_method: str, **kwargs
) -> Iterator:
    """Convenience function for running a python function in parallel on multiple cores or threads

    Parameters
    ----------
    func: Callable
        A function taking a single argument (x)
    input_tuple: tuple
        A tuple (immutable list) containing the list of input objects to process by the function
    parallel_method: str
        The method to use for parallelisation: one of ['multi_core', 'multi_thread']
    **kwargs
        Additional keyword arguments to pass to concurrent.futures.ProcessPoolExecutor() or concurrent.futures.ThreadPoolExecutor()
    Returns
    -------
    Iterator
        Returns the function outputs as an iterator

    Example Usage
    -------------
    >>>def sum_squares(x): return sum([num**2 for num in x])
    >>>run_test = run_python_function_in_parallel(
    ...     func = sum_squares,
    ...     input_tuple = ( [1,2], [3,4], [5,6,7] ),
    ...     parallel_method = "multi_thread",
    ...     max_workers = 10,
    ...)
    >>>list(run_test)
    [5, 25, 110]
    """
    assert parallel_method in [
        "multi_core",
        "multi_thread",
    ], "parallel_method must be one of ['multi_core', 'multi_thread']"

    if parallel_method == "multi_core":
        with concurrent.futures.ProcessPoolExecutor(**kwargs) as executor:
            result = executor.map(func, input_tuple)

    elif parallel_method == "multi_thread":
        with concurrent.futures.ThreadPoolExecutor(**kwargs) as executor:
            result = executor.map(func, input_tuple)

    else:
        raise ValueError(
            "parameter 'parallel_method' must be one of ['multi_core', 'multi_thread']"
        )

    return result
