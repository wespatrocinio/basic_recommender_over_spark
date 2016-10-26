# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def get_array_norm(array):
	return np.linalg.norm(array)

def get_dot_product(array1, array2):
	return np.dot(array1, array2)

def get_cosine_similarity(product_1, product_2):
	sim = get_dot_product(product_1['array'], product_2['array']) / (product_1['norm'] * product_2['norm'])
	#return {"id": product_2['id'], "similarity": sim}
	return sim

def get_similarities(product, products_rdd):
	return products_rdd.foreach(lambda x: get_cosine_similarity(product, x)).collect()