# -*- coding: utf-8 -*-
import json


def load_json_file(file_path):
	with open(file_path) as json_data:
		return json.load(json_data)

def load_dataframe(file_path):
	json_data = load_json_file(file_path)
	return sqlContext.createDataFrame(json_data)