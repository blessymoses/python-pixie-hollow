"""
   Calculate Pi using PySpark
"""

import random

from pyspark import SparkContext
from pyspark.sql import SparkSession

NUM_SAMPLES = 100000000


def inside(p):
    x, y = random.random(), random.random()
    return x * x + y * y < 1


sc = SparkContext("local", "Pi App")
print(f"spark context: {sc}")
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
pi = 4 * count / NUM_SAMPLES

print(f"pi: {pi}")
