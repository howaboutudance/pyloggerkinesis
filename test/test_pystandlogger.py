import pytest
from pystandlogger import stand_dist
import numpy as np
import logging

def test_stand_dist_default():
  dist = stand_dist.generate_standard()
  assert isinstance(dist, np.ndarray)
  assert 1 == np.round(np.std(dist))
  assert 0 == np.round(np.mean(dist))
  
def test_stand_dist_vars():
  dist = stand_dist.generate_standard(mean = 5, st_dev = 2)
  assert isinstance(dist, np.ndarray)
  assert 2 == np.round(np.std(dist))
  assert 5 == np.round(np.mean(dist))

def test_stand_dist_summaries_debug(caplog):
  caplog.set_level(logging.DEBUG)
  res = stand_dist.summary()

  info_rec = 0
  for record in caplog.records:
    assert record.levelname != "CRITICAL"
    if record.levelname == "INFO":
      info_rec += 1
    
  assert info_rec > 0  
  assert "median" in caplog.text
  assert "mean" in caplog.text
  assert "standard_dev" in caplog.text

