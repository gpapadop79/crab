## Example 01: Training a user-based collaborative filtering recommender


from scikits.crab import datasets

movies = datasets.load_sample_movies()
songs = datasets.load_sample_songs()

from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender

# Load data model
model = MatrixPreferenceDataModel(movies.data)
# Calculate similarity
similarity = UserSimilarity(model, pearson_correlation)
# Load Memory-based 
recommender = UserBasedRecommender(model, similarity, with_preference=True)
recs = recommender.recommend(5)