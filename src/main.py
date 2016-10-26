# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext, sql

from data.load import get_product_data
from data.file_io import write_json_file, generate_output_dict
from recommender.recommend import get_most_similars, generate_collaborative_matrix

# Raise Spark environment
conf = SparkConf().setAppName('RecommenderWithSpark') \
    .set("spark.sql.pivotMaxValues", 500000) \
    .set('spark.executor.memory', '8g') \
    .set('spark.driver.memory', '8g')
sc = SparkContext(conf=conf)
sql_context = sql.SQLContext(sc)

# Load dataset and represent it in the desired way
df = get_product_data(sql_context)

# Generate matrix to be computed
collaborative_rdd = generate_collaborative_matrix(df)

output_recs = []

# Scan all the product ids
for product_id in df.select('product_id').collect():
	print product_id[0]
	# Retrieve the 5 most similar products
	similars = get_most_similars(product_id[0], collaborative_rdd)
	output_recs.append(generate_output_dict(product_id[0], similars))

# Write the output file JSON
write_json_file(output_recs)