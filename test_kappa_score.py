from .main import calculate_kappa_score
from math import isclose


def test_calculate_kappa_score():
    pred = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
    label = [0, 0, 1, 2, 0, 1, 0, 0, 1, 2]

    k_score = calculate_kappa_score(pred, label)
    linear_k_score = calculate_kappa_score(pred, label, 'linear')
    quad_k_score = calculate_kappa_score(pred, label, 'quadratic')

    assert isclose(k_score, 0.11764705882352945)
    assert isclose(linear_k_score, 0.14893617021276587)
    assert isclose(quad_k_score, 0.17808219178082207)
