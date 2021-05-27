from typing import Callable, MutableMapping, Text
import numpy as np
import logging
from pathlib import Path
import argparse
from aws_logging_handlers.Kinesis import KinesisHandler

stand_dist_logger = logging.getLogger("pystandlogger.stand_dist")
stand_dist_logger.setLevel(logging.INFO)

value_logger = logging.getLogger("pystandlogger.stand_dist.values")
value_logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(Path("./values.json", encoding="utf-8", mode="w"))
fh.setFormatter(logging.Formatter("%(message)s"))
fh.setLevel(logging.DEBUG)

value_logger.addHandler(fh)

def generate_standard(mean: float = 0, st_dev: float = 1, n: int = 1000) -> np.ndarray:
  """
  generate a standard distrubution bases on parameters

  :param mean: mean value expect (average)
  :param st_dev: standard deviation expected
  :parm n: number of values generated
  :returns: np.ndarray of values
  """
  stand_dist_logger.info({"event": "generate", "text": "generating distrubution"})
  dist = np.random.normal(loc = mean, scale = st_dev, size = n)

  # log to a json file the values from dist
  value_logger.debug({"event": "values", "values": list(dist)})
  return np.array(dist)

def summary(func: Callable[..., np.ndarray] = generate_standard, **kwargs) -> MutableMapping[Text, float]:
  """
  Creates summary stats of distrubution

  :param func: distrubution generator (default is generate)
  :returns: summary stats
  """
  gen_dist = func(**kwargs)
  summary_dict = { 
    "median": np.median(gen_dist), 
    "mean": np.mean(gen_dist), 
    "standard_dev": np.std(gen_dist),
    "n": len(gen_dist)
    }

  stand_dist_logger.info({"event": "summary", **summary_dict})
  return summary_dict

def setup_parser() -> argparse.ArgumentParser:
  pass