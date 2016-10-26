# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext, sql

from data.load import load_dataframe
from data.datarep import aggregate_count_by_user_id, pivot_over_product
from data.file_io import write_json_file, generate_output_dict
from tools.mathematics import get_cosine_similarity
from recommender.recommend import get_most_similars, generate_collaborative_matrix
from settings import *

# Raise Spark environment
conf = SparkConf().setAppName('RecommenderWithSpark') \
    .set("spark.sql.pivotMaxValues", 500000) \
    .set('spark.executor.memory', '8g') \
    .set('spark.driver.memory', '8g')
sc = SparkContext(conf=conf)
sql_context = sql.SQLContext(sc)

# Load dataset and represent it in the desired way
df = load_dataframe(INPUT_PATH, sql_context)
df = aggregate_count_by_user_id(df)
df = pivot_over_product(df)

# Generate matrix to be computed
collaborative_rdd = generate_collaborative_matrix(df)

output_dict = {}

# Scan all the product ids
for product_id in df.select('product_id').collect()[:50]:
	# Retrieve the 5 most similar products
	similars = get_most_similars(product_id[0], collaborative_rdd)
	output_dict.update(generate_output_dict(product_id[0], similars))

# Write the output file JSON
write_json_file(OUTPUT_PATH, output_dict)