# -*- coding: utf-8 -*-
from pyspark.mllib.linalg.distributed import CoordinateMatrix, MatrixEntry

def aggregate_count_by_user_id(df):
	return df.groupBy('product_id', 'user_id').count()

def generate_collaborative_matrix(df):
	df_pvt = df.groupBy('product_id').pivot('product_id').sum('count')
