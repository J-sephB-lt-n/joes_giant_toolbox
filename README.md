# Joe's Giant Tool Box

This is a large collection of general python functions and classes that I use in my daily work

```
                                                     .-.
                                                    /   \
                                     _____.....-----|(o) |
                               _..--'          _..--|  .''
                             .'  o      _..--''     |  | |
                            /  _/_..--''            |  | |
                   ________/  / /                   |  | |
                  | _  ____\ / /                    |  | |
 _.-----._________|| ||    \\ /                     |  | |
|=================||=||_____\\                      |__|-'
|                 ||_||_____//                      (o\ |
|_________________|_________/                        |-\|
 `-------------._______.----'                        /  `.
    .,.,.,.,.,.,.,.,.,.,.,.,.,                      /     \
   ((O) o o o o ======= o o(O))                 ._.'      /
LGB `-.,.,.,.,.,.,.,.,.,.,.,-'                   `.......'
```
source: https://ascii.co.uk

The scripts exist at varying levels of completeness (some have seen extensive use in many projects whereas others have been used little or have incomplete documentation and missing unit tests). In order to measure this, I have added in a confidence score for each:

Confidence Score | Description                      
-----------------|-----------------------------------------
5                | Code has been used (without any observed failures) in multiple production environments (or large real world projects)
4                | Code has been used (without any observed failures) in a production environment (or large real world project)
3                | Code appears to work perfectly and passes a suite of unit tests but has not yet been used in a production environment or large real world project 
2                | The code appears to work perfectly but has not been thoroughly tested
1                | Skeleton of function/class is present but the code does not work fully yet 

You can search by category:

* [API and Web](#api-and-web) 

* [Data Visualisation](#data-visualisation)

* [Google Cloud](#google-cloud)

* [Python Convenience Functions](#python-convenience-functions) 

* [Statistical Inference and Hypothesis Testing](#statistical-inference-and-hypothesis-testing)

* [Statistical Modelling and Machine Learning](#statistical-modelling-and-machine-learning)

* [Text and Natural Language Processing](#text-and-natural-language-processing)

..or you can just scroll through the master list:

Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
[anonymous_view_public_linkedin_page](joes_giant_toolbox/anonymous_view_public_linkedin_page.py) | Function extracts the information (HTML) from a public LinkedIn page (e.g. person or company) using a virtual browser | joes_giant_toolbox/anonymous_view_public_linkedin_page.py | x | x | | 2 |
[ascii_barplot](joes_giant_toolbox/ascii_barplot.py)           | A function which draws a barplot using only raw text symbols            | joes_giant_toolbox/ascii_barplot.py           |                |            |                             | 2                |
[ascii_density_histogram](joes_giant_toolbox/ascii_density_histogram.py) | A function which draws a histogram using only raw text symbols          | joes_giant_toolbox/ascii_density_histogram.py |                |            |                             | 2                |
[conjugate_prior_beta_binomial](joes_giant_toolbox/conjugate_prior_beta_binomial.py) | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | joes_giant_toolbox/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |
[delete_file_in_gcloud_bucket](joes_giant_toolbox/delete_file_in_gcloud_bucket.py) | Function to delete a file which is in a google cloud bucket | joes_giant_toolbox/delete_file_in_gcloud_bucket.py | x | x | | 4 |
[download_file_from_gcloud_bucket_to_python](download_file_from_gcloud_bucket_to_python.py) | Function which reads a file from a google cloud bucket into python memory | joes_giant_toolbox/download_file_from_gcloud_bucket_to_python.py | x | x | | 4 |
[duckduckgo_search_multipage](joes_giant_toolbox/duckduckgo_search_multipage.py) | Function fetches search results from the DuckDuckGo Lite search engine | joes_giant_toolbox/duckduckgo_search_multipage.py | x | x | | 2 |
[list_files_in_gcloud_bucket](joes_giant_toolbox/list_files_in_gcloud_bucket.py) | Function which returns a list of the files present in a specified google cloud bucket | joes_giant_toolbox/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |
[longest_portion_of_phrase_in_search_string](joes_giant_toolbox/longest_portion_of_phrase_in_search_string.py) | A function for finding the longest subsequence of words in a phrase string that occur within a search string | joes_giant_toolbox/longest_portion_of_phrase_in_search_string.py | x | x | | 2 |
[make_url_request](joes_giant_toolbox/make_url_request.py) | A convenience function for making API requests using the urllib library | joes_giant_toolbox/make_url_request.py | x              | x          | tests/test_make_url_request.py   | 3                |
[move_or_rename_file_in_gcloud_bucket](joes_giant_toolbox/move_or_rename_file_in_gcloud_bucket.py) | Function to move or rename a file which is in a google cloud bucket (which includes moving it to a different bucket) | joes_giant_toolbox/move_or_rename_file_in_gcloud_bucket.py | x | x | | 2 |
[query_bigquery_to_pandas_df](joes_giant_toolbox/query_bigquery_to_pandas_df.py) | Function which runs a query on Google BigQuery and writes the result into a local pandas.DataFrame | joes_giant_toolbox/query_bigquery_to_pandas_df.py | x              | x          |     | 4                |
[RapidBinaryClassifier](joes_giant_toolbox/rapid_binary_classifier.py) | Class facilitating the ultra rapid generation of binary classifier models in scikit-learn by abstracting away a lot of the decisions and model code | joes_giant_toolbox/rapid_binary_classifier.py | x | | tests/test_rapid_binary_classifier.py | 2.5 |
[run_python_function_in_parallel](joes_giant_toolbox/run_python_function_in_parallel.py) | Convenience function for running a python function in parallel on multiple cores or threads | joes_giant_toolbox/run_python_function_in_parallel.py | x | x | | 2 |
[scrape_webpage_and_all_linked_webpages](joes_giant_toolbox/scrape_webpage_and_all_linked_wepages.py) | Function extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too | joes_giant_toolbox/scrape_webpage_and_all_linked_wepages.py | x | x | | 2
[string_cleaner](joes_giant_toolbox/string_cleaner.py) | A class for chaining common string-cleaning operations | joes_giant_toolbox/string_cleaner.py |                |            | tests/test_string_cleaner.py    | 2                |
[upload_file_python_to_gcloud_bucket](joes_giant_toolbox/upload_file_python_to_gcloud_bucket.py) | Function writes an object in python memory to a file (blob) on a google cloud bucket | joes_giant_toolbox/upload_file_python_to_gcloud_bucket.py | x | x | | 2 |
[url_to_filename_to_url_mapper](joes_giant_toolbox/url_to_filename_to_url_mapper.py) | Converts a webpage URL into a useable filename, where the URL can be recovered from the filename | joes_giant_toolbox/url_to_filename_to_url_mapper.py | x | | | 2
[view_nested_dict_structure](joes_giant_toolbox/view_nested_dict_structure.py) | Provides a simple printout for understanding the structure of a complex nested python dictionary | joes_giant_toolbox/view_nested_dict_structure.py | x               |            |                             | 2                |
[write_pandas_df_to_google_bigquery_table](joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py)  | Function which writes a pandas dataframe to a table on Google BigQuery | joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py | x              | x          |     | 4                |

## API and Web

Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
[anonymous_view_public_linkedin_page](joes_giant_toolbox/anonymous_view_public_linkedin_page.py) | Function extracts the information (HTML) from a public LinkedIn page (e.g. person or company) using a virtual browser | joes_giant_toolbox/anonymous_view_public_linkedin_page.py | x | x | | 2 |
[duckduckgo_search_multipage](joes_giant_toolbox/duckduckgo_search_multipage.py) | Function fetches search results from the DuckDuckGo Lite search engine | joes_giant_toolbox/duckduckgo_search_multipage.py | x | x | | 2 |
[make_url_request](joes_giant_toolbox/make_url_request.py) | A convenience function for making API requests using the urllib library | joes_giant_toolbox/make_url_request.py | x              | x          | tests/test_make_url_request.py   | 3                |
[scrape_webpage_and_all_linked_webpages](joes_giant_toolbox/scrape_webpage_and_all_linked_webpages.py) | Function extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too | joes_giant_toolbox/scrape_webpage_and_all_linked_wepages.py | x | x | | 2
[url_to_filename_to_url_mapper](joes_giant_toolbox/url_to_filename_to_url_mapper.py) | Converts a webpage URL into a useable filename, where the URL can be recovered from the filename | joes_giant_toolbox/url_to_filename_to_url_mapper.py | x | | | 2

## Data Visualisation

Name           | Description                                                             | Location                             | Code Completed | Documentation Completed | Tests                       | Confidence Score |
------------------------|-------------------------------------------------------------------------|--------------------------------------|----------------|------------|-----------------------------|----------
ascii_barplot           | A function which draws a barplot using only raw text symbols            | joes_giant_toolbox/ascii_barplot.py           |                |            |                             | 2                |
ascii_density_histogram | A function which draws a histogram using only raw text symbols          | joes_giant_toolbox/ascii_density_histogram.py |                |            |                             | 2                |
view_nested_dict_structure | Provides a simple printout for understanding the structure of a complex nested python dictionary | joes_giant_toolbox/view_nested_dict_structure.py | x              |            |                             | 2                |

## Google Cloud

Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
[delete_file_in_gcloud_bucket](joes_giant_toolbox/delete_file_in_gcloud_bucket.py) | Function to delete a file which is in a google cloud bucket | joes_giant_toolbox/delete_file_in_gcloud_bucket.py | x | x | | 4 |
[download_file_from_gcloud_bucket_to_python](joes_giant_toolbox/download_file_from_gcloud_bucket_to_python.py) | Function which reads a file from a google cloud bucket into python memory | joes_giant_toolbox/download_file_from_gcloud_bucket_to_python.py | x | x | | 4 |
[list_files_in_gcloud_bucket](joes_giant_toolbox/list_files_in_gcloud_bucket.py) | Function which returns a list of the files present in a specified google cloud bucket | joes_giant_toolbox/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |
[move_or_rename_file_in_gcloud_bucket](joes_giant_toolbox/move_or_rename_file_in_gcloud_bucket.py) | Function to move or rename a file which is in a google cloud bucket (which includes moving it to a different bucket) | joes_giant_toolbox/move_or_rename_file_in_gcloud_bucket.py | x | x | | 2 |
[query_bigquery_to_pandas_df](joes_giant_toolbox/query_bigquery_to_pandas_df.py) | Function which runs a query on Google BigQuery and writes the result into a local pandas.DataFrame | joes_giant_toolbox/query_bigquery_to_pandas_df.py | x              | x          |     | 4                |
[upload_file_python_to_gcloud_bucket](joes_giant_toolbox/upload_file_python_to_gcloud_bucket.py) | Function writes an object in python memory to a file (blob) on a google cloud bucket | joes_giant_toolbox/upload_file_python_to_gcloud_bucket.py | x | x | | 2 |
[write_pandas_df_to_google_bigquery_table](joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py)  | Function which writes a pandas dataframe to a table on Google BigQuery | joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py | x              | x          |     | 4                |

## Python Convenience Functions 
Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
[run_python_function_in_parallel](joes_giant_toolbox/run_python_function_in_parallel.py) | Convenience function for running a python function in parallel on multiple cores or threads | joes_giant_toolbox/run_python_function_in_parallel.py | x | x | | 2 |

## Statistical Inference and Hypothesis Testing 

Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
conjugate_prior_beta_binomial | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | joes_giant_toolbox/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |

## Statistical Modelling and Machine Learning 

Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
[RapidBinaryClassifier](joes_giant_toolbox/rapid_binary_classifier.py) | Class facilitating the ultra rapid generation of binary classifier models in scikit-learn by abstracting away a lot of the decisions and model code | joes_giant_toolbox/rapid_binary_classifier.py | x | | tests/test_rapid_binary_classifier.py | 2.5 |

## Text and Natural Language Processing
Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
longest_portion_of_phrase_in_search_string | A function for finding the longest subsequence of words in a phrase string that occur within a search string | joes_giant_toolbox/longest_portion_of_phrase_in_search_string.py | x | x | | 2 |
string_cleaner | A class for chaining common string-cleaning operations | joes_giant_toolbox/string_cleaner.py |                |            | tests/test_string_cleaner.py    | 2                |


# Run Unit Tests

```bash
pip install pytest
pytest -v
```