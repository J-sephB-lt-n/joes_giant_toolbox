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

-  `Project Management <#project-management>`__

-  `Python Convenience Functions <#python-convenience-functions>`__

-  `Statistical Inference and Hypothesis
   Testing <#statistical-inference-and-hypothesis-testing>`__

-  `Statistical Modelling and Machine
   Learning <#statistical-modelling-and-machine-learning>`__

-  `Text and Natural Language
   Processing <#text-and-natural-language-processing>`__

..or you can just scroll through the master list:

+------+------------------------------+-----+----+-----------+------+
| Name | Description                  | C   | D  | Tests     | Co   |
|      |                              | ode | oc |           | nfid |
|      |                              | Com | um |           | ence |
|      |                              | ple | en |           | S    |
|      |                              | ted | ta |           | core |
|      |                              |     | ti |           |      |
|      |                              |     | on |           |      |
|      |                              |     | C  |           |      |
|      |                              |     | om |           |      |
|      |                              |     | pl |           |      |
|      |                              |     | et |           |      |
|      |                              |     | ed |           |      |
+======+==============================+=====+====+===========+======+
| `an  | Function extracts the        | x   | x  |           | 2    |
| onym | information (HTML) from a    |     |    |           |      |
| ous_ | public LinkedIn page         |     |    |           |      |
| view | (e.g. person or company)     |     |    |           |      |
| _pub | using a virtual browser      |     |    |           |      |
| lic_ |                              |     |    |           |      |
| link |                              |     |    |           |      |
| edin |                              |     |    |           |      |
| _pag |                              |     |    |           |      |
| e <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/an |                              |     |    |           |      |
| onym |                              |     |    |           |      |
| ous_ |                              |     |    |           |      |
| view |                              |     |    |           |      |
| _pub |                              |     |    |           |      |
| lic_ |                              |     |    |           |      |
| link |                              |     |    |           |      |
| edin |                              |     |    |           |      |
| _pag |                              |     |    |           |      |
| e.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `as  | A function which draws a     | x   | x  |           | 2    |
| cii_ | histogram using only raw     |     |    |           |      |
| dens | text symbols                 |     |    |           |      |
| ity_ |                              |     |    |           |      |
| hist |                              |     |    |           |      |
| ogra |                              |     |    |           |      |
| m <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/as |                              |     |    |           |      |
| cii_ |                              |     |    |           |      |
| dens |                              |     |    |           |      |
| ity_ |                              |     |    |           |      |
| hist |                              |     |    |           |      |
| ogra |                              |     |    |           |      |
| m.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `co  | Function which calculates    | x   | x  | tests/t   | 4    |
| njug | the posterior distribution   |     |    | est_conju |      |
| ate_ | of the success probability   |     |    | gate_prio |      |
| prio | parameter [p] of a binomial  |     |    | r_beta_bi |      |
| r_be | distribution, from observed  |     |    | nomial.py |      |
| ta_b | data and a user-specified    |     |    |           |      |
| inom | beta prior                   |     |    |           |      |
| ial  |                              |     |    |           |      |
| <joe |                              |     |    |           |      |
| s_gi |                              |     |    |           |      |
| ant_ |                              |     |    |           |      |
| tool |                              |     |    |           |      |
| box/ |                              |     |    |           |      |
| conj |                              |     |    |           |      |
| ugat |                              |     |    |           |      |
| e_pr |                              |     |    |           |      |
| ior_ |                              |     |    |           |      |
| beta |                              |     |    |           |      |
| _bin |                              |     |    |           |      |
| omia |                              |     |    |           |      |
| l.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Creates a basic project      | x   |    |           | 2    |
| crea | scope document (markdown)    |     |    |           |      |
| te_p | using user input prompts     |     |    |           |      |
| roje |                              |     |    |           |      |
| ct_s |                              |     |    |           |      |
| cope |                              |     |    |           |      |
| _doc |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /cre |                              |     |    |           |      |
| ate_ |                              |     |    |           |      |
| proj |                              |     |    |           |      |
| ect_ |                              |     |    |           |      |
| scop |                              |     |    |           |      |
| e_do |                              |     |    |           |      |
| c.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Function to delete a file    | x   | x  |           | 4    |
| dele | which is in a google cloud   |     |    |           |      |
| te_f | bucket                       |     |    |           |      |
| ile_ |                              |     |    |           |      |
| in_g |                              |     |    |           |      |
| clou |                              |     |    |           |      |
| d_bu |                              |     |    |           |      |
| cket |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /del |                              |     |    |           |      |
| ete_ |                              |     |    |           |      |
| file |                              |     |    |           |      |
| _in_ |                              |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `d   | Function which reads a file  | x   | x  |           | 4    |
| ownl | from a google cloud bucket   |     |    |           |      |
| oad_ | into python memory           |     |    |           |      |
| file |                              |     |    |           |      |
| _fro |                              |     |    |           |      |
| m_gc |                              |     |    |           |      |
| loud |                              |     |    |           |      |
| _buc |                              |     |    |           |      |
| ket_ |                              |     |    |           |      |
| to_p |                              |     |    |           |      |
| ytho |                              |     |    |           |      |
| n <d |                              |     |    |           |      |
| ownl |                              |     |    |           |      |
| oad_ |                              |     |    |           |      |
| file |                              |     |    |           |      |
| _fro |                              |     |    |           |      |
| m_gc |                              |     |    |           |      |
| loud |                              |     |    |           |      |
| _buc |                              |     |    |           |      |
| ket_ |                              |     |    |           |      |
| to_p |                              |     |    |           |      |
| ytho |                              |     |    |           |      |
| n.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `du  | Function fetches search      | x   | x  |           | 2    |
| ckdu | results from the DuckDuckGo  |     |    |           |      |
| ckgo | Lite search engine           |     |    |           |      |
| _sea |                              |     |    |           |      |
| rch_ |                              |     |    |           |      |
| mult |                              |     |    |           |      |
| ipag |                              |     |    |           |      |
| e <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/du |                              |     |    |           |      |
| ckdu |                              |     |    |           |      |
| ckgo |                              |     |    |           |      |
| _sea |                              |     |    |           |      |
| rch_ |                              |     |    |           |      |
| mult |                              |     |    |           |      |
| ipag |                              |     |    |           |      |
| e.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `li  | Searches every python script | x   | x  |           | 2    |
| st_a | in a given folder and lists  |     |    |           |      |
| ll_p | all python modules imported  |     |    |           |      |
| ytho | within those scripts         |     |    |           |      |
| n_im |                              |     |    |           |      |
| port |                              |     |    |           |      |
| s <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/li |                              |     |    |           |      |
| st_a |                              |     |    |           |      |
| ll_p |                              |     |    |           |      |
| ytho |                              |     |    |           |      |
| n_im |                              |     |    |           |      |
| port |                              |     |    |           |      |
| s.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `li  | Function which returns a     | x   | x  |           | 4    |
| st_f | list of the files present in |     |    |           |      |
| iles | a specified google cloud     |     |    |           |      |
| _in_ | bucket                       |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/li |                              |     |    |           |      |
| st_f |                              |     |    |           |      |
| iles |                              |     |    |           |      |
| _in_ |                              |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Finds phrases (sequences of  | x   | x  | tests/te  | 3    |
| long | consecutive words) common to |     |    | st_longes |      |
| est_ | 2 documents (e.g. to act as  |     |    | t_sentenc |      |
| sent | a naive plagiarism detector) |     |    | e_subsequ |      |
| ence |                              |     |    | ence_plag |      |
| _sub |                              |     |    | iarism_de |      |
| sequ |                              |     |    | tector.py |      |
| ence |                              |     |    |           |      |
| _pla |                              |     |    |           |      |
| giar |                              |     |    |           |      |
| ism_ |                              |     |    |           |      |
| dete |                              |     |    |           |      |
| ctor |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /lon |                              |     |    |           |      |
| gest |                              |     |    |           |      |
| _sen |                              |     |    |           |      |
| tenc |                              |     |    |           |      |
| e_su |                              |     |    |           |      |
| bseq |                              |     |    |           |      |
| uenc |                              |     |    |           |      |
| e_pl |                              |     |    |           |      |
| agia |                              |     |    |           |      |
| rism |                              |     |    |           |      |
| _det |                              |     |    |           |      |
| ecto |                              |     |    |           |      |
| r.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | A convenience function for   | x   | x  | tes       | 3    |
| make | making API requests using    |     |    | ts/test_m |      |
| _url | the urllib library           |     |    | ake_url_r |      |
| _req |                              |     |    | equest.py |      |
| uest |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /mak |                              |     |    |           |      |
| e_ur |                              |     |    |           |      |
| l_re |                              |     |    |           |      |
| ques |                              |     |    |           |      |
| t.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Function to move or rename a | x   | x  |           | 2    |
| move | file which is in a google    |     |    |           |      |
| _or_ | cloud bucket (which includes |     |    |           |      |
| rena | moving it to a different     |     |    |           |      |
| me_f | bucket)                      |     |    |           |      |
| ile_ |                              |     |    |           |      |
| in_g |                              |     |    |           |      |
| clou |                              |     |    |           |      |
| d_bu |                              |     |    |           |      |
| cket |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /mov |                              |     |    |           |      |
| e_or |                              |     |    |           |      |
| _ren |                              |     |    |           |      |
| ame_ |                              |     |    |           |      |
| file |                              |     |    |           |      |
| _in_ |                              |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Prints a progress bar (to    | x   | x  |           | 2    |
| prin | standard out) while code is  |     |    |           |      |
| t_pr | running                      |     |    |           |      |
| ogre |                              |     |    |           |      |
| ss_b |                              |     |    |           |      |
| ar < |                              |     |    |           |      |
| joes |                              |     |    |           |      |
| _gia |                              |     |    |           |      |
| nt_t |                              |     |    |           |      |
| oolb |                              |     |    |           |      |
| ox/p |                              |     |    |           |      |
| rint |                              |     |    |           |      |
| _pro |                              |     |    |           |      |
| gres |                              |     |    |           |      |
| s_ba |                              |     |    |           |      |
| r.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `qu  | Function which runs a query  | x   | x  |           | 4    |
| ery_ | on Google BigQuery and       |     |    |           |      |
| bigq | writes the result into a     |     |    |           |      |
| uery | local pandas.DataFrame       |     |    |           |      |
| _to_ |                              |     |    |           |      |
| pand |                              |     |    |           |      |
| as_d |                              |     |    |           |      |
| f <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/qu |                              |     |    |           |      |
| ery_ |                              |     |    |           |      |
| bigq |                              |     |    |           |      |
| uery |                              |     |    |           |      |
| _to_ |                              |     |    |           |      |
| pand |                              |     |    |           |      |
| as_d |                              |     |    |           |      |
| f.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Class facilitating the ultra | x   |    | t         | 2.5  |
| Rapi | rapid generation of binary   |     |    | ests/test |      |
| dBin | classifier models in         |     |    | _rapid_bi |      |
| aryC | scikit-learn by abstracting  |     |    | nary_clas |      |
| lass | away a lot of the decisions  |     |    | sifier.py |      |
| ifie | and model code               |     |    |           |      |
| r <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/ra |                              |     |    |           |      |
| pid_ |                              |     |    |           |      |
| bina |                              |     |    |           |      |
| ry_c |                              |     |    |           |      |
| lass |                              |     |    |           |      |
| ifie |                              |     |    |           |      |
| r.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `ru  | Convenience function for     | x   | x  |           | 2    |
| n_py | running a python function in |     |    |           |      |
| thon | parallel on multiple cores   |     |    |           |      |
| _fun | or threads                   |     |    |           |      |
| ctio |                              |     |    |           |      |
| n_in |                              |     |    |           |      |
| _par |                              |     |    |           |      |
| alle |                              |     |    |           |      |
| l <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/ru |                              |     |    |           |      |
| n_py |                              |     |    |           |      |
| thon |                              |     |    |           |      |
| _fun |                              |     |    |           |      |
| ctio |                              |     |    |           |      |
| n_in |                              |     |    |           |      |
| _par |                              |     |    |           |      |
| alle |                              |     |    |           |      |
| l.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `scr | Function extracts HTML from  | x   | x  |           | 2    |
| ape_ | given web page, and also     |     |    |           |      |
| webp | follows all of the           |     |    |           |      |
| age_ | hyperlinks on that page and  |     |    |           |      |
| and_ | scrapes those too            |     |    |           |      |
| all_ |                              |     |    |           |      |
| link |                              |     |    |           |      |
| ed_w |                              |     |    |           |      |
| ebpa |                              |     |    |           |      |
| ges  |                              |     |    |           |      |
| <joe |                              |     |    |           |      |
| s_gi |                              |     |    |           |      |
| ant_ |                              |     |    |           |      |
| tool |                              |     |    |           |      |
| box/ |                              |     |    |           |      |
| scra |                              |     |    |           |      |
| pe_w |                              |     |    |           |      |
| ebpa |                              |     |    |           |      |
| ge_a |                              |     |    |           |      |
| nd_a |                              |     |    |           |      |
| ll_l |                              |     |    |           |      |
| inke |                              |     |    |           |      |
| d_we |                              |     |    |           |      |
| page |                              |     |    |           |      |
| s.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | A class for chaining common  |     |    | t         | 2    |
| stri | string-cleaning operations   |     |    | ests/test |      |
| ng_c |                              |     |    | _string_c |      |
| lean |                              |     |    | leaner.py |      |
| er < |                              |     |    |           |      |
| joes |                              |     |    |           |      |
| _gia |                              |     |    |           |      |
| nt_t |                              |     |    |           |      |
| oolb |                              |     |    |           |      |
| ox/s |                              |     |    |           |      |
| trin |                              |     |    |           |      |
| g_cl |                              |     |    |           |      |
| eane |                              |     |    |           |      |
| r.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `up  | Function writes an object in | x   | x  |           | 2    |
| load | python memory to a file      |     |    |           |      |
| _fil | (blob) on a google cloud     |     |    |           |      |
| e_py | bucket                       |     |    |           |      |
| thon |                              |     |    |           |      |
| _to_ |                              |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t <j |                              |     |    |           |      |
| oes_ |                              |     |    |           |      |
| gian |                              |     |    |           |      |
| t_to |                              |     |    |           |      |
| olbo |                              |     |    |           |      |
| x/up |                              |     |    |           |      |
| load |                              |     |    |           |      |
| _fil |                              |     |    |           |      |
| e_py |                              |     |    |           |      |
| thon |                              |     |    |           |      |
| _to_ |                              |     |    |           |      |
| gclo |                              |     |    |           |      |
| ud_b |                              |     |    |           |      |
| ucke |                              |     |    |           |      |
| t.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `ur  | Converts a webpage URL into  | x   |    |           | 2    |
| l_to | a useable filename, where    |     |    |           |      |
| _fil | the URL can be recovered     |     |    |           |      |
| enam | from the filename            |     |    |           |      |
| e_to |                              |     |    |           |      |
| _url |                              |     |    |           |      |
| _map |                              |     |    |           |      |
| per  |                              |     |    |           |      |
| <joe |                              |     |    |           |      |
| s_gi |                              |     |    |           |      |
| ant_ |                              |     |    |           |      |
| tool |                              |     |    |           |      |
| box/ |                              |     |    |           |      |
| url_ |                              |     |    |           |      |
| to_f |                              |     |    |           |      |
| ilen |                              |     |    |           |      |
| ame_ |                              |     |    |           |      |
| to_u |                              |     |    |           |      |
| rl_m |                              |     |    |           |      |
| appe |                              |     |    |           |      |
| r.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Provides a simple printout   | x   |    |           | 2    |
| view | for understanding the        |     |    |           |      |
| _nes | structure of a complex       |     |    |           |      |
| ted_ | nested python dictionary     |     |    |           |      |
| dict |                              |     |    |           |      |
| _str |                              |     |    |           |      |
| uctu |                              |     |    |           |      |
| re < |                              |     |    |           |      |
| joes |                              |     |    |           |      |
| _gia |                              |     |    |           |      |
| nt_t |                              |     |    |           |      |
| oolb |                              |     |    |           |      |
| ox/v |                              |     |    |           |      |
| iew_ |                              |     |    |           |      |
| nest |                              |     |    |           |      |
| ed_d |                              |     |    |           |      |
| ict_ |                              |     |    |           |      |
| stru |                              |     |    |           |      |
| ctur |                              |     |    |           |      |
| e.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+
| `    | Function which writes a      | x   | x  |           | 4    |
| writ | pandas dataframe to a table  |     |    |           |      |
| e_pa | on Google BigQuery           |     |    |           |      |
| ndas |                              |     |    |           |      |
| _df_ |                              |     |    |           |      |
| to_g |                              |     |    |           |      |
| oogl |                              |     |    |           |      |
| e_bi |                              |     |    |           |      |
| gque |                              |     |    |           |      |
| ry_t |                              |     |    |           |      |
| able |                              |     |    |           |      |
|  <jo |                              |     |    |           |      |
| es_g |                              |     |    |           |      |
| iant |                              |     |    |           |      |
| _too |                              |     |    |           |      |
| lbox |                              |     |    |           |      |
| /wri |                              |     |    |           |      |
| te_p |                              |     |    |           |      |
| anda |                              |     |    |           |      |
| s_df |                              |     |    |           |      |
| _to_ |                              |     |    |           |      |
| goog |                              |     |    |           |      |
| le_b |                              |     |    |           |      |
| igqu |                              |     |    |           |      |
| ery_ |                              |     |    |           |      |
| tabl |                              |     |    |           |      |
| e.py |                              |     |    |           |      |
| >`__ |                              |     |    |           |      |
+------+------------------------------+-----+----+-----------+------+

