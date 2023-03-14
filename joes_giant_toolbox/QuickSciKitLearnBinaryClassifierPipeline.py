from typing import List
import time

import pandas as pd
import numpy as np
import sklearn
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.naive_bayes
import sklearn.tree
import sklearn.linear_model
import sklearn.neural_network
import sklearn.discriminant_analysis
import sklearn.ensemble
import sklearn.gaussian_process
import sklearn.metrics
import sklearn.calibration
from matplotlib import pyplot as plt


class QuickSciKitLearnBinaryClassifierPipeline:
    """This class facilitates the rapid generation of binary classifier models using scikit-learn

    Example Usage
    -------------
    >>> data_df = pd.read_csv(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
            header = None,
            names = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","annual_salary"],
        )
    >>> data_df["annual_salary_over_50k"] = (data_df["annual_salary"]==" >50K").astype(int)
    >>> sk_classifier = QuickSciKitLearnBinaryClassifierPipeline(
            data_df = data_df,
            verbose = True
        )
    >>> sk_classifier.set_variable_roles_in_model(
            y_varname="annual_salary_over_50k",
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
    >>> sk_classifier.transform_x_features(rare_category_min_freq=500)
    >>> sk_classifier.define_models()
    >>> sk_classifier.fit_cross_valid_models(
            k_folds=10,
            models_list = [
                "adaboost",
                "decision_tree",
                "gaussian_naive_bayes",
                "gaussian_process",
                "logistic_regression",
                "neural_net",
                "quadratic_discriminant_analysis",
                "random_forest"
            ]
        )
    >>> sk_classifier.compare_models()
    """

    def __init__(self, data_df: pd.DataFrame, verbose: bool, eval_code: bool) -> None:
        self.global_params = {
            "verbose": verbose,
            "eval_code": eval_code,
        }
        self.data = {
            "data_df": data_df,
            "y": None,
            "x_df": None,
            "y_train_for_model": None,
            "y_test_for_model": None,
            "x_train": None,
            "x_test": None,
            "x_train_categorical_1hot": None,
            "x_test_categorical_1hot": None,
            "x_train_numeric": None,
            "x_test_numeric": None,
            "x_train_for_model": None,
            "x_test_for_model": None,
        }
        self.user_inputs = {
            "x_numeric_varnames": None,
            "x_categorical_varnames": None,
        }
        self.sklearn_components = {
            "feature_engineering": {"one_hot_transformer": None},
            "models": {},
            "k_folds": None,
            "k_fold_cv_results": {},
            "test_set_predictions": {},
        }
        self.full_model_script = """
# import packages #
import pandas as pd
import sklearn
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.naive_bayes
import sklearn.tree
import sklearn.linear_model
import sklearn.neural_network
import sklearn.discriminant_analysis
import sklearn.ensemble
import sklearn.gaussian_process
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
            self.data["y_train_for_model"],
            self.data["y_test_for_model"],
        ) = sklearn.model_selection.train_test_split(
            self.data["x_df"], self.data["y"], test_size=test_percent
        )
        code_str = f"""
# train/test split #
train_percent = {train_percent}
test_percent = {test_percent}
x_train, x_test, y_train_for_model, y_test_for_model = train_test_split(
        x_df, y, test_size=test_percent
)
        """
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

    def transform_x_features(self, rare_category_min_freq: int) -> None:
        """TODO docstring here"""
        one_hot_var_transformer = sklearn.preprocessing.OneHotEncoder(
            sparse_output=False,  # return output as sparse array
            handle_unknown="ignore",  # ignore levels unseen in training data
            min_frequency=rare_category_min_freq,  # categories with fewer samples will be labelled "infrequent_sklearn"
            dtype=np.int8,  # Data type of output columns
        )

        numeric_scaler_transformer = sklearn.preprocessing.StandardScaler()

        self.sklearn_components["feature_engineering"][
            "one_hot_transformer"
        ] = one_hot_var_transformer

        one_hot_var_transformer.fit(
            self.data["x_train"][self.user_inputs["x_categorical_varnames"]]
        )
        numeric_scaler_transformer.fit(
            self.data["x_train"][self.user_inputs["x_numeric_varnames"]]
        )

        self.data["x_train_categorical_1hot"] = pd.DataFrame(
            one_hot_var_transformer.transform(
                self.data["x_train"][self.user_inputs["x_categorical_varnames"]]
            ),
            columns=one_hot_var_transformer.get_feature_names_out(),
        )
        self.data["x_test_categorical_1hot"] = pd.DataFrame(
            one_hot_var_transformer.transform(
                self.data["x_test"][self.user_inputs["x_categorical_varnames"]]
            ),
            columns=one_hot_var_transformer.get_feature_names_out(),
        )

        self.data["x_train_numeric"] = pd.DataFrame(
            numeric_scaler_transformer.transform(
                self.data["x_train"][self.user_inputs["x_numeric_varnames"]]
            ),
            columns=numeric_scaler_transformer.get_feature_names_out(),
        )
        self.data["x_test_numeric"] = pd.DataFrame(
            numeric_scaler_transformer.transform(
                self.data["x_test"][self.user_inputs["x_numeric_varnames"]]
            ),
            columns=numeric_scaler_transformer.get_feature_names_out(),
        )

        self.data["x_train_for_model"] = pd.concat(
            [
                self.data["x_train_categorical_1hot"],
                self.data["x_train_numeric"],
            ],
            axis=1,
        )
        self.data["x_test_for_model"] = pd.concat(
            [
                self.data["x_test_categorical_1hot"],
                self.data["x_test_numeric"],
            ],
            axis=1,
        )

        code_str = f"""
