# -*- coding: utf-8 -*-
def aggregate_count_by_user_id(df):
	return df.groupBy('product_id', 'user_id').count()

def generate_collaborative_matrix(df):
	return df.groupBy('product_id').pivot('product_id').sum('count').fillna(0)

def join_pair(pair):
    return dict(pair[0].asDict().items() + [("array", pair[1])])

def add_products_arrays(df):
	products_cols = df.columns
	products_cols.remove('product_id')
	df_array = df.select('product_id').rdd.zip(products_arrays.rdd).map(join_pair).toDF()
