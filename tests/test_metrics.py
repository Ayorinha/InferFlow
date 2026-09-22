from inferflow.metrics import *
def test_summary(): assert summary([10,20],100)['mean_ms']==15
