

def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for field in observer_schema:
        if field not in last_applied_manifest:
            last_applied_manifest[field] = response[field]

    for item in response:
        if isinstance(item, list):
            update_last_applied_manifest_list_from_resp(last_applied_manifest[item], observer_schema[item], response[item])
        elif isinstance(item, dict):
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[item], observer_schema[item], response[item])
