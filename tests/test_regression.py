from inferflow.regression import within_latency_budget
def test_latency_regression_gate():
    assert within_latency_budget(100,105)
    assert not within_latency_budget(100,120)