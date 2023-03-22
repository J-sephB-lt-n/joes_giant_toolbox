import re
import string
import typing


class StringCleaner:
    """
    A utility for performing common string-cleaning operations. Multiple operations can be chained sequentially.

    Example Usage
    -------------
    >> string_cleaner = StringCleaner(verbose=True)
    >>

    Attributes
    ----------
    operations: dict
        A dictionary containing each individual string cleaning function
    verbose: str, optional (default: True)
        A global parameter dictating the verbosity of every string cleaning function

    Methods
    -------
    apply_sequential_operations
        Sequentially applies 1 or more string cleaning operations to a given string

    Notes
    -----
    You can get help on a specific string cleaning function using the built-in python help() function:
    >>> string_cleaner = StringCleaner()
    >>> help( string_cleaner.operations["to_lowercase"] )

    A single string cleaning operation can be accessed directly:
    >>> string_cleaner.operations["remove_punctuation"]("j!o@e#i$s%t^h&e&b*e(s)t")
    joeisthebest
        ...or called via a chain consisting of only that 1 operation:
    >>> string_cleaner.apply_sequential_operations("j!o@e#i$s%t^h&e&b*e(s)t", operation_names_list=["remove_punctuation"])
    joeisthebest

    Available String Cleaning Operations
    ------------------------------------
    extract_domain_from_url
        Extracts the base domain from a given website URL
    remove_words_or_phrases
        Removes specific 'words' or 'phrases' (i.e. specific characters in a specific order) from a given string, possibly observing word boundaries
    to_lowercase
        Converts all upper case characters in the given string to lower case
    punctuation_to_spaces
        Turns any character which is not a letter or a number into a space character
    remove_punctuation
        Removes any character which is not a letter or a number
    numbers_to_spaces
        Turns all number characters in a given string into space characters
    remove_numbers
        Removes all number characters from a given string
    remove_spaces
        Removes all spaces from a given string
    newlines_to_spaces
        Turn newline characters ("\\n") into space characters in a given string
    multiple_spaces_to_single_spaces
        Turns every sequence of space characters in a given string into a single space character
    remove_spaces_at_start_and_end
        Remove any spaces characters
    non_letters_to_spaces
        Turn every character in a given string which is not a letter into a single space character
    remove_non_letters
        Remove every character in a given string which is not a letter
    join_single_space_separated_letters_together
        Removes the space characters between sequences of single letter characters separated by a single space (e.g. "a  B c D  e" becomes "a  BcD  e")
    remove_non_printable_ascii_chars
        Removes all characters from a given string which are not in the python constant 'string.printable'
    """

    def __init__(self, verbose: bool = True) -> None:
        self.operations = {}
        self.verbose = verbose
        self.printable_ascii_chars = string.printable

        def extract_domain_from_url(raw_str: str) -> str:
            """Extracts the base domain from a given website URL

            Example Usage
            -------------
            >>> string_cleaner = StringCleaner()
            >>> string_cleaner.operations["extract_domain_from_url"]("https://www.google.co.uk/media/contact-us.php")
            'https://www.google.co.uk'
            """
            if self.verbose:
                print(
                    f"""
" ".join(
    re.findall(
        "(?P<url>https?://[^/]+)",
        "{raw_str}",
    )     
)           
"""
                )
            return " ".join(
                re.findall(
                    "(?P<url>https?://[^/]+)",
                    raw_str,
                )
            )

        def remove_words_or_phrases(
            raw_str: str,
            remove_list: typing.List[str],
            enforce_word_boundaries: bool,
            **kwargs,
        ) -> str:
            """Removes specific 'words' or 'phrases' (i.e. specific characters in a specific order) from a given string, possibly observing word boundaries

            Example Usage
            -------------
            >>> string_cleaner = StringCleaner()
            >>> string_cleaner.operations["remove_words_or_phrases"](
            ...    raw_str="the company name is big stinc inc",
            ...    remove_list=["inc"],
            ...    enforce_word_boundaries=False
            ... )
            'the company name is big st '
            >>> string_cleaner.operations["remove_words_or_phrases"](
            ...    raw_str="the company name is big stinc inc",
            ...    remove_list=["inc"],
            ...    enforce_word_boundaries=True
            ... )
            'the company name is big stinc '
            """
            if enforce_word_boundaries:
                if self.verbose:
                    print(
                        f"""
re.sub(
    "|".join([f"(\\\\b{{re.escape(x)}}\\\\b)" for x in {remove_list}]),
    "",
    "{raw_str}",
)"""
                    )
                return re.sub(
                    "|".join([f"(\\b{re.escape(x)}\\b)" for x in remove_list]),
                    "",
                    raw_str,
                )
            else:
                if self.verbose:
                    print(
                        f"""
re.sub( 
    "|".join( [f"({{re.escape(x)}})" for x in {remove_list}] ), 
    "", 
    "{raw_str}"
)                    
"""
                    )
                return re.sub(
                    "|".join([f"({re.escape(x)})" for x in remove_list]), "", raw_str
                )

        def to_lowercase(raw_str):
            """Converts all upper case characters in a given string to lower case"""
            return raw_str.lower()

        def punctuation_to_spaces(raw_str):
            """Turns any character in a given string that is not a number or letter"""
            return re.sub(r"[^A-Za-z0-9 ]+", " ", raw_str)

        def remove_punctuation(raw_str):
            return re.sub(r"[^A-Za-z0-9 ]+", "", raw_str)

        def numbers_to_spaces(raw_str):
            return raw_str.translate(
                str.maketrans("0123456789", " " * len("0123456789"))
            )

        def remove_numbers(raw_str):
            return raw_str.translate(str.maketrans("", "", "0123456789"))

        def remove_spaces(raw_str):
            return re.sub(" ", "", raw_str)

        def newlines_to_spaces(raw_str):
            return raw_str.replace("\n", " ")

        def multiple_spaces_to_single_spaces(raw_str):
            return re.sub(" +", " ", raw_str)

        def remove_spaces_at_start_and_end(raw_str):
            return raw_str.strip()

        def non_letters_to_spaces(raw_str):
            return re.sub("[^a-zA-Z]", " ", raw_str)

        def remove_non_letters(raw_str):
            return re.sub("[^a-zA-Z]", "", raw_str)

        def join_single_space_separated_letters_together(raw_str):
            return re.sub(r"\b([a-zA-Z]) (?=[a-zA-Z]\b)", r"\1", raw_str)

        def remove_non_printable_ascii_chars(raw_str):
            """Removes all characters from a given string which are not in the python constant 'string.printable'"""
            return "".join(filter(lambda x: x in self.printable_ascii_chars, raw_str))

        self.operations["extract_domain_from_url"] = extract_domain_from_url
        self.operations["remove_words_or_phrases"] = remove_words_or_phrases
        self.operations["to_lowercase"] = to_lowercase
        self.operations["punctuation_to_spaces"] = punctuation_to_spaces
        self.operations["remove_punctuation"] = remove_punctuation
        self.operations["numbers_to_spaces"] = numbers_to_spaces
        self.operations["remove_numbers"] = remove_numbers
        self.operations["remove_spaces"] = remove_spaces
        self.operations["newlines_to_spaces"] = newlines_to_spaces
        self.operations[
            "multiple_spaces_to_single_spaces"
        ] = multiple_spaces_to_single_spaces
        self.operations[
            "remove_spaces_at_start_and_end"
        ] = remove_spaces_at_start_and_end
        self.operations["non_letters_to_spaces"] = non_letters_to_spaces
        self.operations["remove_non_letters"] = remove_non_letters
        self.operations[
            "join_single_space_separated_letters_together"
        ] = join_single_space_separated_letters_together
        self.operations[
            "remove_non_printable_ascii_chars"
        ] = remove_non_printable_ascii_chars

        if self.verbose:
            print("-- Initiated StringCleaner() --")
            print("available string-cleaning operations:")
            for op_name in self.operations:
                print(f"\to {op_name}")

    def apply_sequential_operations(
        self,
        raw_str: str,
        operation_names_list: typing.List[str],
        operation_params_dict: dict = {},
    ) -> str:
        """Sequentially applies 1 or more string cleaning operations to a given string

        Parameters
        ----------
        raw_str: str
            The string to be processed
        operation_names_list: List[str]
            A list containing the names (operations will be applied in the order provided in this list)
        operation_params_dict: dict, optional
            This dictionary is used to passed named parameters to string cleaning functions which require specific parameters
            (refer to example usage below)

        Returns
        -------
        str
            The input string, after having applied all of the string cleaning operations to it

        Example Usage
        -------------
        TODO
        """
        for op_name in operation_names_list:
            if op_name in operation_params_dict:
                raw_str = self.operations[op_name](
                    raw_str, **operation_params_dict[op_name]
                )
            else:
                raw_str = self.operations[op_name](raw_str)

        return raw_str
