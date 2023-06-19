import logging
from pathlib import Path

from src.clusterizer import Clusterizer
from src.utils import read_config

DEFAULT_CONFIG_PATH = Path(__file__).parent / "configs/default.yml"


def main(config):
    model = Clusterizer(config)
    metric = model.fit()
    logging.info(f"Metric: {metric}")
    model.save(config.model.save_path)


if __name__ == "__main__":
    config = read_config(DEFAULT_CONFIG_PATH)
    main(config)
