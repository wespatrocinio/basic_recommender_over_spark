# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def get_array_norm(array):
	return np.linalg.norm(array)

def get_dot_product(array1, array2):
	return np.dot(array1, array2)

def get_cosine_similarity(array1, array2):
	return get_dot_product(array1, array2) / (get_array_norm(array1) * get_array_norm(array2))