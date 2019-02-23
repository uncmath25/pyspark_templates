# flake8: noqa
import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("test").setMaster("local[*]")

sc = SparkContext(conf=conf)
spark = SparkSession(sc)
