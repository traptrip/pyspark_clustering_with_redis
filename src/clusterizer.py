import os
import pickle
import shutil

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from src.logger import LOGGER


class Clusterizer:
    def __init__(self, config, raw_data):
        self.spark = (
            SparkSession.builder.master("local[*]")
            .appName("OpenFoodClusterizer")
            .config("spark.num.executors", "2")
            .config("spark.executor.cores", "4")
            .config("spark.executor.memory", "4g")
            .config("spark.driver.memory", "4g")
            .getOrCreate()
        )
        self.sc = self.spark.sparkContext

        self.model = KMeans(k=config.model.k, seed=config.model.seed)
        self.cfg = config

        LOGGER.info("Process data")
        self.preprocess(raw_data)

    def preprocess(self, raw_data):
        raw_data = pickle.loads(raw_data)
        with open("tmp.csv", "wb") as f:
            f.write(raw_data)
        data = self.spark.read.csv("tmp.csv", header=True, sep="\t")
        data = data.sample(self.cfg.data.data_share, 1)

        # keep only selected columns
        data = data.select(
            [col(c).cast("float") for c in self.cfg.model.feature_columns]
        )

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
        LOGGER.info("Training")
        metric = ClusteringEvaluator()
        self.model = self.model.fit(self.data)
        pred = self.model.transform(self.data)

        LOGGER.info("Evaluating")
        m = metric.evaluate(pred)
        return m

    def save(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)
        self.model.save(path)
