

def _replace_register(flow_params, register_number, register_value):
    for flow in flow_params:
        if register_value in flow_params[flow]:
            flow_params[flow][register_number] = flow_params[flow].pop(register_value)
    return flow_params
