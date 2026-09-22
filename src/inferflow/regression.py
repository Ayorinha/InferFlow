"""Benchmark regression gates."""
def within_latency_budget(baseline_ms: float, candidate_ms: float, max_regression: float=.10) -> bool:
    if baseline_ms <= 0 or candidate_ms < 0 or max_regression < 0: raise ValueError("invalid benchmark values")
    return candidate_ms <= baseline_ms * (1 + max_regression)