# Joe's Giant Tool Box

A large collection of general python functions and classes that I use in my daily work

!! THE STRUCTURE OF THIS PROJECT IS GOING THROUGH A REFACTORING IN PREPARATION FOR RELEASE ON PYPI !!

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

* [Project Managment](#project-management)

* [Python Convenience Functions](#python-convenience-functions) 

* [Statistical Inference and Hypothesis Testing](#statistical-inference-and-hypothesis-testing)

* [Statistical Modelling and Machine Learning](#statistical-modelling-and-machine-learning)

* [Text and Natural Language Processing](#text-and-natural-language-processing)

..or you can just scroll through the master list:

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| anonymous_view_public_linkedin_page               | Extracts the information (HTML) from a public LinkedIn page (e.g. person or company) using a virtual browser |         2        |
| ascii_density_histogram                           | Draws a histogram using only raw text symbols                                                                |         2        |
| conjugate_prior_beta_binomial                     | Calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | 4                |
| create_project_scope_doc                          | Creates a basic project scope document (markdown) by prompting the user for input                            |         3        | 
| delete_file_in_gcloud_bucket                      | Deletes a file which is in a google cloud bucket                                                             |         4        |
| download_file_from_gcloud_bucket_to_python        | Reads a file from a google cloud bucket into python memory                                                   |         4        |
| duckduckgo_search_multipage                       | Fetches search results from the DuckDuckGo Lite search engine                                                |         2        |
| list_all_python_imports                           | Searches every python script in a given folder and lists all python modules imported within those scripts    |         2        |
| list_files_in_gcloud_bucket                       | Returns a list of the files present in a specified google cloud bucket                                       |         4        |
| longest_sentence_subsequence_plagiarism_detector  | Finds phrases (sequences of consecutive words) common to 2 documents (e.g. to act as a naive plagiarism detector) |    3        |
| make_url_request                                  | A convenience function for making API requests using the urllib library                                      |         3        |
| move_or_rename_file_in_gcloud_bucket              | Move or rename a file which is in a google cloud bucket (which includes moving it to a different bucket)     |         4        |
| print_progress_bar                                | Prints a progress bar (to standard out) while code is running                                                |         3        |
| query_bigquery_to_pandas_df                       | Runs a query on Google BigQuery and writes the result into a local pandas.DataFrame                          |         4        |
| RapidBinaryClassifier                             | Ultra rapid generation of binary classifier models in scikit-learn by abstracting away a lot of the decisions and model code| 3 |
| run_python_function_in_parallel                   | Runs a python function in parallel on multiple cores or threads                                              |         4        |
| scrape_webpage_and_all_linked_webpages            | Extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too |         1        | 
| StringCleaner                                     | Performs common string-cleaning operations to a text string, also allowing them to be chained in sequence    |         1        |
| upload_file_python_to_gcloud_bucket               | Writes an object in python memory to a file (blob) on a google cloud bucket                                  |         4        |
| url_to_filename_to_url_mapper                     | Converts a webpage URL into a useable filename, where the URL can be recovered directly from the filename    |         2        |
| view_nested_dict_structure                        | Generates a simple printout for understanding the structure of a complex nested python dictionary            |         2        |
| write_pandas_df_to_google_bigquery_table          | Writes a pandas dataframe to a table on Google BigQuery                                                      |         4        |

## API and Web

```python
import joes_giant_toolbox.web
help( joes_giant_toolbox.web.anonymous_view_public_linkedin_page )
help( joes_giant_toolbox.web.duckduckgo_search_multipage )
help( joes_giant_toolbox.web.make_url_request )
help( joes_giant_toolbox.web.scrape_webpage_and_all_linked_webpages )
help( joes_giant_toolbox.web.url_to_filename_to_url_mapper ) 
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| anonymous_view_public_linkedin_page               | Extracts the information (HTML) from a public LinkedIn page (e.g. person or company) using a virtual browser |         2        |
| duckduckgo_search_multipage                       | Fetches search results from the DuckDuckGo Lite search engine                                                |         2        |
| make_url_request                                  | A convenience function for making API requests using the urllib library                                      |         3        |
| scrape_webpage_and_all_linked_webpages            | Extracts HTML from given web page, and also follows all of the hyperlinks on that page and scrapes those too |         1        | 
| url_to_filename_to_url_mapper                     | Converts a webpage URL into a useable filename, where the URL can be recovered directly from the filename    |         2        |

## Data Visualisation

```python
import joes_giant_toolbox.dataviz
help( joes_giant_toolbox.dataviz.ascii_density_histogram )
help( joes_giant_toolbox.dataviz.view_nested_dict_structure )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| ascii_density_histogram                           | Draws a histogram using only raw text symbols                                                                |         2        |
| view_nested_dict_structure                        | Generates a simple printout for understanding the structure of a complex nested python dictionary            |         2        |

## Google Cloud

```python
import joes_giant_toolbox.google_cloud
help( joes_giant_toolbox.google_cloud.delete_file_in_gcloud_bucket )
help( joes_giant_toolbox.google_cloud.download_file_from_gcloud_bucket_to_python )
help( joes_giant_toolbox.google_cloud.list_files_in_gcloud_bucket )
help( joes_giant_toolbox.google_cloud.move_or_rename_file_in_gcloud_bucket )
help( joes_giant_toolbox.google_cloud.query_bigquery_to_pandas_df )
help( joes_giant_toolbox.google_cloud.upload_file_python_to_gcloud_bucket )
help( joes_giant_toolbox.google_cloud.write_pandas_df_to_google_bigquery_table )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| delete_file_in_gcloud_bucket                      | Deletes a file which is in a google cloud bucket                                                             |         4        |
| download_file_from_gcloud_bucket_to_python        | Reads a file from a google cloud bucket into python memory                                                   |         4        |
| list_files_in_gcloud_bucket                       | Returns a list of the files present in a specified google cloud bucket                                       |         4        |
| move_or_rename_file_in_gcloud_bucket              | Move or rename a file which is in a google cloud bucket (which includes moving it to a different bucket)     |         4        |
| query_bigquery_to_pandas_df                       | Runs a query on Google BigQuery and writes the result into a local pandas.DataFrame                          |         4        |
| upload_file_python_to_gcloud_bucket               | Writes an object in python memory to a file (blob) on a google cloud bucket                                  |         4        |
| write_pandas_df_to_google_bigquery_table          | Writes a pandas dataframe to a table on Google BigQuery                                                      |         4        |

## Project Management
```python
import joes_giant_toolbox.proj_mgmt
help( joes_giant_toolbox.proj_mgmt.create_project_scope_doc )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| create_project_scope_doc                          | Creates a basic project scope document (markdown) by prompting the user for input                            |         3        | 


## Python Convenience Functions 
```python
import joes_giant_toolbox.convenience
help( joes_giant_toolbox.convenience.list_all_python_imports )
help( joes_giant_toolbox.convenience.print_progress_bar )
help( joes_giant_toolbox.convenience.run_python_function_in_parallel )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| list_all_python_imports                           | Searches every python script in a given folder and lists all python modules imported within those scripts    |         2        |
| print_progress_bar                                | Prints a progress bar (to standard out) while code is running                                                |         3        |
| run_python_function_in_parallel                   | Runs a python function in parallel on multiple cores or threads                                              |         4        |

## Statistical Inference and Hypothesis Testing 
```python
import joes_giant_toolbox.stats
help( joes_giant_toolbox.stats.conjugate_prior_beta_binomial )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| conjugate_prior_beta_binomial                     | Calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | 4                |

## Statistical Modelling and Machine Learning 
```python
import joes_giant_toolbox.sklearn
help( joes_giant_toolbox.sklearn.RapidBinaryClassifier )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| RapidBinaryClassifier                             | Ultra rapid generation of binary classifier models in scikit-learn by abstracting away a lot of the decisions and model code| 3 |

## Text and Natural Language Processing
```python 
import joes_giant_toolbox.text
help( joes_giant_toolbox.text.longest_sentence_subsequence_plagiarism_detector )
help( joes_giant_toolbox.text.StringCleaner )
```

| Name                                              | Description                                                                                                  | Confidence Score |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| longest_sentence_subsequence_plagiarism_detector  | Finds phrases (sequences of consecutive words) common to 2 documents (e.g. to act as a naive plagiarism detector) |    3        |
| StringCleaner                                     | Performs common string-cleaning operations to a text string, also allowing them to be chained in sequence    |         1        |

# Run Unit Tests

```bash
git clone https://github.com/J-sephB-lt-n/joes_giant_toolbox.git
pip install pytest
pytest -v
```