# Pyspark Clustering
ITMO Big data course lab5

Dataset: [openfoodfacts](https://world.openfoodfacts.org/data)

# Project structure
```
├── configs                           <- Configs for the project
│
├── data                              <- Dir where dataset will be placed
│   └── download_data.sh                <- Download raw data
│
├── src                               <- Training utils
│   ├── clusterizer.py                  <- Main class of clustering algorithm
│   ├── word_count.py                   <- Word Count baseline example
│   └── utils.py                        <- Running utils
│
├── main.py                           <- Script to get cluster model
├── requirements.txt                  <- Project requirements
└── README.md                         <- Project documentation
```


# Assets

1. Настроить среду для Spark вычислений: https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows/
2. Обязательно проверить работоспособность компонентов Spark платформы, запустив примеры (WordCount).
3. Разработать на PySpark модель кластеризации на базе алгоритма к-средних. Разрешено использование любых метрик и подходов машинного обучения.

Данные:
https://static.openfoodfacts.org/data/openfoodfacts-
mongodbdump.tar.gz
https://world.openfoodfacts.org/data
4 Можно использовать все доступные средства языка Python/Scala.
Обязательно провести предобработку данных с целью формирования
выборки адекватного размера в зависимости от системных ресурсов.