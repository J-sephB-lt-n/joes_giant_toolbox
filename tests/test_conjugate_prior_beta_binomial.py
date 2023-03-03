# add the root project directory to the system path:
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import the function to be tested:
from joes_giant_toolbox.conjugate_prior_beta_binomial import (
    conjugate_prior_beta_binomial,
)

# run the tests:
def test_expected_output_single_example():
    result = conjugate_prior_beta_binomial(
        prior_beta_a=1, prior_beta_b=1, n_successes=3, n_trials=3
    )
    assert (
        result["posterior_beta_a"] == 4 and result["posterior_beta_b"] == 1
    ), f"known example (prior_beta_a=1, prior_beta_b=1, n_successes=3, n_trials=3) produced incorrect output posterior_beta_a={result['posterior_beta_a']} posterior_beta_b={result['posterior_beta_b']}. Expected posterior_beta_a=4 posterior_beta_b=1"
