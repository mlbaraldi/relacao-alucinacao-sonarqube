

def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for i, schema in enumerate(observer_schema):
        if isinstance(schema, dict):
            for key in schema:
                if key not in last_applied_manifest[i]:
                    if key in response[i]:
                        last_applied_manifest[i][key] = response[i][key]
                    else:
                        last_applied_manifest[i][key] = None
        elif isinstance(schema, list):
            if not last_applied_manifest[i]:
                last_applied_manifest[i] = [None] * len(schema)
            update_last_applied_manifest_list_from_resp(last_applied_manifest[i], schema, response[i])
        else:
            if not last_applied_manifest[i]:
                last_applied_manifest[i] = None
            if schema in response[i]:
                last_applied_manifest[i] = response[i][schema]
    return last_applied_manifest
