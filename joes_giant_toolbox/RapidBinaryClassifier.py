from typing import List
import warnings
import time
import pprint
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


class RapidBinaryClassifier:
    """This class facilitates the rapid generation of binary classifier models using scikit-learn [https://github.com/scikit-learn/scikit-learn]"""

    def __init__(self, data_df: pd.DataFrame, verbose: bool, eval_code: bool) -> None:
        self.global_params = {
            "verbose": verbose,
            "eval_code": eval_code,
        }
        self.data = {
            "data_df": data_df.copy(),
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
        """
        self.full_model_script += """
# import data #
data_df = pd.read_csv(...)
        """
        if self.global_params["verbose"]:
            print(self.full_model_script)

    def assess_input_data_quality(self) -> None:
        """Checks the quality of the raw input data self.data["data_df"]"""
        code_str = f"""
# Quantify missing values in input data #
print("Count of missing values per column:")
print(data_df.isna().sum())
assert self.data["data_df"].isna().sum().sum() == 0, "Missing values in input data currently not supported"
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)
        if self.global_params["eval_code"]:
            print("Count of missing values per column:")
            print(self.data["data_df"].isna().sum())
            assert (
                self.data["data_df"].isna().sum().sum() == 0
            ), "Missing values in input data currently not supported (future version will include missing data imputation)"
            warnings.warn(
                "Missing value imputation is not yet implemented - input data must have no missing values",
                UserWarning,
            )

    def set_variable_roles_in_model(
        self,
        y_varname: str,
        x_numeric_varnames: List[str],
        x_categorical_varnames: List[str],
    ) -> None:
        """Specifies which variables are to be included in the model, and the role of each

        Parameters
        ----------
        y_varname: str
            The column name of the outcome variable (binary variable to be predicted)
        x_numeric_varnames: List[str]
            List of column names of continuous (real-values) variables to included as predictors in the model
        x_categorical_varnames: List[str]
            List of column names of categorical variables to be included as predictors in the model
        """
        code_str = f"""
# define variable roles in model #
y = data_df["{y_varname}"]
x_numeric_varnames = [{",".join([f'"{x}"'for x in x_numeric_varnames])}]
x_categorical_varnames = [{",".join([f'"{x}"'for x in x_categorical_varnames])}]
x_df = data_df[x_numeric_varnames + x_categorical_varnames]
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

        if self.global_params["eval_code"]:
            self.data["y"] = self.data["data_df"][y_varname]
            self.user_inputs["x_numeric_varnames"] = x_numeric_varnames
            self.user_inputs["x_categorical_varnames"] = x_categorical_varnames
            self.data["x_df"] = self.data["data_df"][
                x_numeric_varnames + x_categorical_varnames
            ]

    def generate_train_test_split(self, test_percent: float) -> None:
        """Splits data into 2 non-overlapping partitions ("training" and "test")

        Parameters
        ----------
        test_percent: float in (0.0, 1.0)
            Proportion of the input data to include in the test partition
            The training partition is then 100(1-test_percent)% of the input data
        """
        code_str = f"""
# train/test split #
train_percent = {1.0-test_percent}
test_percent = {test_percent}
x_train, x_test, y_train_for_model, y_test_for_model = train_test_split(
        x_df, y, test_size=test_percent
)
        """
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

        if self.global_params["eval_code"]:
            (
                self.data["x_train"],
                self.data["x_test"],
                self.data["y_train_for_model"],
                self.data["y_test_for_model"],
            ) = sklearn.model_selection.train_test_split(
                self.data["x_df"], self.data["y"], test_size=test_percent
            )

    def transform_x_features(self, rare_category_min_freq: int) -> None:
        """1-hot encodes categorical predictors and scales numeric predictors

        Parameters
        ----------
        rare_category_min_freq: int
            (only applies to categorical predictors)
            Categories must have at least this many samples, otherwise they are put into the category "infrequent_sklearn"
        """
        code_str = f"""
