# -*- coding: utf-8 -*-
def aggregate_count_by_user_id(df):
	return df.groupBy('product_id', 'user_id').count()

def pivot_over_product(df):
	return df.groupBy('product_id').pivot('product_id').sum('count').fillna(0)