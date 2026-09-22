from statistics import mean

def summary(latencies_ms:list[float],tokens:int)->dict[str,float]:
 if not latencies_ms: raise ValueError("latencies cannot be empty")
 total=sum(latencies_ms)
 return {"mean_ms":mean(latencies_ms),"p95_ms":sorted(latencies_ms)[max(0,int(len(latencies_ms)*.95)-1)],"tokens_per_second":tokens/(total/1000) if total else 0.0}
