# -*- coding: utf-8 -*-
from mathematics import *
from setting import *

import numpy as np

def generate_collaborative_matrix(df):
	return df.rdd.map(lambda row: {
		"id": row.product_id,
		"array": np.array(row[1:]),
		"norm": np.linalg.norm(np.array(row[1:]))
	})


def get_most_similars(product_id, collaborative_rdd):
	const_prod = collaborative_rdd.filter(lambda x: x['id'] == product_id).first()
	return collaborative_rdd.map(
		lambda x: (get_cosine_similarity(x, const_prod), x['id'])
	).sortBy(lambda y: -y[0]).take(NUM_RECS + 1)