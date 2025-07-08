import yaml
from monitor.collector import collect_metrics
from predict.model import predict_traffic
from decision.engine import decide_scaling
from scale.scaler import execute_scaling

def load_config():
    with open("config.yaml", 'r') as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    metrics = collect_metrics(config)
    predicted_demand = predict_traffic(metrics, config)
    scaling_decision = decide_scaling(predicted_demand, config)
    execute_scaling(scaling_decision, config)

if __name__ == "__main__":
    main()
