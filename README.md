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
