import logging

import psutil
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


class Clusterizer:
    def __init__(self, config):
        self.spark = (
            SparkSession.builder.appName("OpenFoodEDA")
            .config("spark.num.executors", "2")
            .config("spark.executor.cores", "4")
            .config("spark.executor.memory", "4g")
            .config("spark.driver.memory", "4g")
            .getOrCreate()
        )

        self.model = KMeans(k=config.model.k, seed=config.model.seed)
        self.cfg = config

        print("Process data")
        data = self.spark.read.csv(config.data_path, header=True, sep="\t")
        self.preprocess(data)

    def preprocess(self, data):
        data = data.sample(self.cfg.data_share, 1)

        # keep only selected columns
        data = data.select([col(c).cast("float") for c in self.cfg.feature_columns])

        # process NaNs
        data = data.na.fill(0.0).na.fill("unk")

        # Scale data
        data = (
            VectorAssembler(inputCols=data.columns, outputCol="raw_features")
            .setHandleInvalid("error")
            .transform(data)
        )
        scaler = MinMaxScaler(inputCol="raw_features", outputCol="features")
        self.data = scaler.fit(data).transform(data)

    def fit(self):
        print("Training")
        metric = ClusteringEvaluator()
        self.model = self.model.fit(self.data)
        pred = self.model.transform(self.data)

        print("Evaluating")
        m = metric.evaluate(pred)
        return m

    def save(self, path):
        self.model.overwrite().save(path)
