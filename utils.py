import pandas as pd
import numpy as np

def split_data_points(data_points, n_train):
    # data_points: [(u1, i1, r1), (u2, i2, r2), ...]
    import random
    import copy
    _data_points = copy.deepcopy(data_points)
    # shuffle is an in-place operation
    random.shuffle(_data_points)
    train_data_points = _data_points[:n_train]
    test_data_points = _data_points[n_train:]
    return train_data_points, test_data_points

def data_points_to_crab_model(data_points):
    from scikits.crab.models import MatrixPreferenceDataModel
    from collections import defaultdict
    data = defaultdict(dict)
    for (u, i, r) in data_points:
        data[u][i] = r
    model = MatrixPreferenceDataModel(data)
    return model

def predict(recommender, data_points):
    return np.array([recommender.estimate_preference(u, i) for (u, i) in data_points])

def trivial_activation(x):
    if x > 0.2:
        return 1
    elif x < -0.2:
        return -1
    else:
        return 0

def identity_activation(x):
    return x

def evaluate(recommender,
             test_data_points,
             activation_function=identity_activation,
             return_data_points=False):
    # test_data_points: [(u1, i1, r1), (u2, i2, r2), ...]
    r_predict = predict(recommender, [(u, i) for (u, i, r) in test_data_points])
    v_activation_function = np.vectorize(activation_function)
    r_predict_activated = v_activation_function(r_predict)
    r_real = np.array(zip(*test_data_points)[2])
    evaluation = {}
    if return_data_points:
        evaluation['test_data_points_with_prediction'] = \
            pd.DataFrame([(d[0], d[1], rr, rp, rpa)
                          for (d, rr, rp, rpa) in
                          zip(test_data_points, r_real, r_predict, r_predict_activated)],
                         columns = ['user', 'item', 'r_real', 'r_predict', 'r_predict_activated'])
        evaluation['test_data_points_with_prediction'] = evaluation['test_data_points_with_prediction'].to_dict()
    evaluation['n_test_data_points'] = len(test_data_points)
    evaluation['se'] = float(np.sum((r_predict_activated - r_real) ** 2))
    evaluation['mse'] = evaluation['se'] / len(test_data_points)
    evaluation['rmse'] = np.sqrt(evaluation['mse'])
    # This should not be part of evaluation function
    # Put it here for smoking test regarding preferences_from_user()
    evaluation['LEE Cheuk-yan'] = set(recommender.model.preferences_from_user('LEE Cheuk-yan'))
    return evaluation
