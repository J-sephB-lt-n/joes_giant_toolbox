Joe’s Giant Tool Box
====================

A large collection of general python functions and classes that I use in
my daily work

::

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

source: https://ascii.co.uk

The scripts exist at varying levels of completeness (some have seen
extensive use in many projects whereas others have been used little or
have incomplete documentation and missing unit tests). In order to
measure this, I have added in a confidence score for each:

+--------------------+-------------------------------------------------+
| Confidence Score   | Description                                     |
+====================+=================================================+
| 5                  | Code has been used (without any observed        |
|                    | failures) in multiple production environments   |
|                    | (or large real world projects)                  |
+--------------------+-------------------------------------------------+
| 4                  | Code has been used (without any observed        |
|                    | failures) in a production environment (or large |
|                    | real world project)                             |
+--------------------+-------------------------------------------------+
| 3                  | Code appears to work perfectly and passes a     |
|                    | suite of unit tests but has not yet been used   |
|                    | in a production environment or large real world |
|                    | project                                         |
+--------------------+-------------------------------------------------+
| 2                  | The code appears to work perfectly but has not  |
|                    | been thoroughly tested                          |
+--------------------+-------------------------------------------------+
| 1                  | Skeleton of function/class is present but the   |
|                    | code does not work fully yet                    |
+--------------------+-------------------------------------------------+

You can search by category:

-  `API and Web <#api-and-web>`__

-  `Data Visualisation <#data-visualisation>`__

-  `Google Cloud <#google-cloud>`__

-  `Project Managment <#project-management>`__

-  `Python Convenience Functions <#python-convenience-functions>`__

-  `Statistical Inference and Hypothesis
   Testing <#statistical-inference-and-hypothesis-testing>`__

-  `Statistical Modelling and Machine
   Learning <#statistical-modelling-and-machine-learning>`__

-  `Text and Natural Language
   Processing <#text-and-natural-language-processing>`__

..or you can just scroll through the master list:

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| a                 | Extracts the information (HTML) from a    | 2    |
| nonymous_view_pub | public LinkedIn page (e.g. person or      |      |
| lic_linkedin_page | company) using a virtual browser          |      |
+-------------------+-------------------------------------------+------+
| ascii_            | Draws a histogram using only raw text     | 2    |
| density_histogram | symbols                                   |      |
+-------------------+-------------------------------------------+------+
| conjugate_pr      | Calculates the posterior distribution of  | 4    |
| ior_beta_binomial | the success probability parameter [p] of  |      |
|                   | a binomial distribution, from observed    |      |
|                   | data and a user-specified beta prior      |      |
+-------------------+-------------------------------------------+------+
| create_           | Creates a basic project scope document    | 3    |
| project_scope_doc | (markdown) by prompting the user for      |      |
|                   | input                                     |      |
+-------------------+-------------------------------------------+------+
| delete_file       | Deletes a file which is in a google cloud | 4    |
| _in_gcloud_bucket | bucket                                    |      |
+-------------------+-------------------------------------------+------+
| download          | Reads a file from a google cloud bucket   | 4    |
| _file_from_gcloud | into python memory                        |      |
| _bucket_to_python |                                           |      |
+-------------------+-------------------------------------------+------+
| duckduckgo        | Fetches search results from the           | 2    |
| _search_multipage | DuckDuckGo Lite search engine             |      |
+-------------------+-------------------------------------------+------+
| list_a            | Searches every python script in a given   | 2    |
| ll_python_imports | folder and lists all python modules       |      |
|                   | imported within those scripts             |      |
+-------------------+-------------------------------------------+------+
| list_files        | Returns a list of the files present in a  | 4    |
| _in_gcloud_bucket | specified google cloud bucket             |      |
+-------------------+-------------------------------------------+------+
| longest_senten    | Finds phrases (sequences of consecutive   | 3    |
| ce_subsequence_pl | words) common to 2 documents (e.g. to act |      |
| agiarism_detector | as a naive plagiarism detector)           |      |
+-------------------+-------------------------------------------+------+
| make_url_request  | A convenience function for making API     | 3    |
|                   | requests using the urllib library         |      |
+-------------------+-------------------------------------------+------+
| mo                | Move or rename a file which is in a       | 4    |
| ve_or_rename_file | google cloud bucket (which includes       |      |
| _in_gcloud_bucket | moving it to a different bucket)          |      |
+-------------------+-------------------------------------------+------+
| p                 | Prints a progress bar (to standard out)   | 3    |
| rint_progress_bar | while code is running                     |      |
+-------------------+-------------------------------------------+------+
| query_bigq        | Runs a query on Google BigQuery and       | 4    |
| uery_to_pandas_df | writes the result into a local            |      |
|                   | pandas.DataFrame                          |      |
+-------------------+-------------------------------------------+------+
| Rapi              | Ultra rapid generation of binary          | 3    |
| dBinaryClassifier | classifier models in scikit-learn by      |      |
|                   | abstracting away a lot of the decisions   |      |
|                   | and model code                            |      |
+-------------------+-------------------------------------------+------+
| run_python_fun    | Runs a python function in parallel on     | 4    |
| ction_in_parallel | multiple cores or threads                 |      |
+-------------------+-------------------------------------------+------+
| scra              | Extracts HTML from given web page, and    | 1    |
| pe_webpage_and_al | also follows all of the hyperlinks on     |      |
| l_linked_webpages | that page and scrapes those too           |      |
+-------------------+-------------------------------------------+------+
| StringCleaner     | Performs common string-cleaning           | 1    |
|                   | operations to a text string, also         |      |
|                   | allowing them to be chained in sequence   |      |
+-------------------+-------------------------------------------+------+
| u                 | Writes an object in python memory to a    | 4    |
| pload_file_python | file (blob) on a google cloud bucket      |      |
| _to_gcloud_bucket |                                           |      |
+-------------------+-------------------------------------------+------+
| url_to_filen      | Converts a webpage URL into a useable     | 2    |
| ame_to_url_mapper | filename, where the URL can be recovered  |      |
|                   | directly from the filename                |      |
+-------------------+-------------------------------------------+------+
| view_nest         | Generates a simple printout for           | 2    |
| ed_dict_structure | understanding the structure of a complex  |      |
|                   | nested python dictionary                  |      |
+-------------------+-------------------------------------------+------+
| write_            | Writes a pandas dataframe to a table on   | 4    |
| pandas_df_to_goog | Google BigQuery                           |      |
| le_bigquery_table |                                           |      |
+-------------------+-------------------------------------------+------+

