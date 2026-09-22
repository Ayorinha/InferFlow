from inferflow.core import InferenceSample, summarize

def test_metrics():
    m = summarize([InferenceSample(10, 5), InferenceSample(20, 7, False)])
    assert m.requests == 2 and m.successes == 1 and m.tokens == 12 and m.avg_latency_ms == 15