# feature preprocessing #
one_hot_var_transformer = sklearn.preprocessing.OneHotEncoder(
    sparse_output=False,  # return output as sparse array
    handle_unknown="ignore",  # ignore levels (categories) unseen in training data
    min_frequency={rare_category_min_freq},  # categories with fewer samples will be labelled "infrequent_sklearn"
    dtype=np.int8,  # Data type of output columns
)

numeric_scaler_transformer = sklearn.preprocessing.StandardScaler()

one_hot_var_transformer.fit( x_train[x_categorical_varnames] )
numeric_scaler_transformer.fit( x_train[x_numeric_varnames] )

x_train_categorical_1hot = pd.DataFrame(
    one_hot_var_transformer.transform( x_train[x_categorical_varnames] ),
    columns = one_hot_var_transformer.get_feature_names_out(),
)
x_test_categorical_1hot = pd.DataFrame(
    one_hot_var_transformer.transform( x_test[x_categorical_varnames] ),
    columns = one_hot_var_transformer.get_feature_names_out(),
)

x_train_numeric = pd.DataFrame(
    numeric_scaler_transformer.transform( x_train[x_numeric_varnames] ),
    columns = numeric_scaler_transformer.get_feature_names_out(),
)
x_test_numeric = pd.DataFrame(
    numeric_scaler_transformer.transform( x_test[x_numeric_varnames] ),
    columns = numeric_scaler_transformer.get_feature_names_out(),
)

