"""Reproducible inference benchmark records."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BenchmarkSample:
    model: str
    latency_ms: float
    input_tokens: int
    output_tokens: int

def throughput(sample: BenchmarkSample) -> float:
    if sample.latency_ms <= 0:
        raise ValueError("latency_ms must be positive")
    return (sample.input_tokens + sample.output_tokens) / (sample.latency_ms / 1000.0)
