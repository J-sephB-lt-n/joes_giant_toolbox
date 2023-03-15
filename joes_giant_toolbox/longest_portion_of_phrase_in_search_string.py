def longest_portion_of_phrase_in_search_string(phrase_str: str, search_str: str) -> str:
    """returns longest sequence of words from phrase present in search string

    Parameters
    ----------
    phrase_str: str
        The phrase (sequence of words) which we want to find in the search string
    search_str: str
        The string in which to search for a portion of the phrase
    Returns
    -------
    str
        The longest portion of the phrase that was found in the search string
        In the case of a tie for sequence length, returns the first one found
    Example Usage
    -------------
    >>>longest_portion_of_phrase_in_search_string(
        phrase_str="find me quickly please",
        search_str="please find which of find me and find me quickly contains the most of me",
    )
    >>>longest_portion_of_phrase_in_search_string(
        phrase_str="a b c d e f g h",
        search_str="a b a b c a b c d a b a a a b c a b c d e f a b c d e a",
    )
    """
    phrase_word_list = phrase_str.split()
    search_word_list = search_str.split()
    all_seq_found = []
    search_idx = 0
    while search_idx < len(search_word_list) - 1:
        search_word = search_word_list[search_idx]
        if search_word in phrase_word_list:
            seq_found = [search_word]
            phrase_idx = phrase_word_list.index(search_word)
            for next_phrase_word in phrase_word_list[phrase_idx + 1 :]:
                next_search_word = search_word_list[search_idx + 1]
                if next_search_word == next_phrase_word:
                    seq_found.append(next_search_word)
                    search_idx += 1
            all_seq_found.append(seq_found)
        search_idx += 1
    max_seq_len_found = max([len(x) for x in all_seq_found])
    gen = (seq for seq in all_seq_found if len(seq) == max_seq_len_found)
    return " ".join(next(gen))
