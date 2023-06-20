import pickle
from pathlib import Path

from src.redis import RedisBroker
from src.utils import read_config

DEFAULT_CONFIG_PATH = Path(__file__).parent / "configs/default.yml"


def store_dataset(config):
    redis_broker = RedisBroker(config.redis)

    with open(config.data.data_path, "rb") as f:
        raw_dataset = f.read()
        raw_dataset = pickle.dumps(raw_dataset)
    redis_broker.set(config.data.raw_dataset_name, raw_dataset)


if __name__ == "__main__":
    config = read_config(DEFAULT_CONFIG_PATH)
    store_dataset(config)
