import stand_dist
import logging
from pathlib import Path

LOGGING_FORMATTER = ("%(asctime)s %(process)s:%(thread)d " + 
  "%(levelname)s %(module)s:%(funcName)s:%(lineno)d -- %(message)s")

logger = logging.getLogger("pystandlogger")
logger.setLevel(logging.DEBUG)

cl = logging.StreamHandler()
cl.setLevel(logging.INFO)
cl.setFormatter(logging.Formatter(LOGGING_FORMATTER))

logger.addHandler(cl)

logger.info({"event": "starting code"})

for x in range(20):
    stand_dist.summary()