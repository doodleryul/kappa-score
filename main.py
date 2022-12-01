import numpy as np
from sklearn.metrics import confusion_matrix
from typing import Optional, Union, List


def calculate_kappa_score(pred: Union[List, np.array], label: Union[List, np.array], weight: Optional[str] = None):
    assert weight in ['linear', 'quadratic', None], 'Not supported weight in kappa score'

    cf = confusion_matrix(label, pred)
    W = _calculate_weight(cf, weight)

    total_num = np.sum(cf)
    P_j = (np.sum(cf, axis=1)/total_num).reshape(3,1)
    P_i = (np.sum(cf, axis=0)/total_num).reshape(1,3)

    p_e = np.sum(W*np.matmul(P_j, P_i))
    p_o = np.sum(W*cf/total_num)
    score = (p_o-p_e)/(1-p_e)
    return score


def _calculate_weight(cf: np.array, weight: Optional[str]) -> np.array:
    class_num = len(cf)
    if weight:
        R = class_num
        I = np.array([list(range(1,R+1))]*len(cf))
        J = I.T

        if weight == 'linear':
            return 1 - abs(I-J)/(R-1)
        elif weight == 'quadratic':
            return 1 - (I-J)*(I-J)/((R-1)*(R-1))
    else:
        return np.identity(class_num)
