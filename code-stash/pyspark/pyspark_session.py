"""
   catalog - lists all the data inside the cluster

   listTables() - returns the names of all the tables in the cluster as a list

"""
from pyspark.sql import SparkSession

my_spark = SparkSession.builder.getOrCreate()

print(f"\nspark session: {my_spark}")

# Print the tables in the catalog
print(f"\nTables: {my_spark.catalog.listTables()}")
