import json

def load_json_file(file_path):
	with open(file_path) as json_data:
		return json.load(json_data)