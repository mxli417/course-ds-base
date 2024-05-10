import argparse
from typing import Text

import pandas as pd
import yaml
from sklearn.datasets import load_iris

from dumbo.utils.logs import get_logger


def data_load(config_path: Text) -> None:
    """Raw data loading stage function

    Args:
        config_path (Text): path to config file
    """
    with open(config_path, "r") as conf_file:
        config = yaml.safe_load(conf_file)

    logger = get_logger("DATA_LOAD", log_level=config["base"]["log_level"])

    logger.info("Get dataset")
    data = load_iris(as_frame=True)
    dataset = data.frame
    dataset.columns = [
        colname.strip(" (cm)").replace(" ", "_") for colname in dataset.columns.tolist()
    ]
    logger.info("Save raw data")
    dataset.to_csv(config["data_load"]["dataset_csv"], index=False)

    print(f"Data load complete: {dataset.head()}")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
