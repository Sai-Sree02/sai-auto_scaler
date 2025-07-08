def execute_scaling(decision, config):
    print(f"[Scaler] Decision: {decision}")
    if decision == "scale_up":
        print("Scaling up resources...")
    elif decision == "scale_down":
        print("Scaling down resources...")
    else:
        print("No scaling action required.")
