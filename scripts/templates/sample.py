from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum as _sum
from pyspark.sql.types import FloatType, IntegerType, StringType, StructField, StructType


# Get spark context and session
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

# RDD Sample
values = [
    [1, 'grocery', 'Trader Joes', 53.46, 'weekly groceries'],
    [2, 'dining', 'Chiptole', 7.87, 'burrito for lunch'],
    [3, 'upkeep', 'CVS', 6.59, None],
    [4, 'upkeep', 'Chevron', 43.13, 'car gas fillup'],
    [5, 'grocery', 'Trader Joes', 5.42, 'dessert :)']
]
rdd = sc.parallelize(values)
print('#############################################################')
print('Count: {count}'.format(count=rdd.count()))
print(rdd.collect())
print('#############################################################')

# DataFrame Sample
schema = StructType([
    StructField(name='transaction_id', dataType=IntegerType(), nullable=False),
    StructField(name='type', dataType=StringType(), nullable=False),
    StructField(name='vendor', dataType=StringType(), nullable=False),
    StructField(name='amount', dataType=FloatType(), nullable=False),
    StructField(name='description', dataType=StringType(), nullable=True)
])
df = spark.createDataFrame(rdd, schema)
print('Count: {count}'.format(count=df.count()))
print(df.collect())
print('#############################################################')

# Pivoting Example
category_agg_df = df \
    .withColumn('category', col('type')) \
    .groupBy('category') \
    .agg(_sum('amount').alias('total')) \
    .select('category', 'total')
print('Count: {count}'.format(count=category_agg_df.count()))
print(category_agg_df.collect())
print('#############################################################')
