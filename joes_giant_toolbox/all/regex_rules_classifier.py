"""

TO SHOW:
    a word/phrase that contributes to more than 1 label

"""

import random
import re


class RegexRulesClassifier:
    """Multi-class text classifier using manual regex rules

    Example Usage
    -------------
    >>> clothing_gender_classifier = RegexRulesClassifier(verbose=True)
    >>> clothing_gender_classifier.define_rules(
    ...     {
    ...         r"\bmen": {"mens": 10}, # e.g. will not match "women"
    ...         r"(\bbikini\b)|(\bskirt)|(\bdress)": {"ladies": 10}, # must match 1 or more of these words
    ...         r"(\bchild)|(\bkid)": {"childrens": 10}, # will match "child" or "children" or "kid" or "kids" etc.
    ...         r"\bgirls?\b": {"ladies": 5, "childrens": 5},
    ...         r"\badult": {"ladies":5, "mens":5},
    ...         r"\bhawaiian\b.*\bshirt\b": {"mens":10}, # must contain both "hawaiian" and "shirt"
    ...     }
    ... )
    defined 6 rules
    >>> clothing_gender_classifier.predict("girls bikini top")
    'ladies'
    >>> clothing_gender_classifier.predict_scores("girls bikini top")
    {'ladies': 15, 'childrens': 5, 'mens': 0}
    >>> clothing_gender_classifier.predict_proba("girls bikini top")
    {'ladies': 0.75, 'childrens': 0.25, 'mens': 0.0}
    >>> clothing_gender_classifier.predict_scores("adults denim")

    >>> clothing_gender_classifier.predict("adults denim", ties_handling="first")

    >>> clothing_gender_classifier.predict("adults denim", ties_handling="all")

    >>> clothing_gender_classifier.predict("adults denim", ties_handling="random")

    >>> clothing_gender_classifier.predict("shirt", ties_handling="all")

    >>> clothing_gender_classifier.predict("hawaiian patterned shirt", ties_handling="all")
    """

    def __init__(self, verbose: bool = True):
        self._rules_dict: dict = {}
        self._unique_labels: tuple = ()
        self.verbose: bool = verbose

    def define_rules(self, manual_rules_dict: dict) -> None:
        all_labels: list = []
        for k in manual_rules_dict:
            all_labels += list(manual_rules_dict[k].keys())
        self._unique_labels: tuple = tuple(set(all_labels))
        self._rules_dict = manual_rules_dict
        if self.verbose:
            print(f"defined {len(self._rules_dict)} rules")

    def tally_label_scores(self, text_str: str) -> dict:
        scores_dict: dict = {k: 0 for k in self._unique_labels}
        for rule in self._rules_dict:
            if re.search(rule, text_str):
                for label in self._rules_dict[rule]:
                    scores_dict[label] += self._rules_dict[rule][label]
        return scores_dict

    def predict(self, text_str: str, ties_handling: str = "first") -> str:
        scores_dict: dict = self.tally_label_scores(text_str)
        if ties_handling == "first":
            return max(scores_dict, key=scores_dict.get)
        elif ties_handling == "all":
            return [
                k for k in scores_dict if scores_dict[k] == max(scores_dict.values())
            ]
        elif ties_handling == "random":
            return random.choice(
                [k for k in scores_dict if scores_dict[k] == max(scores_dict.values())]
            )
        else:
            raise ValueError("arg. 'tie_handling' must be one of ['first','all']")

    def predict_scores(self, text_str: str) -> dict:
        scores_dict: dict = self.tally_label_scores(text_str)
        return scores_dict

    def predict_proba(self, text_str: str) -> dict:
        scores_dict: dict = self.tally_label_scores(text_str)
        return {k: scores_dict[k] / sum(scores_dict.values()) for k in scores_dict}
