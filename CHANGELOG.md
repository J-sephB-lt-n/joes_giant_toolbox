
# Change Log

## 0.7.1 new features

* Added fixed_batch functionality to **joes_giant_toolbox.convenience.data_batcher**

## 0.6.1 new features

* Added print depth control to **joes_giant_toolbox.dataviz.view_nested_dict_structure**

## 0.5.1 new features

* Added class **joes_giant_toolbox.convenience.DataBatcher**

## 0.4.1 new features

* Added function **joes_giant_toolbox.text.longest_common_substring()**

* Added function **joes_giant_toolbox.google_cloud.gcloud_vm_deletes_itself()**

* Added function **joes_giant_toolbox.web.parse_mime_email_parts()**

* Added function **joes_giant_toolbox.web.require_api_key()**

## 0.3.2 bug and documentation fixes

* Small change to documentation code example in create_parallel_google_cloud_run_job_template()

## 0.3.1 new features

* Added function **joes_giant_toolbox.google_cloud.create_parallel_google_cloud_run_job_template()**

* Added function **joes_giant_toolbox.google_cloud.gcloud_vm_deletes_itself()**

## 0.2.24 bug and documentation fixes

* Improved quality of **joes_giant_toolbox.text.RegexRulesClassifier** code (perfect pylint score)

## 0.2.23 bug fixes

* Method **remove_non_letters()** in **joes_giant_toolbox.text.StringCleaner()** no longer removes whitespace

## 0.2.22 bug fixes

* Improved the behaviour of **joes_giant_toolbox.text.RegexRulesClassifier** for the case where no rules match and ties_handling=="all"

## 0.2.21 bug fixes

* Fixed a bug introduced in version 0.2.2 in **joes_giant_toolbox.text.RegexRulesClassifier**

## 0.2.2 bug fixes

* Fixed the case of score=0 in **joes_giant_toolbox.text.RegexRulesClassifier**

## 0.2.1 bug and documentation fixes

* Fixed error in code in "Example Usage" of class **joes_giant_toolbox.text.RegexRulesClassifier**

* Small aesthetic changes to README.md

## 0.2.0 new features

* Added fig.tight_layout() to PythonPlottingTutorials().tutorials["grid_of_matplotlib_plots"]

* Added function **joes_giant_toolbox.google_cloud.create_gcloud_vm_docker_template**

* Added class **joes_giant_toolbox.text.RegexRulesClassifier**

## 0.1.0 new features

* Added additional documentation to function **joes_giant_toolbox.google_cloud.move_or_rename_file_in_gcloud_bucket**

* Added class **joes_giant_toolbox.dataviz.PythonPlottingTutorials**

* Added documentation to **joes_giant_toolbox.dataviz**

* Added documentation to **joes_giant_toolbox.google_cloud**

* Added documentation to **joes_giant_toolbox.stats**

* Added documentation to **joes_giant_toolbox.text**

* Added package dependency group **[google]**

* Added pypi version and download metrics to **README.md**

* Improved documentation of **joes_giant_toolbox.text.StringCleaner**

* Improved (verbose=True) output of function **joes_giant_toolbox.google_cloud.move_or_rename_file_in_gcloud_bucket**
