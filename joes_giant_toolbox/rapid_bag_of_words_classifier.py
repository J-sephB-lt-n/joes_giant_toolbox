import pandas as pd


class RapidBagOfWordsClassifier:
    """

    Example Usage
    -------------
    >>> bow_classifier = RapidBagOfWordsClassifier(data_df=data_df, verbose=True, eval_code=True)
    """

    def __init__():
        pass


if __name__ == "__main__":
    import sklearn.datasets

    X, y = sklearn.datasets.fetch_20newsgroups(
        subset="test",
        shuffle=True,
        random_state=69,
        remove=("headers", "footers", "quotes"),
        return_X_y=True,
    )
