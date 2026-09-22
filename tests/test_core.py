from inferflow.core import *

def test_metrics():assert summarize([InferenceSample(10,5)]).tokens==5
