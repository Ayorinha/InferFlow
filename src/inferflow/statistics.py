from statistics import mean

def percentiles(latencies_ms: list[float]) -> dict[str,float]:
    if not latencies_ms or any(x < 0 for x in latencies_ms):
        raise ValueError("latencies must be non-empty and non-negative")
    values=sorted(latencies_ms)
    def pct(p):
        idx=min(len(values)-1, max(0, int(round((p/100)*(len(values)-1)))))
        return values[idx]
    return {"mean_ms":mean(values),"p50_ms":pct(50),"p95_ms":pct(95),"p99_ms":pct(99)}
