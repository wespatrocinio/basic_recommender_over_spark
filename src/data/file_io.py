import json

def load_json_file(file_path):
	with open(file_path) as input_file:
		return json.load(input_file)

def generate_output_dict(reference_id, similarities):
	recs = [
		{"product_id": sim[1], "similarity": sim[0]}
		for sim in similarities
		if sim[0] > 0.0 and sim[1] != reference_id
	]
	return {
		"reference_product_id": reference_id,
		"recommendations": recs
	}

def write_json_file(file_path, output_list):
	with open(file_path, 'w') as output_file:
		json.dump(output_list, output_file)