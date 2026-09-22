from inferflow.benchmark import BenchmarkSample,throughput

def test_throughput_is_tokens_per_second():
    assert throughput(BenchmarkSample("m",100,50,50)) == 1000.0
