# This code depicts the snippets appeared in Chapter 2 of the Crab's Official Tutorial:
# 
#   http://muricoca.github.io/crab/tutorial.html#introducing-recommendation-engines
#

import sys

from scikits.crab import datasets
from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender

# input
movies = datasets.load_sample_movies()
print movies.data

# build the model
model = MatrixPreferenceDataModel(movies.data)
print model

# build the similarity
similarity = UserSimilarity(model, pearson_correlation)

# build the user based recommender
recommender = UserBasedRecommender(model, similarity, with_preference=True)

# recommend items for the user 5
result = recommender.recommend(5)
print result