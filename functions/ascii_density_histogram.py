def ascii_density_histogram(
    value_list,  # python list containing integers or floats
    n_bins,  # number of histogram bins
    symbol="|",  # symbol to use to build the bars
    density_per_symbol=0.005,  # e.g. 0.01 means each 1% of the data will draw 1 symbol
    label_round_n_places=2,  # number of places to round the axis bin labels to
):
    """
    A function which draws a histogram using only raw text symbols

    ## EXAMPLE USAGE ##
    import numpy as np
    from matplotlib import pyplot as plt
    values = np.random.normal(size=100_000, loc=0, scale=10).tolist()
    print(
        ascii_density_histogram(
                value_list = values
            ,   n_bins = 15
            ,   symbol = "|"
            ,   density_per_symbol = 0.005
            ,   label_round_n_places = 1
        )
    )
    plt.hist(values, bins=15)       # compare to matplotlib histogram
    """
    assert label_round_n_places > 0, "label_round_n_places must be a positive integer"
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
    histogram_string = ""
    longest_label_len = max(
        len(str(int(round(sorted_value_list[0])))) + label_round_n_places + 1,
        len(str(int(round(sorted_value_list[-1])))) + label_round_n_places + 1,
    )
    closing_bracket_ref = ")" * (n_bins - 1) + "]"
    axis_labels = []
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
            + symbol * n_symbols_per_bin[j]
        )

    return histogram_string
