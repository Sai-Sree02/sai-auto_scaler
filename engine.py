def decide_scaling(predicted_demand, config):
    print("[Decision] Evaluating scaling requirements...")
    max_rpm = 1200
    load_ratio = predicted_demand / max_rpm

    if load_ratio > config['scale_up_threshold']:
        return "scale_up"
    elif load_ratio < config['scale_down_threshold']:
        return "scale_down"
    else:
        return "no_action"
