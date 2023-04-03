from typing import List


def ascii_density_histogram(
    value_list: List[int | float],
    n_bins: int = 50,
    draw_character: str = "|",
    density_per_symbol: float = 0.005,
    label_round_n_places: int = 2,
) -> str:
    """
    Draws a histogram using raw text symbols

    Parameters
    ----------
    value_list: List[int | float]
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
                value_list = values
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
    sorted_value_list = value_list.copy()
    sorted_value_list.sort()
    min_value = sorted_value_list[0]
    max_value = sorted_value_list[-1]
    bin_width = (max_value - min_value) / n_bins
    bin_ref = []
    for i in range(n_bins):
        bin_ref += [
            [
                min_value + i * bin_width,  # left side of bin (include)
                min_value + (i + 1) * bin_width,  # right side of bin (exclude)
                0,  # count of values in this bin (to be populated)
            ]
        ]
    current_bin_idx = 0
    current_bin = bin_ref[current_bin_idx]
    i = 0
    while i < len(sorted_value_list):
        if sorted_value_list[i] < current_bin[1]:
            bin_ref[current_bin_idx][2] += 1
            i += 1
        elif current_bin_idx < (n_bins - 1):
            current_bin_idx += 1
            current_bin = bin_ref[current_bin_idx]
        else:
            bin_ref[current_bin_idx][2] += 1
            i += 1
    # build the histogram string:
    n_values = len(value_list)
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
