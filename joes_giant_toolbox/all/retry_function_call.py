"""
Defines function retry_function_call
"""
import random
import time
from typing import Any, Callable, Iterable

from joes_giant_toolbox.custom_exceptions import MaxRetriesExceededError


def retry_function_call(  # pylint: disable=too-many-arguments
    func: Callable,
    retry_pattern_seconds: Iterable[int | float | tuple[int | float, int | float]],
    exceptions_to_handle: tuple,
    func_args: tuple | None = None,
    func_kwargs: dict | None = None,
    verbose: bool = False,
) -> Any:
    """
    Retries function (if it fails) according to retry pattern

    Args:
        func (Callable): The function to run
        func_args (tuple): (unnamed) arguments to pass to the function
        func_kwargs (dict): keyword (named) arguments to pass to the function
        retry_pattern_seconds (Iterable): Number of seconds to wait between failed function calls
                                          Each entry in this Iterable can be an integer, float or tuple
                                          Integer or float results in a deterministic wait time
                                          If tuple, then a random wait time is drawn (uniformly) from the range defined in the tuple
                                          e.g. retry_pattern_seconds=(1.5, (2,10)) will wait first 1.5 seconds and then a random
                                            number of seconds between 2 and 10
        exceptions_to_handle (tuple): Exceptions which trigger a retry (others simply raise)
        verbose (bool): Print debugging information to standard out

    Returns:
        Any: If function executes without error, returns the function result

    Raises:
        MaxRetriesExceededError: if `retry_pattern_seconds` exhausted before successful function call # pylint: disable=line-too-long

    Example:
        >>> def random_failer(fail_prob: float) -> str:
        ...     '''Function which fails randomly with probability `fail_prob`'''
        ...     if random.uniform(0, 1) < fail_prob:
        ...         raise random.choice([ValueError, MemoryError])
        ...     return "function ran successfully"
        >>> func_output = retry_function_call(
        ...        random_failer,
        ...        func_args=(0.8,),
        ...        func_kwargs={},
        ...        retry_pattern_seconds=(0.1, (1,3), 2.5, (5,7.5),
        ...        exceptions_to_handle=(ValueError,),
        ...        verbose=True
        ...    )
        >>> print("Function output:", func_output)
    """
    if func_args is None:
        func_args = tuple()
    if func_kwargs is None:
        func_kwargs = {}

    for wait_n_seconds in retry_pattern_seconds:
        try:
            return func(*func_args, **func_kwargs)
        except Exception as err:  # pylint: disable=broad-exception-caught
            if verbose:
                print(f"received error {type(err)}")
            if type(err) in exceptions_to_handle:
                if isinstance(wait_n_seconds, tuple):
                    sleep_n_seconds = random.uniform(*wait_n_seconds)
                else:
                    sleep_n_seconds = wait_n_seconds
                if verbose:
                    print(f"waiting {sleep_n_seconds:,} seconds then retrying")
                time.sleep(sleep_n_seconds)
            else:
                raise err

    raise MaxRetriesExceededError("Exhausted retry_pattern_seconds")


if __name__ == "__main__":

    def random_failer(fail_prob: float) -> str:
        """Function which fails randomly with probability `fail_prob`"""
        if random.uniform(0, 1) < fail_prob:
            raise random.choice([ValueError, MemoryError])
        return "function ran successfully"

    func_output = retry_function_call(  # pylint: disable=invalid-name
        random_failer,
        func_args=tuple(),
        func_kwargs={"fail_prob": 0.5},
        retry_pattern_seconds=(0.1, (1, 3), 2.5, (5, 7.5)),
        exceptions_to_handle=(ValueError,),
        verbose=True,
    )
    print("Function output:", func_output)
