from scikits.crab.datasets import load_sample_movies
movies = load_sample_movies()

from scikits.crab.models import MatrixPreferenceDataModel
model = MatrixPreferenceDataModel(movies.data)

from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
similarity = UserSimilarity(model, pearson_correlation)

from scikits.crab.recommenders.knn import UserBasedRecommender
recommender = UserBasedRecommender(model, similarity, with_preference=True)
print recommender.recommend(5)
