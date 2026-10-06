

def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    for field in observer_schema:
        if field not in response:
            raise KeyError(f"Observed field {field} is not present in the Kubernetes response")
        last_applied_manifest[field] = response[field]