API and Web
-----------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| `an | Function extracts the   | j        | x  | x |         | 2   |
| ony | information (HTML) from | oes_gian |    |   |         |     |
| mou | a public LinkedIn page  | t_toolbo |    |   |         |     |
| s_v | (e.g. person or         | x/anonym |    |   |         |     |
| iew | company) using a        | ous_view |    |   |         |     |
| _pu | virtual browser         | _public_ |    |   |         |     |
| bli |                         | linkedin |    |   |         |     |
| c_l |                         | _page.py |    |   |         |     |
| ink |                         |          |    |   |         |     |
| edi |                         |          |    |   |         |     |
| n_p |                         |          |    |   |         |     |
| age |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| ano |                         |          |    |   |         |     |
| nym |                         |          |    |   |         |     |
| ous |                         |          |    |   |         |     |
| _vi |                         |          |    |   |         |     |
| ew_ |                         |          |    |   |         |     |
| pub |                         |          |    |   |         |     |
| lic |                         |          |    |   |         |     |
| _li |                         |          |    |   |         |     |
| nke |                         |          |    |   |         |     |
| din |                         |          |    |   |         |     |
| _pa |                         |          |    |   |         |     |
| ge. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `d  | Function fetches search | j        | x  | x |         | 2   |
| uck | results from the        | oes_gian |    |   |         |     |
| duc | DuckDuckGo Lite search  | t_toolbo |    |   |         |     |
| kgo | engine                  | x/duckdu |    |   |         |     |
| _se |                         | ckgo_sea |    |   |         |     |
| arc |                         | rch_mult |    |   |         |     |
| h_m |                         | ipage.py |    |   |         |     |
| ult |                         |          |    |   |         |     |
| ipa |                         |          |    |   |         |     |
| ge  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/d |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| duc |                         |          |    |   |         |     |
| kgo |                         |          |    |   |         |     |
| _se |                         |          |    |   |         |     |
| arc |                         |          |    |   |         |     |
| h_m |                         |          |    |   |         |     |
| ult |                         |          |    |   |         |     |
| ipa |                         |          |    |   |         |     |
| ge. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `   | A convenience function  | joes_g   | x  | x | te      | 3   |
| mak | for making API requests | iant_too |    |   | sts/tes |     |
| e_u | using the urllib        | lbox/mak |    |   | t_make_ |     |
| rl_ | library                 | e_url_re |    |   | url_req |     |
| req |                         | quest.py |    |   | uest.py |     |
| ues |                         |          |    |   |         |     |
| t < |                         |          |    |   |         |     |
| joe |                         |          |    |   |         |     |
| s_g |                         |          |    |   |         |     |
| ian |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| ool |                         |          |    |   |         |     |
| box |                         |          |    |   |         |     |
| /ma |                         |          |    |   |         |     |
| ke_ |                         |          |    |   |         |     |
| url |                         |          |    |   |         |     |
| _re |                         |          |    |   |         |     |
| que |                         |          |    |   |         |     |
| st. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `sc | Function extracts HTML  | joe      | x  | x |         | 2   |
| rap | from given web page,    | s_giant_ |    |   |         |     |
| e_w | and also follows all of | toolbox/ |    |   |         |     |
| ebp | the hyperlinks on that  | scrape_w |    |   |         |     |
| age | page and scrapes those  | ebpage_a |    |   |         |     |
| _an | too                     | nd_all_l |    |   |         |     |
| d_a |                         | inked_we |    |   |         |     |
| ll_ |                         | pages.py |    |   |         |     |
| lin |                         |          |    |   |         |     |
| ked |                         |          |    |   |         |     |
| _we |                         |          |    |   |         |     |
| bpa |                         |          |    |   |         |     |
| ges |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| scr |                         |          |    |   |         |     |
| ape |                         |          |    |   |         |     |
| _we |                         |          |    |   |         |     |
| bpa |                         |          |    |   |         |     |
| ge_ |                         |          |    |   |         |     |
| and |                         |          |    |   |         |     |
| _al |                         |          |    |   |         |     |
| l_l |                         |          |    |   |         |     |
| ink |                         |          |    |   |         |     |
| ed_ |                         |          |    |   |         |     |
| web |                         |          |    |   |         |     |
| pag |                         |          |    |   |         |     |
| es. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `ur | Converts a webpage URL  | joe      | x  |   |         | 2   |
| l_t | into a useable          | s_giant_ |    |   |         |     |
| o_f | filename, where the URL | toolbox/ |    |   |         |     |
| ile | can be recovered from   | url_to_f |    |   |         |     |
| nam | the filename            | ilename_ |    |   |         |     |
| e_t |                         | to_url_m |    |   |         |     |
| o_u |                         | apper.py |    |   |         |     |
| rl_ |                         |          |    |   |         |     |
| map |                         |          |    |   |         |     |
| per |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| url |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| _fi |                         |          |    |   |         |     |
| len |                         |          |    |   |         |     |
| ame |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| _ur |                         |          |    |   |         |     |
| l_m |                         |          |    |   |         |     |
| app |                         |          |    |   |         |     |
| er. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Data Visualisation
------------------

+-------+-------------------------+------------+----+---+---------+---+
| Name  | Description             | Location   | Co | D | Tests   | C |
|       |                         |            | de | o |         | o |
|       |                         |            | C  | c |         | n |
|       |                         |            | om | u |         | f |
|       |                         |            | pl | m |         | i |
|       |                         |            | et | e |         | d |
|       |                         |            | ed | n |         | e |
|       |                         |            |    | t |         | n |
|       |                         |            |    | a |         | c |
|       |                         |            |    | t |         | e |
|       |                         |            |    | i |         | S |
|       |                         |            |    | o |         | c |
|       |                         |            |    | n |         | o |
|       |                         |            |    | C |         | r |
|       |                         |            |    | o |         | e |
|       |                         |            |    | m |         |   |
|       |                         |            |    | p |         |   |
|       |                         |            |    | l |         |   |
|       |                         |            |    | e |         |   |
|       |                         |            |    | t |         |   |
|       |                         |            |    | e |         |   |
|       |                         |            |    | d |         |   |
+=======+=========================+============+====+===+=========+===+
| asc   | A function which draws  | joes_      | x  | x |         | 2 |
| ii_de | a histogram using only  | giant_tool |    |   |         |   |
| nsity | raw text symbols        | box/ascii_ |    |   |         |   |
| _hist |                         | density_hi |    |   |         |   |
| ogram |                         | stogram.py |    |   |         |   |
+-------+-------------------------+------------+----+---+---------+---+
| v     | Provides a simple       | joes_gia   | x  |   |         | 2 |
| iew_n | printout for            | nt_toolbox |    |   |         |   |
| ested | understanding the       | /view_nest |    |   |         |   |
| _dict | structure of a complex  | ed_dict_st |    |   |         |   |
| _stru | nested python           | ructure.py |    |   |         |   |
| cture | dictionary              |            |    |   |         |   |
+-------+-------------------------+------------+----+---+---------+---+

Google Cloud
------------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| `   | Function to delete a    | jo       | x  | x |         | 4   |
| del | file which is in a      | es_giant |    |   |         |     |
| ete | google cloud bucket     | _toolbox |    |   |         |     |
| _fi |                         | /delete_ |    |   |         |     |
| le_ |                         | file_in_ |    |   |         |     |
| in_ |                         | gcloud_b |    |   |         |     |
| gcl |                         | ucket.py |    |   |         |     |
| oud |                         |          |    |   |         |     |
| _bu |                         |          |    |   |         |     |
| cke |                         |          |    |   |         |     |
| t < |                         |          |    |   |         |     |
| joe |                         |          |    |   |         |     |
| s_g |                         |          |    |   |         |     |
| ian |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| ool |                         |          |    |   |         |     |
| box |                         |          |    |   |         |     |
| /de |                         |          |    |   |         |     |
| let |                         |          |    |   |         |     |
| e_f |                         |          |    |   |         |     |
| ile |                         |          |    |   |         |     |
| _in |                         |          |    |   |         |     |
| _gc |                         |          |    |   |         |     |
| lou |                         |          |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `d  | Function which reads a  | joes_gia | x  | x |         | 4   |
| own | file from a google      | nt_toolb |    |   |         |     |
| loa | cloud bucket into       | ox/downl |    |   |         |     |
| d_f | python memory           | oad_file |    |   |         |     |
| ile |                         | _from_gc |    |   |         |     |
| _fr |                         | loud_buc |    |   |         |     |
| om_ |                         | ket_to_p |    |   |         |     |
| gcl |                         | ython.py |    |   |         |     |
| oud |                         |          |    |   |         |     |
| _bu |                         |          |    |   |         |     |
| cke |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| o_p |                         |          |    |   |         |     |
| yth |                         |          |    |   |         |     |
| on  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/d |                         |          |    |   |         |     |
| own |                         |          |    |   |         |     |
| loa |                         |          |    |   |         |     |
| d_f |                         |          |    |   |         |     |
| ile |                         |          |    |   |         |     |
| _fr |                         |          |    |   |         |     |
| om_ |                         |          |    |   |         |     |
| gcl |                         |          |    |   |         |     |
| oud |                         |          |    |   |         |     |
| _bu |                         |          |    |   |         |     |
| cke |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| o_p |                         |          |    |   |         |     |
| yth |                         |          |    |   |         |     |
| on. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `l  | Function which returns  | j        | x  | x |         | 4   |
| ist | a list of the files     | oes_gian |    |   |         |     |
| _fi | present in a specified  | t_toolbo |    |   |         |     |
| les | google cloud bucket     | x/list_f |    |   |         |     |
| _in |                         | iles_in_ |    |   |         |     |
| _gc |                         | gcloud_b |    |   |         |     |
| lou |                         | ucket.py |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/l |                         |          |    |   |         |     |
| ist |                         |          |    |   |         |     |
| _fi |                         |          |    |   |         |     |
| les |                         |          |    |   |         |     |
| _in |                         |          |    |   |         |     |
| _gc |                         |          |    |   |         |     |
| lou |                         |          |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `m  | Function to move or     | jo       | x  | x |         | 2   |
| ove | rename a file which is  | es_giant |    |   |         |     |
| _or | in a google cloud       | _toolbox |    |   |         |     |
| _re | bucket (which includes  | /move_or |    |   |         |     |
| nam | moving it to a          | _rename_ |    |   |         |     |
| e_f | different bucket)       | file_in_ |    |   |         |     |
| ile |                         | gcloud_b |    |   |         |     |
| _in |                         | ucket.py |    |   |         |     |
| _gc |                         |          |    |   |         |     |
| lou |                         |          |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/m |                         |          |    |   |         |     |
| ove |                         |          |    |   |         |     |
| _or |                         |          |    |   |         |     |
| _re |                         |          |    |   |         |     |
| nam |                         |          |    |   |         |     |
| e_f |                         |          |    |   |         |     |
| ile |                         |          |    |   |         |     |
| _in |                         |          |    |   |         |     |
| _gc |                         |          |    |   |         |     |
| lou |                         |          |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `q  | Function which runs a   | j        | x  | x |         | 4   |
| uer | query on Google         | oes_gian |    |   |         |     |
| y_b | BigQuery and writes the | t_toolbo |    |   |         |     |
| igq | result into a local     | x/query_ |    |   |         |     |
| uer | pandas.DataFrame        | bigquery |    |   |         |     |
| y_t |                         | _to_pand |    |   |         |     |
| o_p |                         | as_df.py |    |   |         |     |
| and |                         |          |    |   |         |     |
| as_ |                         |          |    |   |         |     |
| df  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/q |                         |          |    |   |         |     |
| uer |                         |          |    |   |         |     |
| y_b |                         |          |    |   |         |     |
| igq |                         |          |    |   |         |     |
| uer |                         |          |    |   |         |     |
| y_t |                         |          |    |   |         |     |
| o_p |                         |          |    |   |         |     |
| and |                         |          |    |   |         |     |
| as_ |                         |          |    |   |         |     |
| df. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `up | Function writes an      | j        | x  | x |         | 2   |
| loa | object in python memory | oes_gian |    |   |         |     |
| d_f | to a file (blob) on a   | t_toolbo |    |   |         |     |
| ile | google cloud bucket     | x/upload |    |   |         |     |
| _py |                         | _file_py |    |   |         |     |
| tho |                         | thon_to_ |    |   |         |     |
| n_t |                         | gcloud_b |    |   |         |     |
| o_g |                         | ucket.py |    |   |         |     |
| clo |                         |          |    |   |         |     |
| ud_ |                         |          |    |   |         |     |
| buc |                         |          |    |   |         |     |
| ket |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| upl |                         |          |    |   |         |     |
| oad |                         |          |    |   |         |     |
| _fi |                         |          |    |   |         |     |
| le_ |                         |          |    |   |         |     |
| pyt |                         |          |    |   |         |     |
| hon |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| _gc |                         |          |    |   |         |     |
| lou |                         |          |    |   |         |     |
| d_b |                         |          |    |   |         |     |
| uck |                         |          |    |   |         |     |
| et. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `   | Function which writes a | joes_g   | x  | x |         | 4   |
| wri | pandas dataframe to a   | iant_too |    |   |         |     |
| te_ | table on Google         | lbox/wri |    |   |         |     |
| pan | BigQuery                | te_panda |    |   |         |     |
| das |                         | s_df_to_ |    |   |         |     |
| _df |                         | google_b |    |   |         |     |
| _to |                         | igquery_ |    |   |         |     |
| _go |                         | table.py |    |   |         |     |
| ogl |                         |          |    |   |         |     |
| e_b |                         |          |    |   |         |     |
| igq |                         |          |    |   |         |     |
| uer |                         |          |    |   |         |     |
| y_t |                         |          |    |   |         |     |
| abl |                         |          |    |   |         |     |
| e < |                         |          |    |   |         |     |
| joe |                         |          |    |   |         |     |
| s_g |                         |          |    |   |         |     |
| ian |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| ool |                         |          |    |   |         |     |
| box |                         |          |    |   |         |     |
| /wr |                         |          |    |   |         |     |
| ite |                         |          |    |   |         |     |
| _pa |                         |          |    |   |         |     |
| nda |                         |          |    |   |         |     |
| s_d |                         |          |    |   |         |     |
| f_t |                         |          |    |   |         |     |
| o_g |                         |          |    |   |         |     |
| oog |                         |          |    |   |         |     |
| le_ |                         |          |    |   |         |     |
| big |                         |          |    |   |         |     |
| que |                         |          |    |   |         |     |
| ry_ |                         |          |    |   |         |     |
| tab |                         |          |    |   |         |     |
| le. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Project Management
------------------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| `c  | Creates a basic project | joes_g   | x  |   |         | 2   |
| rea | scope document          | iant_too |    |   |         |     |
| te_ | (markdown) using user   | lbox/cre |    |   |         |     |
| pro | input prompts           | ate_proj |    |   |         |     |
| jec |                         | ect_scop |    |   |         |     |
| t_s |                         | e_doc.py |    |   |         |     |
| cop |                         |          |    |   |         |     |
| e_d |                         |          |    |   |         |     |
| oc  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/c |                         |          |    |   |         |     |
| rea |                         |          |    |   |         |     |
| te_ |                         |          |    |   |         |     |
| pro |                         |          |    |   |         |     |
| jec |                         |          |    |   |         |     |
| t_s |                         |          |    |   |         |     |
| cop |                         |          |    |   |         |     |
| e_d |                         |          |    |   |         |     |
| oc. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Python Convenience Functions
----------------------------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| `li | Searches every python   | joes_    | x  | x |         | 2   |
| st_ | script in a given       | giant_to |    |   |         |     |
| all | folder and lists all    | olbox/li |    |   |         |     |
| _py | python modules imported | st_all_p |    |   |         |     |
| tho | within those scripts    | ython_im |    |   |         |     |
| n_i |                         | ports.py |    |   |         |     |
| mpo |                         |          |    |   |         |     |
| rts |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| lis |                         |          |    |   |         |     |
| t_a |                         |          |    |   |         |     |
| ll_ |                         |          |    |   |         |     |
| pyt |                         |          |    |   |         |     |
| hon |                         |          |    |   |         |     |
| _im |                         |          |    |   |         |     |
| por |                         |          |    |   |         |     |
| ts. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `p  | Prints a progress bar   | joes_gia | x  | x |         | 2   |
| rin | (to standard out) while | nt_toolb |    |   |         |     |
| t_p | code is running         | ox/print |    |   |         |     |
| rog |                         | _progres |    |   |         |     |
| res |                         | s_bar.py |    |   |         |     |
| s_b |                         |          |    |   |         |     |
| ar  |                         |          |    |   |         |     |
| <jo |                         |          |    |   |         |     |
| es_ |                         |          |    |   |         |     |
| gia |                         |          |    |   |         |     |
| nt_ |                         |          |    |   |         |     |
| too |                         |          |    |   |         |     |
| lbo |                         |          |    |   |         |     |
| x/p |                         |          |    |   |         |     |
| rin |                         |          |    |   |         |     |
| t_p |                         |          |    |   |         |     |
| rog |                         |          |    |   |         |     |
| res |                         |          |    |   |         |     |
| s_b |                         |          |    |   |         |     |
| ar. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+
| `   | Convenience function    | joes_    | x  | x |         | 2   |
| run | for running a python    | giant_to |    |   |         |     |
| _py | function in parallel on | olbox/ru |    |   |         |     |
| tho | multiple cores or       | n_python |    |   |         |     |
| n_f | threads                 | _functio |    |   |         |     |
| unc |                         | n_in_par |    |   |         |     |
| tio |                         | allel.py |    |   |         |     |
| n_i |                         |          |    |   |         |     |
| n_p |                         |          |    |   |         |     |
| ara |                         |          |    |   |         |     |
| lle |                         |          |    |   |         |     |
| l < |                         |          |    |   |         |     |
| joe |                         |          |    |   |         |     |
| s_g |                         |          |    |   |         |     |
| ian |                         |          |    |   |         |     |
| t_t |                         |          |    |   |         |     |
| ool |                         |          |    |   |         |     |
| box |                         |          |    |   |         |     |
| /ru |                         |          |    |   |         |     |
| n_p |                         |          |    |   |         |     |
| yth |                         |          |    |   |         |     |
| on_ |                         |          |    |   |         |     |
| fun |                         |          |    |   |         |     |
| cti |                         |          |    |   |         |     |
| on_ |                         |          |    |   |         |     |
| in_ |                         |          |    |   |         |     |
| par |                         |          |    |   |         |     |
| all |                         |          |    |   |         |     |
| el. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Statistical Inference and Hypothesis Testing
--------------------------------------------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| co  | Function which          | joe      | x  | x | t       | 4   |
| nju | calculates the          | s_giant_ |    |   | ests/te |     |
| gat | posterior distribution  | toolbox/ |    |   | st_conj |     |
| e_p | of the success          | conjugat |    |   | ugate_p |     |
| rio | probability parameter   | e_prior_ |    |   | rior_be |     |
| r_b | [p] of a binomial       | beta_bin |    |   | ta_bino |     |
| eta | distribution, from      | omial.py |    |   | mial.py |     |
| _bi | observed data and a     |          |    |   |         |     |
| nom | user-specified beta     |          |    |   |         |     |
| ial | prior                   |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Statistical Modelling and Machine Learning
------------------------------------------