API and Web
-----------

.. code:: python

   import joes_giant_toolbox.web
   help( joes_giant_toolbox.web.anonymous_view_public_linkedin_page )
   help( joes_giant_toolbox.web.duckduckgo_search_multipage )
   help( joes_giant_toolbox.web.make_url_request )
   help( joes_giant_toolbox.web.scrape_webpage_and_all_linked_webpages )
   help( joes_giant_toolbox.web.url_to_filename_to_url_mapper ) 

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| a                 | Extracts the information (HTML) from a    | 2    |
| nonymous_view_pub | public LinkedIn page (e.g. person or      |      |
| lic_linkedin_page | company) using a virtual browser          |      |
+-------------------+-------------------------------------------+------+
| duckduckgo        | Fetches search results from the           | 2    |
| _search_multipage | DuckDuckGo Lite search engine             |      |
+-------------------+-------------------------------------------+------+
| make_url_request  | A convenience function for making API     | 3    |
|                   | requests using the urllib library         |      |
+-------------------+-------------------------------------------+------+
| scra              | Extracts HTML from given web page, and    | 1    |
| pe_webpage_and_al | also follows all of the hyperlinks on     |      |
| l_linked_webpages | that page and scrapes those too           |      |
+-------------------+-------------------------------------------+------+
| url_to_filen      | Converts a webpage URL into a useable     | 2    |
| ame_to_url_mapper | filename, where the URL can be recovered  |      |
|                   | directly from the filename                |      |
+-------------------+-------------------------------------------+------+

Data Visualisation
------------------

.. code:: python

   import joes_giant_toolbox.dataviz
   help( joes_giant_toolbox.dataviz.ascii_density_histogram )
   help( joes_giant_toolbox.dataviz.view_nested_dict_structure )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| ascii_            | Draws a histogram using only raw text     | 2    |
| density_histogram | symbols                                   |      |
+-------------------+-------------------------------------------+------+
| view_nest         | Generates a simple printout for           | 2    |
| ed_dict_structure | understanding the structure of a complex  |      |
|                   | nested python dictionary                  |      |
+-------------------+-------------------------------------------+------+

Google Cloud
------------

.. code:: python

   import joes_giant_toolbox.google_cloud
   help( joes_giant_toolbox.google_cloud.delete_file_in_gcloud_bucket )
   help( joes_giant_toolbox.google_cloud.download_file_from_gcloud_bucket_to_python )
   help( joes_giant_toolbox.google_cloud.list_files_in_gcloud_bucket )
   help( joes_giant_toolbox.google_cloud.move_or_rename_file_in_gcloud_bucket )
   help( joes_giant_toolbox.google_cloud.query_bigquery_to_pandas_df )
   help( joes_giant_toolbox.google_cloud.upload_file_python_to_gcloud_bucket )
   help( joes_giant_toolbox.google_cloud.write_pandas_df_to_google_bigquery_table )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| delete_file       | Deletes a file which is in a google cloud | 4    |
