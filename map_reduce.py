from functools import reduce
l = [1,1,2,3,4,5]
l = list(map(lambda x: x ** 2, l))
b = reduce(lambda x, y: x if x > y else y, l)
c = reduce(lambda x, y: x + y, filter(lambda x: x > 10, l), 0)
#print(c)

def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x < pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

q = qsort([23,34,534,12,23,12,75,23])
#print(q)


########反序迭代########
for i in range(len(q)-1, -1, -1): #start, stop, stepsize
    print(q[i])



########pi###########
from pyspark.sql import SparkSession
import random
spark = SparkSession.builder.appName("pi").getOrCreate()
partitions = 20
n = 100000 * partitions

def f(_):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    return 1 if x ** 2 + y ** 2 <= 1 else 0


count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(lambda x, y: x + y)
print("Pi is roughly %f" % (4.0 * count / n))

spark.stop()