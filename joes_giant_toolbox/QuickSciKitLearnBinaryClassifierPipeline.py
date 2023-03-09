from typing import List

import pandas as pd
import numpy as np
import sklearn
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.pipeline


class QuickSciKitLearnBinaryClassifierPipeline:
    """high level explanation TODO

    Example Usage
    -------------
    >>> import pandas as pd
    >>> download_data_df = pd.read_csv(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
            header = None,
            names = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","annual_salary"],
        )
    >>> sk_classifier = QuickSciKitLearnBinaryClassifierPipeline(
            data_df = download_data_df,
            verbose = True
        )
    >>> sk_classifier.set_variable_roles_in_model(
            y_varname="annual_salary",
            x_numeric_varnames=[
                "age",
                "fnlwgt",
                "education-num",
                "capital-gain",
                "capital-loss",
                "hours-per-week",
            ],
            x_categorical_varnames=[
                "workclass",
                "education",
                "marital-status",
                "occupation",
                "relationship",
                "race",
                "sex",
                "native-country",
            ],
        )
    >>> sk_classifier.generate_train_test_split( test_percent=0.2 )
    """

    def __init__(self, data_df: pd.DataFrame, verbose: bool) -> None:
        self.global_params = {
            "verbose": verbose,
        }
        self.data = {
            "data_df": data_df,
            "y": None,
            "x_df": None,
            "y_train": None,
            "y_test": None,
            "x_train": None,
            "x_test": None,
        }
        self.user_inputs = {
            "x_numeric_varnames": None,
            "x_categorical_varnames": None,
        }
        self.full_model_script = """
# import packages #
import pandas as pd
import sklearn
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.pipeline
        """
        self.full_model_script += """
# import data #
data_df = pd.read_csv(...)
        """
        if self.global_params["verbose"]:
            print(self.full_model_script)

    def set_variable_roles_in_model(
        self,
        y_varname: str,
        x_numeric_varnames: List[str],
        x_categorical_varnames: List[str],
    ) -> None:
        """docstring TODO"""
        self.data["y"] = self.data["data_df"][y_varname]
        self.user_inputs["x_numeric_varnames"] = x_numeric_varnames
        self.user_inputs["x_categorical_varnames"] = x_categorical_varnames
        self.data["x_df"] = self.data["data_df"][
            x_numeric_varnames + x_categorical_varnames
        ]
        code_str = f"""
# define variable roles in model #
y = data_df["{y_varname}"]
x_numeric_varnames = [{",".join([f'"{x}"'for x in self.user_inputs["x_numeric_varnames"]])}]
x_categorical_varnames = [{",".join([f'"{x}"'for x in self.user_inputs["x_categorical_varnames"]])}]
x_df = data_df[x_numeric_varnames + x_categorical_varnames]
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

    def generate_train_test_split(self, test_percent: float) -> None:
        """explanation here"""
        train_percent = 1.0 - test_percent
        (
            self.data["x_train"],
            self.data["x_test"],
            self.data["y_train"],
            self.data["y_test"],
        ) = sklearn.model_selection.train_test_split(
            self.data["x_df"], self.data["y"], test_size=test_percent
        )
        code_str = f"""
# train/test split #
train_percent = {train_percent}
test_percent = {test_percent}
x_train, x_test, y_train, y_test = train_test_split(
        x_df, y, test_size=test_percent
)
        """
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

    def transform_x_features(self, rare_category_min_freq: int) -> None:
        """TODO docstring here"""
        one_hot_var_transformer = sklearn.pipeline.Pipeline(
            steps=[
                (
                    "one_hot_encoder",
                    sklearn.preprocessing.OneHotEncoder(
                        sparse=False,  # return output as sparse array
                        handle_unknown="ignore",  # ignore levels unseen in training data
                        min_frequency=rare_category_min_freq,  # categories with fewer samples will be labelled "infrequent_sklearn"
                        dtype=np.int8,  # Data type of output columns
                    ),
                ),
            ]
        )
