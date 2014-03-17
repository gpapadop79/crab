import time
import shelve

from utils import *

s = shelve.open('data.shelve')
train_data_points = s['train_data_points']
test_data_points = s['test_data_points']
model = data_points_to_crab_model(train_data_points)

from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
similarity = UserSimilarity(model, pearson_correlation, 5)
from scikits.crab.recommenders.knn import UserBasedRecommender

recommender = UserBasedRecommender(model, similarity, with_preference=True)
e = evaluate(recommender, test_data_points[:10], activation_function=trivial_activation, return_data_points=True)

s['evaluation'] = e
s.close()
