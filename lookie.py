import numpy as np
from source.data_utils import npz_to_dict

dataset = dict(np.load('./data/deepwriting_validation.npz'))
print(dataset['texts'])
