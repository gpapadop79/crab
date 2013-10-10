"""
Metrics module with score  functions, performance metrics and
pairwise metrics or distances computation
"""

from scikits.crab.metrics.pairwise import cosine_distances, euclidean_distances, pearson_correlation, \
    jaccard_coefficient, loglikehood_coefficient, manhattan_distances, \
     sorensen_coefficient, spearman_coefficient
from scikits.crab.metrics.cross_validation import LeaveOneOut, LeavePOut, KFold, ShuffleSplit
from scikits.crab.metrics.sampling import SplitSampling

