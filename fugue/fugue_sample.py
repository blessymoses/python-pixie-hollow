from timeit import timeit
from typing import Dict

import fugue.api as fa
import pandas as pd
from fugue import transform

# from fugue.api import engine_context

input_df = pd.DataFrame({"id": [0, 1, 2], "value": (["A", "B", "C"])})
map_dict = {"A": "Apple", "B": "Banana", "C": "Carrot"}


# @timeit
def map_letter_to_food(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    df["value"] = df["value"].map(mapping)
    return df


mapped_df = map_letter_to_food(input_df, map_dict)
print(mapped_df)


# Spark execution engine
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark_input_df = spark.createDataFrame(input_df)

spark_input_df.show()

out = transform(
    spark_input_df,
    map_letter_to_food,
    schema="*",
    params=dict(mapping=map_dict),
)
# out is a Spark DataFrame
out.show()
