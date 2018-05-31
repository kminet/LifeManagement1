import numpy as np
score = np.loadtxt('python_score.csv', delimiter=',', dtype='float64')
dset = score[:22,:10].T
dset
answer = score[:,10]
answer
bool_dset = (dset == answer)
bool_dset
bool_dset = bool_dset * 1
bool_dset
bool_dset[:,20:] = dset[:,20:]
b = np.ones(22)
b[:20] *= 4
b
np.dot(bool_dset,b)