+-----+-------------------------+----------+----+---+---------+-----+
| N   | Description             | Location | Co | D | Tests   | C   |
| ame |                         |          | de | o |         | onf |
|     |                         |          | C  | c |         | ide |
|     |                         |          | om | u |         | nce |
|     |                         |          | pl | m |         | Sc  |
|     |                         |          | et | e |         | ore |
|     |                         |          | ed | n |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | a |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | i |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | n |         |     |
|     |                         |          |    | C |         |     |
|     |                         |          |    | o |         |     |
|     |                         |          |    | m |         |     |
|     |                         |          |    | p |         |     |
|     |                         |          |    | l |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | t |         |     |
|     |                         |          |    | e |         |     |
|     |                         |          |    | d |         |     |
+=====+=========================+==========+====+===+=========+=====+
| `   | Class facilitating the  | joes_    | x  |   | te      | 2.5 |
| Rap | ultra rapid generation  | giant_to |    |   | sts/tes |     |
| idB | of binary classifier    | olbox/ra |    |   | t_rapid |     |
| ina | models in scikit-learn  | pid_bina |    |   | _binary |     |
| ryC | by abstracting away a   | ry_class |    |   | _classi |     |
| las | lot of the decisions    | ifier.py |    |   | fier.py |     |
| sif | and model code          |          |    |   |         |     |
| ier |                         |          |    |   |         |     |
|  <j |                         |          |    |   |         |     |
| oes |                         |          |    |   |         |     |
| _gi |                         |          |    |   |         |     |
| ant |                         |          |    |   |         |     |
| _to |                         |          |    |   |         |     |
| olb |                         |          |    |   |         |     |
| ox/ |                         |          |    |   |         |     |
| rap |                         |          |    |   |         |     |
| id_ |                         |          |    |   |         |     |
| bin |                         |          |    |   |         |     |
| ary |                         |          |    |   |         |     |
| _cl |                         |          |    |   |         |     |
| ass |                         |          |    |   |         |     |
| ifi |                         |          |    |   |         |     |
| er. |                         |          |    |   |         |     |
| py> |                         |          |    |   |         |     |
| `__ |                         |          |    |   |         |     |
+-----+-------------------------+----------+----+---+---------+-----+