x_train_for_model = pd.concat( [x_train_categorical_1hot, x_train_numeric], axis=1 )
x_test_for_model = pd.concat( [x_test_categorical_1hot, x_test_numeric], axis=1 )
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

        if self.global_params["eval_code"]:
            one_hot_var_transformer = sklearn.preprocessing.OneHotEncoder(
                sparse_output=False,  # return output as sparse array
                handle_unknown="ignore",  # ignore levels (categories) unseen in training data
                min_frequency=rare_category_min_freq,  # categories with fewer samples will be labelled "infrequent_sklearn"
                dtype=np.int8,  # Data type of output columns
            )

            numeric_scaler_transformer = sklearn.preprocessing.StandardScaler()

            one_hot_var_transformer.fit(
                self.data["x_train"][self.user_inputs["x_categorical_varnames"]]
            )
            numeric_scaler_transformer.fit(
                self.data["x_train"][self.user_inputs["x_numeric_varnames"]]
            )

            self.sklearn_components["feature_engineering"][
                "one_hot_transformer"
            ] = one_hot_var_transformer
            self.sklearn_components["feature_engineering"][
                "numeric_scaler_transformer"
            ] = numeric_scaler_transformer

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

    def define_models(self, models_dict: dict) -> None:
        """Initiates the sklearn binary classifier models to be fit

        Parameters
        ----------
        models_dict: dict
            A dictionary containing the sklearn models to be fit

        Example Usage
        -------------
        >>>sk_classifier = RapidBinaryClassifier(data_df=data_df, verbose=True, eval_code=True)
        >>>sk_classifier.define_models(
        ...     models_dict = {
        ...         "adaboost": sklearn.ensemble.AdaBoostClassifier(),
        ...         "logistic_regression": sklearn.linear_model.LogisticRegression(
        ...             penalty=None,
        ...             max_iter=1_000,
        ...         )
        ...     }
        ... )
        """
        code_str = f"""
# define models #
models_to_fit_dict = {pprint.pformat(models_dict)}
"""
        self.full_model_script += code_str
        if self.global_params["verbose"]:
            print(code_str)

        if self.global_params["eval_code"]:
            self.sklearn_components["models"] = models_dict

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

        roc_curve_explanation_text = """
-- Explanation of ROC Curve --
TPR = "True Positive Rate" = "Recall" = The proportion of true y=1 cases which the model has correctly labelled as y=1
FPR = "False Positive Rate" = The proportion of y=0 cases which the model incorrectly labelled as y=1
        
The ROC Curve plots the TPR and FPR achieved under a range of different "decision thresholds" (between 0.0 and 1.0)..
..where for a given "decision threshold" all samples with estimated Pr[y=1] higher than that threshold are labelled as the positive (y=1) class
        
A good resource: https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc        
        """
        print(roc_curve_explanation_text)
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

        print(
            f"""--ROC AUC Scores (test data)--
The "ROC AUC Score" is the area under the ROC Curve
It is also the probability that a random positive (y=1) case and a random negative (y=0) case are ranked correctly by the model 
        """
        )
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
        plt.title("ROC Curves")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate (Recall)")
        [plt.axhline(x / 10, alpha=0.2) for x in range(0, 10)]
        [plt.axvline(x / 10, alpha=0.2) for x in range(0, 10)]
        plt.show()

    def compare_models_calibration_test_set(
        self, model_names_list: List[str], n_bins
    ) -> None:
        """TODO: function documentation here"""
        model_calibration_explanation_text = """
-- Explanation of Model Calibration --
TODO
        """
        print(model_calibration_explanation_text)

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
        plt.title("Calibration Curves (Test Set)")
        plt.xlabel("Mean Predicted y=1 Probability")
        plt.ylabel("Observed y=1 Proportion")
        [plt.axhline(x / 10, alpha=0.2) for x in range(0, 10)]
        [plt.axvline(x / 10, alpha=0.2) for x in range(0, 10)]
        plt.show()

    def compare_models_test_set_precision_recall(
        self, model_names_list: List[str]
    ) -> None:
        """TODO: function documentation here"""
        precision_recall_explanation_text = """
-- Explanation of Precision/Recall Curve --
   "Recall" = The proportion of true y=1 cases which the model has correctly labelled as y=1
"Precision" = The proportion of predicted y=1 cases which are truly y=1 cases
        
The Precision/Recall Curve plots the Precision and Recall achieved under a range of different "decision thresholds" (between 0.0 and 1.0)..
..where for a given "decision threshold" all samples with estimated Pr[y=1] higher than that threshold are labelled as the positive (y=1) class
        """
        print(precision_recall_explanation_text)

        precision_recall_curve_data = {}
        for model_name in model_names_list:
            model_pred_y = self.sklearn_components["test_set_predictions"][model_name]
            precision, recall, thresholds = sklearn.metrics.precision_recall_curve(
                y_true=self.data["y_test_for_model"],
                probas_pred=model_pred_y,
            )
            precision_recall_curve_data[model_name] = {
                "precision": precision,
                "recall": recall,
                "thresholds": thresholds,
            }
        plt.figure(figsize=(10, 7))
        for model_name in precision_recall_curve_data:
            plt.plot(
                precision_recall_curve_data[model_name]["recall"],
                precision_recall_curve_data[model_name]["precision"],
                label=model_name,
            )
        plt.legend()
        plt.title("Precision Recall Curves")
        plt.xlabel("Recall")
        plt.ylabel("Precision")
        [plt.axhline(x / 10, alpha=0.2) for x in range(0, 10)]
        [plt.axvline(x / 10, alpha=0.2) for x in range(0, 10)]
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
    )
    data_df["annual_salary_over_50k"] = (data_df["annual_salary"] == " >50K").astype(
        int
    )
    sk_classifier = RapidBinaryClassifier(data_df=data_df, verbose=True, eval_code=True)
    sk_classifier.assess_input_data_quality()
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
    all_model_names = [
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
    ]
    sk_classifier.fit_cross_valid_models(
        k_folds=10,
        model_names_list=all_model_names,
    )
    sk_classifier.compare_models_cross_valid_roc_auc()
    sk_classifier.add_ensemble_model(
        ensemble_name="all_models_ensemble",
        model_names_list=all_model_names,
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
    sk_classifier.compare_models_test_set_precision_recall(
        model_names_list=final_chosen_model_names_list
    )