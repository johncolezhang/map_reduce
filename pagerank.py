import re
from pyspark.sql import SparkSession


def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]


if __name__ == "__main__":
    # Initialize the spark context.
    spark = SparkSession.builder.appName("PythonPageRank").getOrCreate()
    # Loads in input file. It should be in format of:
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     ...
    lines = spark.read.text("data/mllib/pagerank_data.txt").rdd.map(lambda r: r[0])
    # Loads all URLs from input file and initialize their neighbors.
    # links : [(URL, neighbor URL), ......]
    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()
    # Loads all URLs with other URL(s) link to from input file and initialize ranks of them to 1.
    # ranks : [(URL, 1), ......]
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    for iteration in range(30):
        # Calculates URL contributions to the rank of other URLs.
        # join : [(URL, (list(neighbor)), 1), ......]
        contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
        # Re-calculates URL ranks based on neighbor contributions.
        # ranks : [(URL, score), ......]
        ranks = contribs.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: rank * 0.85 + 0.15)
        print(ranks.collect())


