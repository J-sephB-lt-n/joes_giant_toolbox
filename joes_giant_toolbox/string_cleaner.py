import re


class string_cleaner:
    """
    A utility for performing common string-cleaning operations.

    Cleaning operations can also be chained sequentially.

    Notes
    -----
    TODO

    Methods
    -------
    extract_domain_from_url
        Extracts the base domain from a given website URL
    apply_sequential_operations
        To a given string, applies cleaning operations one after the other
    remove_specific_words
        Removes specific 'words' (i.e. specific characters in a specific order) from a given string
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
        - DOCUMENTATION TODO
    newlines_to_spaces
        - DOCUMENTATION TODO
    multiple_spaces_to_single_spaces
        - DOCUMENTATION TODO
    remove_spaces_at_start_and_end
        - DOCUMENTATION TODO
    non_letters_to_spaces
        - DOCUMENTATION TODO
    remove_non_letters
        - DOCUMENTATION TODO
    join_single_space_separated_letters_together
        - DOCUMENTATION TODO

    Example Usage
    -------------
    string_cleaner_obj = string_cleaner()
    print("operations available:")
    for op in string_cleaner_obj.operations:
        print("\t","o ",op)

    string_cleaner_obj.apply_sequential_operations( "https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/api/polars.DataFrame.apply.html", ops_list=["extract_domain_from_url"])
    string_cleaner_obj.apply_sequential_operations( "j.o/e i*s NOT the best", ops_list=["remove_specific_words"], remove_words_list=["NOT", ".", "/", "*"])
    string_cleaner_obj.apply_sequential_operations( "j.o/e i*s NOT the best", ops_list=["remove_specific_words", "multiple_spaces_to_single_spaces"], remove_words_list=["NOT", ".", "/", "*"])
    string_cleaner_obj.apply_sequential_operations( "DirTy StRiNg", ops_list=["to_lowercase"] )
    string_cleaner_obj.apply_sequential_operations( "!_=,j>?@o#e$i%s^t&h*e(B[E}S|T.", ops_list=["remove_punctuation"] )
    string_cleaner_obj.apply_sequential_operations( "!_=,j>?@o#e$i%s^t&h*e(B[E}S|T.",ops_list=["punctuation_to_spaces"])
    string_cleaner_obj.apply_sequential_operations( "!_=,j>?@o#e$i%s^t&h*e(B[E}S|T.", ops_list=["to_lowercase","remove_punctuation"] )
    string_cleaner_obj.apply_sequential_operations( "012345678901!_=,j2>?@o3#e$456i%s7^8t9&h00*e(1B2[3E4}5S6|7T8.9", ops_list=["to_lowercase","remove_punctuation","remove_numbers"] )
    string_cleaner_obj.apply_sequential_operations( "1 2  3   4    5     6", ops_list=["multiple_spaces_to_single_spaces"] )
    string_cleaner_obj.apply_sequential_operations( "1 2  3   4    5     6", ops_list=["remove_spaces"] )
    string_cleaner_obj.apply_sequential_operations( '''1\n

        2

        3
        ''',
        ops_list=["newlines_to_spaces"]
    )
    string_cleaner_obj.apply_sequential_operations( '''1\n

        2

        3
        ''',
        ops_list=["newlines_to_spaces","multiple_spaces_to_single_spaces", "remove_spaces_at_start_and_end"]
    )
    string_cleaner_obj.apply_sequential_operations( "  I AM     SHOUTING ", ops_list=["to_lowercase","remove_spaces"] )
    string_cleaner_obj.apply_sequential_operations( "!j_O:e.F|o'R+p=R-e0S9i8D7e6N7t", ops_list=["remove_non_letters"])
    string_cleaner_obj.apply_sequential_operations( "!j_O:e.F|o'R+p=R-e0S9i8D7e6N7t", ops_list=["non_letters_to_spaces"])
    string_cleaner_obj.apply_sequential_operations("j O   e's favourite number is 6 9 420 a    c tually", ops_list=["multiple_spaces_to_single_spaces", "join_single_space_separated_letters_together"])
    """

    def __init__(self):
        import re

        self.version = 1.01

        self.operations = {}

        def extract_domain_from_url(raw_str):
            return " ".join(
                re.findall(
                    "(?P<url>https?://[^/]+)",
                    raw_str,
                )
            )

        def remove_specific_words(raw_str, remove_list):
            """
            # example #
            remove_specific_words(
                "j.o/e i*s NOT the best",
                remove_list=["NOT", ".", "/", "*"]
            )
            """
            return re.sub("|".join([re.escape(x) for x in remove_list]), "", raw_str)

        def to_lowercase(raw_str):
            return raw_str.lower()

        def punctuation_to_spaces(raw_str):
            return re.sub(r"[^A-Za-z0-9 ]+", " ", raw_str)

        def remove_punctuation(raw_str):
            return re.sub(r"[^A-Za-z0-9 ]+", "", raw_str)

        def numbers_to_spaces(raw_str):
            from string import digits

            return raw_str.translate(str.maketrans(digits, " " * len(digits)))

        def remove_numbers(raw_str):
            from string import digits

            return raw_str.translate(str.maketrans("", "", digits))

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

        self.operations["extract_domain_from_url"] = extract_domain_from_url
        self.operations["remove_specific_words"] = remove_specific_words
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

    def apply_sequential_operations(self, raw_string, ops_list, remove_words_list=None):
        for operation in ops_list:
            if operation == "remove_specific_words":
                raw_string = self.operations["remove_specific_words"](
                    raw_string, remove_list=remove_words_list
                )
            else:
                raw_string = self.operations[operation](raw_string)

        return raw_string