| _in_gcloud_bucket | bucket                                    |      |
+-------------------+-------------------------------------------+------+
| download          | Reads a file from a google cloud bucket   | 4    |
| _file_from_gcloud | into python memory                        |      |
| _bucket_to_python |                                           |      |
+-------------------+-------------------------------------------+------+
| list_files        | Returns a list of the files present in a  | 4    |
| _in_gcloud_bucket | specified google cloud bucket             |      |
+-------------------+-------------------------------------------+------+
| mo                | Move or rename a file which is in a       | 4    |
| ve_or_rename_file | google cloud bucket (which includes       |      |
| _in_gcloud_bucket | moving it to a different bucket)          |      |
+-------------------+-------------------------------------------+------+
| query_bigq        | Runs a query on Google BigQuery and       | 4    |
| uery_to_pandas_df | writes the result into a local            |      |
|                   | pandas.DataFrame                          |      |
+-------------------+-------------------------------------------+------+
| u                 | Writes an object in python memory to a    | 4    |
| pload_file_python | file (blob) on a google cloud bucket      |      |
| _to_gcloud_bucket |                                           |      |
+-------------------+-------------------------------------------+------+
| write_            | Writes a pandas dataframe to a table on   | 4    |
| pandas_df_to_goog | Google BigQuery                           |      |
| le_bigquery_table |                                           |      |
+-------------------+-------------------------------------------+------+

Project Management
------------------

.. code:: python

   import joes_giant_toolbox.proj_mgmt
   help( joes_giant_toolbox.proj_mgmt.create_project_scope_doc )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| create_           | Creates a basic project scope document    | 3    |
| project_scope_doc | (markdown) by prompting the user for      |      |
|                   | input                                     |      |
+-------------------+-------------------------------------------+------+

Python Convenience Functions
----------------------------

.. code:: python

   import joes_giant_toolbox.convenience
   help( joes_giant_toolbox.convenience.list_all_python_imports )
   help( joes_giant_toolbox.convenience.print_progress_bar )
   help( joes_giant_toolbox.convenience.run_python_function_in_parallel )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| list_a            | Searches every python script in a given   | 2    |
| ll_python_imports | folder and lists all python modules       |      |
|                   | imported within those scripts             |      |
+-------------------+-------------------------------------------+------+
| p                 | Prints a progress bar (to standard out)   | 3    |
| rint_progress_bar | while code is running                     |      |
+-------------------+-------------------------------------------+------+
| run_python_fun    | Runs a python function in parallel on     | 4    |
| ction_in_parallel | multiple cores or threads                 |      |
+-------------------+-------------------------------------------+------+

Statistical Inference and Hypothesis Testing
--------------------------------------------

.. code:: python

   import joes_giant_toolbox.stats
   help( joes_giant_toolbox.stats.conjugate_prior_beta_binomial )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| conjugate_pr      | Calculates the posterior distribution of  | 4    |
| ior_beta_binomial | the success probability parameter [p] of  |      |
|                   | a binomial distribution, from observed    |      |
|                   | data and a user-specified beta prior      |      |
+-------------------+-------------------------------------------+------+

Statistical Modelling and Machine Learning
------------------------------------------

.. code:: python

   import joes_giant_toolbox.sklearn
   help( joes_giant_toolbox.sklearn.RapidBinaryClassifier )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| Rapi              | Ultra rapid generation of binary          | 3    |
| dBinaryClassifier | classifier models in scikit-learn by      |      |
|                   | abstracting away a lot of the decisions   |      |
|                   | and model code                            |      |
+-------------------+-------------------------------------------+------+

Text and Natural Language Processing
------------------------------------

.. code:: python

   import joes_giant_toolbox.text
   help( joes_giant_toolbox.text.longest_sentence_subsequence_plagiarism_detector )
   help( joes_giant_toolbox.text.StringCleaner )

+-------------------+-------------------------------------------+------+
| Name              | Description                               | Co   |
|                   |                                           | nfid |
|                   |                                           | ence |
|                   |                                           | S    |
|                   |                                           | core |
+===================+===========================================+======+
| longest_senten    | Finds phrases (sequences of consecutive   | 3    |
| ce_subsequence_pl | words) common to 2 documents (e.g. to act |      |
| agiarism_detector | as a naive plagiarism detector)           |      |
+-------------------+-------------------------------------------+------+
| StringCleaner     | Performs common string-cleaning           | 1    |
|                   | operations to a text string, also         |      |
|                   | allowing them to be chained in sequence   |      |
+-------------------+-------------------------------------------+------+

Run Unit Tests
==============

.. code:: bash

   git clone https://github.com/J-sephB-lt-n/joes_giant_toolbox.git
   pip install pytest
   pytest -v
