def view_nested_dict_structure(
    dict_, n_layers_deep=0, tab_width=4, value_preview_len=50
):
    """
    Provides a simple printout for understanding the structure of a complex nested python dictionary

    -- example usage --
    >> my_dict = {
        "A": {
            "1": {
                "i": [1,2,3],
                "ii": "an extremely long string here",
            },
            "2": {
                "i": {"x":0,"y":1},
                "ii": [10,11,12,13,14,15,16,17,18],
            },
        },
        "B": {
            "1": {
                "i": "joe",
                "ii": ["for","president"],
            },
            "2": {
                "i": 69,
                "ii": 420,
            },
        },
    }

    >> view_nested_dict_structure(my_dict)
    >> view_nested_dict_structure(my_dict, value_preview_len=20)
    """
    import re

    for key in dict_.keys():
        print(" " * tab_width * (n_layers_deep - 1), end="")
        if n_layers_deep > 0:
            print("-" * tab_width, end="")
        print(f"|{key}|", end="")
        if isinstance(dict_[key], dict):
            print("")
            view_nested_dict_structure(
                dict_[key],
                n_layers_deep=n_layers_deep + 1,
                tab_width=tab_width,
                value_preview_len=value_preview_len,
            )
        else:
            value_string = re.sub(r"\n", "", str(dict_[key]))
            if len(value_string) > value_preview_len:
                print(" " + value_string[:value_preview_len] + "...")
            else:
                print(" " + value_string)
