# Crab - A Recommendation Engine library for Python

  Crab is a ﬂexible, fast recommender engine for Python that integrates classic information ﬁltering recom-
  mendation algorithms in the world of scientiﬁc Python packages (numpy, scipy, matplotlib). The engine aims
  to provide a rich set of components from which you can construct a customized recommender system from a
  set of algorithms.
  
  This is an experimental fork (started in March 2016) that attempts to merge a number of fixes done over the past 2 years in order to get a working recommender library.

  In the code merged into this fork, @gabrielspmoreira did the following changes:
  * Fixed some issues for compatibility with scikit.learn last version (BaseEstimator class deprecated import (scikits.learn.base) and _set_param renamed method)
  * Implemented a hybrid method to combine Collaborative Filtering with Global Baseline estimates (based on users and items average preference), inspired on [Implementing Collaborative Filtering class](https://class.coursera.org/mmds-001/lecture/95) from [Coursera Mining Massive Datasets course](https://www.coursera.org/course/mmds).

## Usage

```python
from scikits.crab import datasets
movies = datasets.load_sample_movies()
songs = datasets.load_sample_songs()

from scikits.crab.models import MatrixPreferenceDataModel
model = MatrixPreferenceDataModel(movies.data)

from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
similarity = UserSimilarity(model, pearson_correlation)

from scikits.crab.recommenders.knn import UserBasedRecommender

recommender = UserBasedRecommender(model, similarity, with_preference=True)

recommender.recommend(5)
```

  For further usage and Instructions checkout the [Crab Wiki](https://github.com/muricoca/crab/wiki)

## History

  The project was started in 2010  by Marcel Caraciolo as a M.S.C related  project, and since then many people interested joined to help in the project.
  It is currently maintained by a team of volunteers, members of the Muriçoca Labs.

## Original Authors
  
  Marcel Caraciolo (marcel@muricoca.com)

  Bruno Melo (bruno@muricoca.com)

  Ricardo Caspirro (ricardo@muricoca.com)

  Rodrigo Alves (rodrigo@muricoca.com)

## Bugs, Feedback

  Please submit bugs you might encounter, as well Patches and Features Requests to the [Issues Tracker](https://github.com/muricoca/crab/issues) located at GitHub.

## Contributions

  If you want to submit a patch to this project, it is AWESOME. Follow this guide:

  * Fork Crab
  * Make your alterations and commit
  * Create a topic branch - git checkout -b my_branch
  * Push to your branch - git push origin my_branch
  * Create a [Pull Request](http://help.github.com/pull-requests/) from your branch.
  * You just contributed to the Crab project!

## Wiki

Please check our [Wiki](https://github.com/muricoca/crab/wiki "Crab Wiki") wiki, for further information on how to start developing or use Crab in your projects.


## Benchmarking notes from @hupili:

I was preparing a [tutorial about RecSys](https://course.ie.cuhk.edu.hk/~engg4030/tutorial/tutorial9/).
After some search, it seems that `crab` is the most commonly used.
When running it on my data set (LegCoHK), the prediction of neighbourhood model is extremely slow.
Then I did some optimization to speed up by 30x.

Feel free to use this fork **at your own risk**.
The best way to checkout what I did is to follow the commits.
Profile data and codes are checked in simultaneous.

Quick notes are followed.

[![Analytics](https://ga-beacon.appspot.com/UA-37311363-6/hupili/default)](https://github.com/igrigorik/ga-beacon)

```
$python benchmark.py
Time spent for training: 7.86781311035e-06
Time spent for testing: 10.1878209114
```

The profiling result:

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 2882    5.694    0.002    6.451    0.002 scikits/crab/models/classes.py:175(preferences_from_user)
 1096    1.556    0.001    2.656    0.002 scikits/crab/similarities/basic_similarities.py:16(find_common_elements)
 4008    0.705    0.000    0.705    0.000 {zip}
 1096    0.429    0.000    8.201    0.007 scikits/crab/similarities/basic_similarities.py:99(get_similarity)
 2206    0.361    0.000    0.362    0.000 {sorted}
    1    0.309    0.309    2.824    2.824 /usr/local/Cellar/python/2.7.6/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pandas/__init__.py:3(<module>)
11419    0.308    0.000    0.308    0.000 {numpy.core.multiarray.array}
 1099    0.262    0.000    0.262    0.000 {method 'sort' of 'numpy.ndarray' objects}
```

Profile: (see this commit)

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1096    2.329    0.002    3.320    0.003 basic_similarities.py:16(find_common_elements)
     2206    0.357    0.000    0.358    0.000 {sorted}
     1099    0.254    0.000    0.254    0.000 {method 'sort' of 'numpy.ndarray' objects}
    11387    0.231    0.000    0.231    0.000 {numpy.core.multiarray.array}
        3    0.136    0.045    0.252    0.084 shelve.py:117(__getitem__)
```

Profile: (see this commit)

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    11387    0.178    0.000    0.178    0.000 {numpy.core.multiarray.array}
     1096    0.154    0.000    0.520    0.000 basic_similarities.py:99(get_similarity)
        3    0.114    0.038    0.114    0.038 {built-in method load}
        3    0.080    0.027    0.194    0.065 shelve.py:117(__getitem__)
        1    0.059    0.059    0.087    0.087 classes.py:100(build_model)
     1096    0.051    0.000    0.170    0.000 distance.py:1712(cdist)
```

Enlarge test data set: (see this commit)

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   109637    2.010    0.000    2.010    0.000 {numpy.core.multiarray.array}
    10885    1.709    0.000    5.668    0.001 basic_similarities.py:99(get_similarity)
    10885    0.523    0.000    1.721    0.000 distance.py:1712(cdist)
    44040    0.330    0.000    0.330    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    21770    0.231    0.000    0.512    0.000 _methods.py:49(_mean)
```

Add similarity cache:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    59237    1.015    0.000    1.015    0.000 {numpy.core.multiarray.array}
    10885    0.888    0.000    2.933    0.000 basic_similarities.py:100(get_similarity)
     5845    0.278    0.000    0.916    0.000 distance.py:1712(cdist)
     6901    0.178    0.000    0.191    0.000 classes.py:162(preference_values_from_user)
    23880    0.176    0.000    0.176    0.000 {method 'reduce' of 'numpy.ufunc' objects}
```

Tune common elements lookup:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10885    0.522    0.000    3.191    0.000 basic_similarities.py:100(get_similarity)
    47547    0.454    0.000    0.454    0.000 {numpy.core.multiarray.array}
    11690    0.440    0.000    1.161    0.000 {numpy.core.multiarray.fromiter}
  1884189    0.377    0.000    0.377    0.000 basic_similarities.py:126(<genexpr>)
  1884189    0.347    0.000    0.347    0.000 basic_similarities.py:125(<genexpr>)
     5845    0.286    0.000    0.930    0.000 distance.py:1712(cdist)
     6901    0.182    0.000    0.195    0.000 classes.py:162(preference_values_from_user)
```

## LICENCE (BSD)

Copyright (c) 2011, Muriçoca Labs

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Muriçoca Labs nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL MURIÇOCA LABS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

