# PySpark

## install pyspark
```sh
$ pip3 install pyspark

$ pyspark
Python 3.9.5 (default, May 14 2021, 00:00:00) 
[GCC 11.1.1 20210428 (Red Hat 11.1.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/home/blessy/Documents/pieces-of-code/python-virtual-environments/pysparkenv/lib/python3.9/site-packages/pyspark/jars/spark-unsafe_2.12-3.1.2.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
21/07/08 23:21:27 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.2
      /_/

Using Python version 3.9.5 (default, May 14 2021 00:00:00)
Spark context Web UI available at http://fedora:4040
Spark context available as 'sc' (master = local[*], app id = local-1625757688414).
SparkSession available as 'spark'.
>>>
```

## Execute a pyspark script

```sh
$ spark-submit pyspark_pi.py
```

## Examples
- [Calculate Pi using PySpark](pyspark_pi.py)