Text and Natural Language Processing
------------------------------------

+-----+----------------------------+-----------+-----+---+----------+
| N   | Description                | Code      | D   | T | Co       |
| ame |                            | Completed | ocu | e | nfidence |
|     |                            |           | men | s | Score    |
|     |                            |           | tat | t |          |
|     |                            |           | ion | s |          |
|     |                            |           | Com |   |          |
|     |                            |           | ple |   |          |
|     |                            |           | ted |   |          |
+=====+============================+===========+=====+===+==========+
| `l  | Finds phrases (sequences   | x         | x   | t | 3        |
| ong | of consecutive words)      |           |     | e |          |
| est | common to 2 documents      |           |     | s |          |
| _se | (e.g. to act as a naive    |           |     | t |          |
| nte | plagiarism detector)       |           |     | s |          |
| nce |                            |           |     | / |          |
| _su |                            |           |     | t |          |
| bse |                            |           |     | e |          |
| que |                            |           |     | s |          |
| nce |                            |           |     | t |          |
| _pl |                            |           |     | _ |          |
| agi |                            |           |     | l |          |
| ari |                            |           |     | o |          |
| sm_ |                            |           |     | n |          |
| det |                            |           |     | g |          |
| ect |                            |           |     | e |          |
| or  |                            |           |     | s |          |
| <jo |                            |           |     | t |          |
| es_ |                            |           |     | _ |          |
| gia |                            |           |     | s |          |
| nt_ |                            |           |     | e |          |
| too |                            |           |     | n |          |
| lbo |                            |           |     | t |          |
| x/l |                            |           |     | e |          |
| ong |                            |           |     | n |          |
| est |                            |           |     | c |          |
| _se |                            |           |     | e |          |
| nte |                            |           |     | _ |          |
| nce |                            |           |     | s |          |
| _su |                            |           |     | u |          |
| bse |                            |           |     | b |          |
| que |                            |           |     | s |          |
| nce |                            |           |     | e |          |
| _pl |                            |           |     | q |          |
| agi |                            |           |     | u |          |
| ari |                            |           |     | e |          |
| sm_ |                            |           |     | n |          |
| det |                            |           |     | c |          |
| ect |                            |           |     | e |          |
| or. |                            |           |     | _ |          |
| py> |                            |           |     | p |          |
| `__ |                            |           |     | l |          |
|     |                            |           |     | a |          |
|     |                            |           |     | g |          |
|     |                            |           |     | i |          |
|     |                            |           |     | a |          |
|     |                            |           |     | r |          |
|     |                            |           |     | i |          |
|     |                            |           |     | s |          |
|     |                            |           |     | m |          |
|     |                            |           |     | _ |          |
|     |                            |           |     | d |          |
|     |                            |           |     | e |          |
|     |                            |           |     | t |          |
|     |                            |           |     | e |          |
|     |                            |           |     | c |          |
|     |                            |           |     | t |          |
|     |                            |           |     | o |          |
|     |                            |           |     | r |          |
|     |                            |           |     | . |          |
|     |                            |           |     | p |          |
|     |                            |           |     | y |          |
+-----+----------------------------+-----------+-----+---+----------+
| `S  | A class for chaining       |           |     |   | 2        |
| tri | common string-cleaning     |           |     |   |          |
| ngC | operations                 |           |     |   |          |
| lea |                            |           |     |   |          |
| ner |                            |           |     |   |          |
|  <j |                            |           |     |   |          |
| oes |                            |           |     |   |          |
| _gi |                            |           |     |   |          |
| ant |                            |           |     |   |          |
| _to |                            |           |     |   |          |
| olb |                            |           |     |   |          |
| ox/ |                            |           |     |   |          |
| str |                            |           |     |   |          |
| ing |                            |           |     |   |          |
| _cl |                            |           |     |   |          |
| ean |                            |           |     |   |          |
| er. |                            |           |     |   |          |
| py> |                            |           |     |   |          |
| `__ |                            |           |     |   |          |
+-----+----------------------------+-----------+-----+---+----------+

Run Unit Tests
==============

.. code:: bash

   pip install pytest
   pytest -v
