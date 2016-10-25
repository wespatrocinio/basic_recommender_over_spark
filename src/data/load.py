# -*- coding: utf-8 -*-
from file_io import load_json_file

def load_dataframe(file_path, sql_context):
	json_data = load_json_file(file_path)
	return sql_context.createDataFrame(json_data["input"])