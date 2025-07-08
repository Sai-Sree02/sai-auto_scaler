import random

def collect_metrics(config):
    print("[Monitor] Collecting current performance metrics...")
    return {
        'cpu_utilization': random.uniform(0.2, 0.9),
        'requests_per_minute': random.randint(100, 1000)
    }