# feature preprocessing #
one_hot_var_transformer = sklearn.preprocessing.OneHotEncoder(
    sparse_output=False,  # return output as sparse array
    handle_unknown="ignore",  # ignore levels unseen in training data
    min_frequency={rare_category_min_freq},  # categories with fewer samples will be labelled "infrequent_sklearn"
    dtype=np.int8,  # Data type of output columns
)

numeric_scaler_transformer = sklearn.preprocessing.StandardScaler()

one_hot_var_transformer.fit( x_train["x_categorical_varnames"] )
numeric_scaler_transformer.fit( x_train["x_numeric_varnames"] )

x_train_categorical_1hot = pd.DataFrame(
    one_hot_var_transformer.transform( x_train["x_categorical_varnames"] ),
    columns = one_hot_var_transformer.get_feature_names_out(),
)
x_test_categorical_1hot = pd.DataFrame(
    one_hot_var_transformer.transform( x_test["x_categorical_varnames"] ),
    columns = one_hot_var_transformer.get_feature_names_out(),
)

x_train_numeric = pd.DataFrame(
    numeric_scaler_transformer.transform( x_train["x_numeric_varnames"] ),
    columns = numeric_scaler_transformer.get_feature_names_out(),
)
x_test_numeric = pd.DataFrame(
    numeric_scaler_transformer.transform( x_test["x_numeric_varnames"] ),
    columns = numeric_scaler_transformer.get_feature_names_out(),
)

x_train_for_model = pd.concat( [x_train_categorical_1hot, x_train_numeric], axis=1 )
x_test_for_model = pd.concat( [x_test_categorical_1hot, x_test_numeric], axis=1 )
"""

        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

    def define_models(self, models_dict: dict) -> None:
        """TODO: function documentation here"""
        self.sklearn_components["models"] = models_dict
        code_str = f"""
