# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf, sql

import json


def load_json_file(file_path):
	with open(file_path) as json_data:
		return json.load(json_data)

def load_dataframe(file_path, sql_context):
	json_data = load_json_file(file_path)
	return sql_context.createDataFrame(json_data["input"])