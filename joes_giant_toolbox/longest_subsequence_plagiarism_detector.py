import re

from print_progress_bar import print_progress_bar


def longest_sentence_subsequence_plagiarism_detector(
    ref_text: str,
    lookup_text: str,
    n_seq: int,
    verbose: bool = True,
):
    """
    Finds the longest [n_seq] consecutive sequences of words in [lookup_text] which also appear in [ref_text]

    This function was coded in a great rush and so:
    *   Is very slow
    *   Is very memory inefficient
    *   Is nonetheless useful, so I have kept it

    Parameters
    ----------
    TODO

    Returns
    -------
    TODO

    Example Usage
    -------------
    >>> longest_sentence_subsequence_plagiarism_detector(
        ref_text="keith allen haring may 4 1958 february 16 1990 was an american artist whose pop art emerged from the new york city graffiti subculture of the 1980s1 his animated imagery has become a widely recognized visual language2 much of his work includes sexual allusions that turned into social activism by using the images to advocate for safe sex and aids awareness3 in addition to solo gallery exhibitions he participated in renowned national and international group shows such as documenta in kassel the whitney biennial in new york the são paulo biennial and the venice biennale the whitney museum held a retrospective of his art in 1997",
        lookup_text="american artist whose art emerged from new york city graffiti subculture",
        n_seq=3,
    )
    """
    seq_found: list = []
    ref_words: list = ref_text.split()
    lookup_words: list = lookup_text.split()
    lookup_pass_idx: dict = {}
    progress_printer = print_progress_bar(base_message="")

    current_seq = []
    for lookup_word_idx in range(len(lookup_words)):
        progress_printer.print_progress(
            percent_complete=(lookup_word_idx + 1) / len(lookup_words)
        )
        for ref_word_idx in range(len(ref_words)):
            if lookup_word_idx in lookup_pass_idx:
                pass
            elif lookup_words[lookup_word_idx] == ref_words[ref_word_idx]:
                current_seq.append(lookup_words[lookup_word_idx])
                lookup_pass_idx[lookup_word_idx] = None
                temp_add = 1
                while 1 == 1:
                    if (
                        lookup_word_idx + temp_add < len(lookup_words)
                        and ref_word_idx + temp_add < len(ref_words)
                        and lookup_words[lookup_word_idx + temp_add]
                        == ref_words[ref_word_idx + temp_add]
                    ):
                        current_seq.append(lookup_words[lookup_word_idx + temp_add])
                        lookup_pass_idx[lookup_word_idx + temp_add] = None
                        temp_add += 1
                    else:
                        if len(current_seq) > 1:
                            seq_found.append(current_seq)
                        current_seq = []
                        break

    return [" ".join(x) for x in sorted(seq_found, key=len, reverse=True)[:n_seq]]


if __name__ == "__main__":
    with open("/Users/josephbolton/Downloads/thesis_text", "r") as f:
        thesis_text = f.read()

    with open("/Users/josephbolton/Downloads/paper_text", "r") as f:
        paper_text = f.read()

    thesis_text = re.sub("[^\w ]", "", thesis_text).lower()
    paper_text = re.sub("[^\w ]", "", paper_text).lower()

    test = longest_sentence_subsequence_plagiarism_detector(
        ref_text=thesis_text,
        lookup_text=paper_text,
        n_seq=200,
    )

    for x in test:
        print(x)
        print()
