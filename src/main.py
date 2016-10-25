# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext, sql
from pyspark.mllib.linalg.distributed import IndexedRowMatrix, IndexedRow

from data.load import load_dataframe
from data.datarep import aggregate_count_by_user_id, pivot_over_product
from recommender.recommend import get_most_similars

# Raise Spark environment
conf = SparkConf().setAppName('RecommenderWithSpark') \
    .set("spark.sql.pivotMaxValues", 500000) \
    .set('spark.executor.memory', '8g') \
    .set('spark.driver.memory', '8g')
sc = SparkContext(conf=conf)
sql_context = sql.SQLContext(sc)

# Load dataset and represent it in the desired way
df = load_dataframe("../data/data_reduced.json", sqlContext)
df = aggregate_count_by_user_id(df)
df = pivot_over_product(df)

# Generate matrix to be computed
matrix = IndexedRowMatrix(df.rdd.map(lambda row: IndexedRow(row.product_id, row[1:])))

# Calculate the cosine similarity for all columns

# Scan all the product ids

# Retrieve the 5 most similar products

# Write the output file JSON