# Joe's Giant ToolBox

This is a large collection of general python functions and classes that I use in my daily work

The various functions/classes exist at varying levels of completeness (e.g. some will have incomplete documentation or missing unit tests)

I have added in a confidence score for each function/class:

Confidence Score | Description                      
-----------------|-----------------------------------------
5                | Code has been used (without any failures) in multiple production environments (or large real world projects)
4                | Code has been used (without any failures) in a production environment (or large real world project)
3                | Code appears to work perfectly and passes a suite of unit tests but has not yet been used in a production environment or large real world project 
2                | The code appears to work perfectly but has not been thoroughly tested
1                | Skeleton of function/class is present but the code does not work fully yet 

You can search by category:

* [API and Web](#api-and-web) 

* [Data Visualisation](#data-visualisation)

* [Google Cloud](#google-cloud)

* [Statistical Inference and Hypothesis Testing](#statistical-inference-and-hypothesis-testing)

..or you can just scroll through the master list:

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
ascii_barplot           | A function which draws a barplot using only raw text symbols            | functions/ascii_barplot.py           |                |            |                             | 2                |
ascii_density_histogram | A function which draws a histogram using only raw text symbols          | functions/ascii_density_histogram.py |                |            |                             | 2                |
conjugate_prior_beta_binomial | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | functions/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |
list_files_in_gcloud_bucket | Function which returns a list of the files present in a specified google cloud bucket | functions/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |
make_url_request | A convenience function for making API requests using the urllib library | functions/make_url_request.py | x              | x          | tests/make_url_request.py   | 3                |

## API and Web

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
make_url_request | A convenience function for making API requests using the urllib library | functions/test_make_url_request.py | x              | x          | tests/make_url_request.py   | 3                |

## Data Visualisation

Function Name           | Description                                                             | Location                             | Code Completed | Documentation Completed | Tests                       | Confidence Score |
------------------------|-------------------------------------------------------------------------|--------------------------------------|----------------|------------|-----------------------------|----------
ascii_barplot           | A function which draws a barplot using only raw text symbols            | functions/ascii_barplot.py           |                |            |                             | 2                |
ascii_density_histogram | A function which draws a histogram using only raw text symbols          | functions/ascii_density_histogram.py |                |            |                             | 2                |

## Google Cloud

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
list_files_in_gcloud_bucket | Function which returns a list of the files present in a specified google cloud bucket | functions/list_files_in_gcloud_bucket.py | x              | x          |     | 4                |


## Statistical Inference and Hypothesis Testing 

Function Name    | Description                                                             | Location                      | Code Completed | Documentation Completed | Tests                       | Confidence Score |
-----------------|-------------------------------------------------------------------------|-------------------------------|----------------|------------|-----------------------------|------------------|
conjugate_prior_beta_binomial | Function which calculates the posterior distribution of the success probability parameter [p] of a binomial distribution, from observed data and a user-specified beta prior | functions/conjugate_prior_beta_binomial.py | x              | x          | tests/test_conjugate_prior_beta_binomial.py    | 4                |

## Run Units Tests

```bash
pip install pytest
pytest -v
```