import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    filename = "data/test.log"
    if len(sys.argv) == 2:
        print("word count, reading file content.......")
        filename = sys.argv[1]

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

    ## text 读一行
    lines = spark.read.text(filename).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
    output = counts.collect()
    for word, count in output:
        print(word, ":", count)

    spark.stop()
