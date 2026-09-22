from dataclasses import dataclass
@dataclass(frozen=True)
class InferenceSample:latency_ms:float;tokens:int;success:bool=True
@dataclass(frozen=True)
class Metrics:requests:int;successes:int;avg_latency_ms:float;tokens:int
def summarize(samples):
 if not samples:return Metrics(0,0,0.0,0)
 return Metrics(len(samples),sum(s.success for s in samples),sum(s.latency_ms for s in samples)/len(samples),sum(s.tokens for s in samples))
