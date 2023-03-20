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
ascii art source: https://ascii.co.uk

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

* [Statistical Inference and Hypothesis Testing](#statistical-inference-and-hypothesis-testing)

* [Text and Natural Language Processing](#text-and-natural-language-processing)

..or you can just scroll through the master list:

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
ascii_barplot           | A function which draws a barplot using only raw text symbols            | joes_giant_toolbox/ascii_barplot.py           |                |            |                             | 2                |
ascii_density_histogram | A function which draws a histogram using only raw text symbols          | joes_giant_toolbox/ascii_density_histogram.py |                |            |                             | 2                |
conjugate_prior_beta_binomial | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | joes_giant_toolbox/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |
download_file_from_gcloud_bucket_to_python | Function which reads a file from a google cloud bucket into python memory | joes_giant_toolbox/download_file_from_gcloud_bucket_to_python.py | x | x | | 4 |
list_files_in_gcloud_bucket | Function which returns a list of the files present in a specified google cloud bucket | joes_giant_toolbox/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |
longest_portion_of_phrase_in_search_string | A function for finding the longest subsequence of words in a phrase string that occur within a search string | joes_giant_toolbox/longest_portion_of_phrase_in_search_string.py | x | x | | 2 |
make_url_request | A convenience function for making API requests using the urllib library | joes_giant_toolbox/make_url_request.py | x              | x          | tests/test_make_url_request.py   | 3                |
query_bigquery_to_pandas_df | Function which runs a query on Google BigQuery and writes the result into a local pandas.DataFrame | joes_giant_toolbox/query_bigquery_to_pandas_df.py | x              | x          |     | 4                |
scrape_webpage_and_all_linked_webpages | Function extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too | joes_giant_toolbox/scrape_webpage_and_all_linked_wepages.py | x | x | | 2
string_cleaner | A class for chaining common string-cleaning operations | joes_giant_toolbox/string_cleaner.py |                |            | tests/test_string_cleaner.py    | 2                |
view_nested_dict_structure | Provides a simple printout for understanding the structure of a complex nested python dictionary | joes_giant_toolbox/view_nested_dict_structure.py |                |            |                             | 2                |
write_pandas_df_to_google_bigquery_table  | Function which writes a pandas dataframe to a table on Google BigQuery | joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py | x              | x          |     | 4                |

## API and Web

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
make_url_request | A convenience function for making API requests using the urllib library | joes_giant_toolbox/make_url_request.py | x              | x          | tests/test_make_url_request.py   | 3                |
scrape_webpage_and_all_linked_webpages | Function extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too | joes_giant_toolbox/scrape_webpage_and_all_linked_wepages.py | x | x | | 2

## Data Visualisation

Function Name           | Description                                                             | Location                             | Code Completed | Documentation Completed | Tests                       | Confidence Score |
------------------------|-------------------------------------------------------------------------|--------------------------------------|----------------|------------|-----------------------------|----------
ascii_barplot           | A function which draws a barplot using only raw text symbols            | joes_giant_toolbox/ascii_barplot.py           |                |            |                             | 2                |
ascii_density_histogram | A function which draws a histogram using only raw text symbols          | joes_giant_toolbox/ascii_density_histogram.py |                |            |                             | 2                |
view_nested_dict_structure | Provides a simple printout for understanding the structure of a complex nested python dictionary | joes_giant_toolbox/view_nested_dict_structure.py |                |            |                             | 2                |

## Google Cloud

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
download_file_from_gcloud_bucket_to_python | Function which reads a file from a google cloud bucket into python memory | joes_giant_toolbox/download_file_from_gcloud_bucket_to_python.py | x | x | | 4 |
list_files_in_gcloud_bucket | Function which returns a list of the files present in a specified google cloud bucket | joes_giant_toolbox/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |
query_bigquery_to_pandas_df | Function which runs a query on Google BigQuery and writes the result into a local pandas.DataFrame | joes_giant_toolbox/query_bigquery_to_pandas_df.py | x              | x          |     | 4                |
write_pandas_df_to_google_bigquery_table  | Function which writes a pandas dataframe to a table on Google BigQuery | joes_giant_toolbox/write_pandas_df_to_google_bigquery_table.py | x              | x          |     | 4                |


/Users/josephbolton/personal_projects/joes_giant_toolbox/joes_giant_toolbox/query_bigquery_to_pandas_df.py

## Statistical Inference and Hypothesis Testing 

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
conjugate_prior_beta_binomial | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | joes_giant_toolbox/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |

## Text and Natural Language Processing
Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
longest_portion_of_phrase_in_search_string | A function for finding the longest subsequence of words in a phrase string that occur within a search string | joes_giant_toolbox/longest_portion_of_phrase_in_search_string.py | x | x | | 2 |
string_cleaner | A class for chaining common string-cleaning operations | joes_giant_toolbox/string_cleaner.py |                |            | tests/test_string_cleaner.py    | 2                |


# Run Unit Tests

```bash
pip install pytest
pytest -v
```