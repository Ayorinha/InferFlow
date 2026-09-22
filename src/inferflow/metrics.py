from statistics import mean
def summary(latencies_ms,tokens):
 if not latencies_ms: raise ValueError('empty')
 s=sorted(latencies_ms); return {'mean_ms':mean(s),'p95_ms':s[max(0,int(len(s)*.95)-1)],'tokens_per_second':tokens/(sum(s)/1000) if sum(s) else 0}