# define models #
models_to_fit_dict = {{
    "gaussian_naive_bayes": sklearn.naive_bayes.GaussianNB(),
    "decision_tree": sklearn.tree.DecisionTreeClassifier(),
    "logistic_regression": sklearn.linear_model.LogisticRegression(
        penalty=None,
        max_iter=1_000,
    ),
    "neural_net": sklearn.neural_network.MLPClassifier(),
    "quadratic_discriminant_analysis": sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis(),
    "random_forest": sklearn.ensemble.RandomForestClassifier(),
    "adaboost": sklearn.ensemble.AdaBoostClassifier(),
    "gaussian_process": sklearn.gaussian_process.GaussianProcessClassifier(),
}}
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

    def fit_cross_valid_models(self, model_names_list: List[str], k_folds: int) -> None:
        """TODO: function documentation here"""
        self.sklearn_components["k_folds"] = k_folds
        model_fit_counter = 1
        for model_name in model_names_list:
            start_time = time.perf_counter()
            print(
                f"fitting model {model_fit_counter} of {len(model_names_list)} [{model_name}] ({k_folds} folds)..",
                end="",
            )
            self.sklearn_components["k_fold_cv_results"][
                model_name
            ] = sklearn.model_selection.cross_validate(
                estimator=self.sklearn_components["models"][model_name],
                X=self.data["x_train_for_model"],
                y=self.data["y_train_for_model"],
                scoring="roc_auc",
                cv=k_folds,
                return_train_score=True,
                return_estimator=False,
            )
            minutes_elapsed = (time.perf_counter() - start_time) / 60
            print(f"..done ({minutes_elapsed:.2f} minutes)")
            model_fit_counter += 1

    def compare_models_cross_valid_roc_auc(self) -> None:
        """TODO: function documentation here"""
        x_axis_values = []
        y_axis_values = []
        model_counter = 0
        model_names = list(self.sklearn_components["k_fold_cv_results"].keys())
        for model_name in model_names:
            test_score_each_fold = self.sklearn_components["k_fold_cv_results"][
                model_name
            ]["test_score"].tolist()
            x_axis_values += [model_counter] * len(test_score_each_fold)
            y_axis_values += test_score_each_fold
            model_counter += 1
        plt.figure(figsize=(10, 5))
        plt.scatter(x_axis_values, y_axis_values, alpha=0.5)
        plt.xticks(ticks=range(len(model_names)), labels=model_names, rotation=45)
        plt.xlabel("Model Name")
        plt.ylabel("ROC AUC")
        plt.title(
            f"Model Performance (ROC AUC) on Each Test Fold Using {self.sklearn_components['k_folds']}-Fold Cross Validation"
        )
        plt.show()

    def add_ensemble_model(
        self,
        ensemble_name: str,
        model_names_list: List[str],
        weight_models_by_mean_test_fold_performance: bool,
    ) -> None:
        """TODO: function documentation here"""
        if weight_models_by_mean_test_fold_performance:
            mean_cv_performance_test_fold = [
                self.sklearn_components["k_fold_cv_results"][model_name][
                    "test_score"
                ].mean()
                for model_name in model_names_list
            ]

        self.sklearn_components["models"][
            ensemble_name
        ] = sklearn.ensemble.VotingClassifier(
            estimators=[
                (model_name, self.sklearn_components["models"][model_name])
                for model_name in model_names_list
            ],
            voting="soft",
            weights=[
                x / sum(mean_cv_performance_test_fold)
                for x in mean_cv_performance_test_fold
            ],
        )
        print(f"fitting models in ensemble '{ensemble_name}'..", end="")
        start_time = time.perf_counter()
        self.sklearn_components["models"][ensemble_name].fit(
            X=self.data["x_train_for_model"],
            y=self.data["y_train_for_model"],
        )
        minutes_elapsed = (time.perf_counter() - start_time) / 60
        print(f"..done ({minutes_elapsed:.2f} minutes)")

    def fit_models(self, model_names_list: List[str]) -> None:
        """TODO: function documentation here"""
        for model_name in model_names_list:
            print(f"fitting model '{model_name}'..", end="")
            start_time = time.perf_counter()
            self.sklearn_components["models"][model_name].fit(
                X=self.data["x_train_for_model"], y=self.data["y_train_for_model"]
            )
            minutes_elapsed = (time.perf_counter() - start_time) / 60
            print(f"..done ({minutes_elapsed:.2f} minutes)")

    def generate_test_set_predictions(self, model_names_list: List[str]) -> None:
        """TODO: function documentation here"""
        for model_name in model_names_list:
            self.sklearn_components["test_set_predictions"][
                model_name
            ] = self.sklearn_components["models"][model_name].predict_proba(
                X=self.data["x_test_for_model"]
            )[
                :, 1
            ]

    def compare_models_test_set_roc_curves(self, model_names_list: List[str]) -> None:
        """TODO: function documentation here"""
        roc_curve_data = {}
        roc_auc_scores = {}
        for model_name in model_names_list:
            model_pred_y = self.sklearn_components["test_set_predictions"][model_name]
            fpr, tpr, thresholds = sklearn.metrics.roc_curve(
                y_true=self.data["y_test_for_model"],
                y_score=model_pred_y,
            )
            roc_curve_data[model_name] = {
                "fpr": fpr,
                "tpr": tpr,
                "thresholds": thresholds,
            }
            roc_auc_scores[model_name] = sklearn.metrics.roc_auc_score(
                y_true=self.data["y_test_for_model"], y_score=model_pred_y
            )
        roc_auc_scores = dict(
            sorted(roc_auc_scores.items(), key=lambda item: item[1], reverse=True)
        )

        print("--ROC AUC Scores (test data)--")
        for model_name in roc_auc_scores:
            print(f"\t{model_name}: {roc_auc_scores[model_name]:.2f}")

        plt.figure(figsize=(10, 7))
        for model_name in roc_curve_data:
            plt.plot(
                roc_curve_data[model_name]["fpr"],
                roc_curve_data[model_name]["tpr"],
                label=model_name,
            )
        plt.axline([0, 0], [1, 1])
        plt.legend()
        plt.title("ROC AUC Curves")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.show()

    def compare_models_calibration_test_set(
        self, model_names_list: List[str], n_bins
    ) -> None:
        """TODO: function documentation here"""
        calibration_curve_data = {}
        for model_name in model_names_list:
            calib_p_true, calib_p_pred = sklearn.calibration.calibration_curve(
                y_true=self.data["y_test_for_model"],
                y_prob=self.sklearn_components["test_set_predictions"][model_name],
                n_bins=n_bins,
            )
            calibration_curve_data[model_name] = {
                "p_true": calib_p_true,
                "p_pred": calib_p_pred,
            }

        plt.figure(figsize=(10, 7))
        for model_name in calibration_curve_data:
            plt.plot(
                calibration_curve_data[model_name]["p_pred"],
                calibration_curve_data[model_name]["p_true"],
                label=model_name,
            )
        plt.axline([0, 0], [1, 1], color="black", linestyle="dotted")
        plt.legend()
        plt.title("Calibration Curves")
        plt.xlabel("Predicted Proportion")
        plt.ylabel("Observed Proportion")
        plt.show()


