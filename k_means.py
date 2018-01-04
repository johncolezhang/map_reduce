from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans
import numpy as np
from math import sqrt


if __name__ == "__main__":
    sc = SparkContext(appName="KMeansExample")  # SparkContext
    # Load and parse the data
    data = sc.textFile("data/mllib/kmeans_data.txt")
    parsedData = data.map(lambda line: np.array([float(x) for x in line.split(' ')]))

    # Build the model (cluster the data)
    clusters = KMeans.train(parsedData, k=2, maxIterations=10, initializationMode="random")

    # Evaluate clustering by computing Within Set Sum of Squared Errors
    def error(point):
        #return the cluster center of this point
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x ** 2 for x in (point - center)]))

    WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("Within Set Sum of Squared Error = " + str(WSSSE))
    sc.stop()