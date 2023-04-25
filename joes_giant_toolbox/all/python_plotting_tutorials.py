import pandas as pd
import numpy as np


class PythonPlottingTutorials:
    """Example code snippets for creating common data visualisations in python

    Example Usage
    -------------
    >>> plot_ref = PythonPlottingTutorials()
    >>> print(plot_ref.available_plots)
    >>> print(plot_ref.tutorials["heatmap"])
    """

    def __init__(self):
        self.available_plots: list = ["heatmap"]
        self.tutorials: dict = {
            "heatmap": """
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
import numpy as np
import seaborn as sns

sns.set_theme()

data_for_heatmap = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

ax = sns.heatmap(data_for_heatmap, annot=True)
ax.set_xticklabels(["a", "b", "c", "d"])
ax.set_yticklabels(["x", "y", "z"])

plt.show()

# same heatmap as above, but with data provided as pandas dataframe:
pandas_df_data_for_heatmap = pd.DataFrame(
    {"a": [1, 5, 9], "b": [2, 6, 10], "c": [3, 7, 11], "d": [4, 8, 12]},
    index=["x", "y", "z"],
)

ax = sns.heatmap(pandas_df_data_for_heatmap, annot=True)

plt.show()
            """
        }
