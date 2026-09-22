import pytest
from inferflow.statistics import percentiles

def test_percentiles():
    result=percentiles([10,20,30,40,50])
    assert result["p50_ms"] == 30
    assert result["p99_ms"] == 50

def test_rejects_negative():
    with pytest.raises(ValueError): percentiles([1,-1])
