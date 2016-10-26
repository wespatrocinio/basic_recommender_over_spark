# -*- coding: utf-8 -*-
from file_io import load_json_file
from datarep import aggregate_count_by_user_id, pivot_over_product
from settings import *

def load_dataframe(sql_context):
	json_data = load_json_file()
	return sql_context.createDataFrame(json_data["input"])

def get_product_data(sql_context):
	df = load_dataframe(sql_context)
	df = aggregate_count_by_user_id(df)
	return pivot_over_product(df)