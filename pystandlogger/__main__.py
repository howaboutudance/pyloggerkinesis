from . import stand_dist
import logging
from pathlib import Path
import argparse
import os
import time
from aws_logging_handlers.Kinesis import KinesisHandler

# Logging Configuratiion
LOGGING_FORMATTER = ("%(asctime)s %(process)s:%(thread)d " + 
  "%(levelname)s %(module)s:%(funcName)s:%(lineno)d -- %(message)s")

logger = logging.getLogger("pystandlogger")
logger.setLevel(logging.DEBUG)

cl = logging.StreamHandler()
cl.setLevel(logging.INFO)
cl.setFormatter(logging.Formatter(LOGGING_FORMATTER))

logger.addHandler(cl)

kl = KinesisHandler("logger_test", "us-west-2")
kl.setLevel(logging.INFO)
kl.setFormatter(logging.Formatter(LOGGING_FORMATTER))
logger.addHandler(kl)

logger.info({"event": "starting code"})


if (env_n := os.environ.get("N_RECORDS")):
  n_default = int(env_n)
else:
  n_default = 200

# argparse setup
parser = argparse.ArgumentParser()
parser.add_argument("-n", default=n_default, type=int)

args = parser.parse_args()
n_records: int = args.n 

for x in range(n_records):
    stand_dist.summary()
    time.sleep(0.1)