if __name__ == "__main__":
    data_df = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
        header=None,
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
            "annual_salary",
        ],
    ).sample(10_000)
    data_df["annual_salary_over_50k"] = (data_df["annual_salary"] == " >50K").astype(
        int
    )
    sk_classifier = QuickSciKitLearnBinaryClassifierPipeline(
        data_df=data_df, verbose=True, eval_code=True
    )
    sk_classifier.set_variable_roles_in_model(
        y_varname="annual_salary_over_50k",
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
    sk_classifier.generate_train_test_split(test_percent=0.2)
    sk_classifier.transform_x_features(rare_category_min_freq=500)
    sk_classifier.define_models(
        {
            "adaboost": sklearn.ensemble.AdaBoostClassifier(),
            "decision_tree": sklearn.tree.DecisionTreeClassifier(),
            "extremely_random_trees": sklearn.ensemble.ExtraTreesClassifier(),
            "gaussian_naive_bayes": sklearn.naive_bayes.GaussianNB(),
            "gaussian_process": sklearn.gaussian_process.GaussianProcessClassifier(),
            "hist_gbm": sklearn.ensemble.HistGradientBoostingClassifier(),
            "logistic_regression": sklearn.linear_model.LogisticRegression(
                penalty=None,
                max_iter=1_000,
            ),
            "neural_net": sklearn.neural_network.MLPClassifier(),
            "quadratic_discriminant_analysis": sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis(),
            "random_forest": sklearn.ensemble.RandomForestClassifier(),
        }
    )
    sk_classifier.fit_cross_valid_models(
        k_folds=10,
        model_names_list=[
            "adaboost",
            "decision_tree",
            "extremely_random_trees",
            "gaussian_naive_bayes",
            # "gaussian_process",
            "hist_gbm",
            "logistic_regression",
            # "neural_net",
            "quadratic_discriminant_analysis",
            "random_forest",
        ],
    )
    sk_classifier.compare_models_cross_valid_roc_auc()
    sk_classifier.add_ensemble_model(
        ensemble_name="all_models_ensemble",
        model_names_list=[
            "adaboost",
            "decision_tree",
            "extremely_random_trees",
            "gaussian_naive_bayes",
            # "gaussian_process",
            "hist_gbm",
            "logistic_regression",
            # "neural_net",
            "quadratic_discriminant_analysis",
            "random_forest",
        ],
        weight_models_by_mean_test_fold_performance=True,
    )
    sk_classifier.add_ensemble_model(
        ensemble_name="best_models_ensemble",
        model_names_list=[
            "adaboost",
            "extremely_random_trees",
            "hist_gbm",
            "logistic_regression",
            "random_forest",
        ],
        weight_models_by_mean_test_fold_performance=True,
    )
    sk_classifier.fit_cross_valid_models(
        k_folds=10,
        model_names_list=["all_models_ensemble", "best_models_ensemble"],
    )
    sk_classifier.compare_models_cross_valid_roc_auc()
    final_chosen_model_names_list = [
        "adaboost",
        "hist_gbm",
        "logistic_regression",
        "random_forest",
        "all_models_ensemble",
        "best_models_ensemble",
    ]
    sk_classifier.fit_models(model_names_list=final_chosen_model_names_list)
    sk_classifier.generate_test_set_predictions(
        model_names_list=final_chosen_model_names_list
    )
    sk_classifier.compare_models_test_set_roc_curves(
        model_names_list=final_chosen_model_names_list
    )
    sk_classifier.compare_models_calibration_test_set(
        model_names_list=final_chosen_model_names_list, n_bins=10
    )
