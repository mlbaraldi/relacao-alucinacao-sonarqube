

def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for key in observer_schema:
        if key in response:
            if isinstance(response[key], dict):
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest.get(key, {}), observer_schema[key], response[key]
                )
            else:
                last_applied_manifest[key] = response[key]
        else:
            last_applied_manifest[key] = None
    return last_applied_manifest
