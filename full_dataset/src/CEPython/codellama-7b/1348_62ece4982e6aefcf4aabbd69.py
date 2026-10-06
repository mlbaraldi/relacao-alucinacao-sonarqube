

def _replace_register(flow_params, register_number, register_value):
    for flow in flow_params:
        if flow["register_value"] == register_value:
            flow["register_number"] = register_number
    return flow_params
