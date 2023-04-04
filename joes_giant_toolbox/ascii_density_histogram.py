import math
from typing import List


def ascii_density_histogram(
    values_list: List[int | float],
    n_bins: int = 50,
    draw_character: str = "|",
    density_per_symbol: float = 0.005,
    label_round_n_places: int = 2,
) -> str:
    """
    Draws a histogram using raw text symbols

    Parameters
    ----------
    values_list: List[int | float]
        The vector of values whose distribution is to be represented by the histogram
    n_bins: int, optional (default: 50)
        The number of bins to use when building the histogram
    draw_character: str, optional (default: "|")
        The string character to use to draw the histogram bars
    density_per_symbol: float, optional (default: 0.005)
        TODO
        e.g. density_per_symbol=0.01 means that each drawn character represents 1% of the total data
    label_round_n_places: int, optional (default: 2)
        The number of places to round the axis bin labels to

    Returns
    -------
    str
        The histogram, returned as a multi-line string

    Example Usage
    -------------
    >>> import numpy as np
    >>> from matplotlib import pyplot as plt
    >>> sample_size=100_000
    >>> dbn_choices=np.random.choice(a=[1,2], size=sample_size, replace=True)
    >>> values=(
        (dbn_choices==1) * np.random.normal(size=100_000, loc=0, scale=1).tolist() +
        (dbn_choices==2) * np.random.normal(size=100_000, loc=10, scale=3).tolist()
    ).tolist()
    >>> print(
        ascii_density_histogram(
                values_list = values
            ,   n_bins = 20
            ,   draw_character = "|"
            ,   density_per_symbol = 0.005
            ,   label_round_n_places = 1
        )
    )
    >>> # compare to matplotlib histogram #
    >>> plt.hist(values, bins=20)
    """
    if label_round_n_places <= 0:
        raise ValueError("[label_round_n_places] must be a positive integer")
    # sorted_value_list = value_list.copy()  # so as not to sort the global value_list
    # sorted_value_list.sort()
    min_value = min(values_list)  # sorted_value_list[0]
    max_value = max(values_list)  # sorted_value_list[-1]
    bin_width: float = (max_value - min_value) / n_bins

    assigned_bin_idx: list = [
        math.floor((x - min_value) / bin_width)
        if x < max_value
        else (n_bins - 1)  # put max_value into top bin
        for x in values_list
    ]

    bin_ref: dict = {}
    for i in range(n_bins):
        bin_ref[i] = {
            "BIN_MIN_INCL": min_value + i * bin_width,
            "BIN_MAX_EXCL": min_value + (i + 1) * bin_width,
            "n_samples_in_bin": 0,  # count of values in this bin (to be populated)
        }

    # for idx in range(len(values_list)):
    #    value = values_list[idx]
    #    bin_idx = assigned_bin_idx[idx]
    #    bin_min_incl = bin_ref[bin_idx]["BIN_MIN_INCL"]
    #    bin_max_excl = bin_ref[bin_idx]["BIN_MAX_EXCL"]
    #    if (value < bin_min_incl) or (value >= bin_max_excl):
    #        if value != max_value:
    #            print(f"issue! idx={idx}")

    # build the histogram string:
    n_samples = len(values_list)
    bin_densities = [bin_ref[i][2] / n_values for i in range(n_bins)]
    n_symbols_per_bin = [int(i // density_per_symbol) for i in bin_densities]
    longest_label_len = max(
        len(str(int(round(sorted_value_list[0])))) + label_round_n_places + 1,
        len(str(int(round(sorted_value_list[-1])))) + label_round_n_places + 1,
    )
    closing_bracket_ref = ")" * (n_bins - 1) + "]"
    histogram_string = ""
    for j in range(len(bin_ref)):
        histogram_string += (
            "\n"
            + "["
            + str(round(bin_ref[j][0], label_round_n_places)).rjust(longest_label_len)
            + ", "
            + str(round(bin_ref[j][1], label_round_n_places)).rjust(longest_label_len)
            + closing_bracket_ref[j]
            + " "
            + draw_character * n_symbols_per_bin[j]
        )

    return histogram_string
