# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext, sql

from settings import *
from data.load import load_dataframe
from recommender.datarep import *

conf = SparkConf().setAppName('RecommenderWithSpark')\
	   .set("spark.sql.pivotMaxValues", 500000)\
	   .set('spark.executor.memory','8g')\
	   .set('spark.driver.memory','8g')
sc = SparkContext(conf=conf)
sql_context = sql.SQLContext(sc)

df = load_dataframe("../data/user-product_map_reduced.json", sql_context)
df = aggregate_count_by_user_id(df)
df = generate_collaborative_matrix(df)