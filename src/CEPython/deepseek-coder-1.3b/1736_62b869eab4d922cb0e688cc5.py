

def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    Together with :func:``update_last_applied_manifest_list_from_resp``, this
    function is called recursively to update a partial ``last_applied_manifest``
    from a partial Kubernetes response

    Args:
        last_applied_manifest (dict): partial ``last_applied_manifest`` being
            updated
        observer_schema (dict): partial ``observer_schema``
        response (dict): partial response from the Kubernetes API.

    Raises:
        KeyError: If the observed field is not present in the Kubernetes response
    """
    for key, value in observer_schema.items():
        if isinstance(value, dict):
            # If the observed field is a dictionary, recursively update it
            if key in response:
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest, value, response[key]
                )
            else:
                raise KeyError(f"Observed field {key} not found in response")
        else:
            # If the observed field is not a dictionary, update it
            if key in last_applied_manifest:
                last_applied_manifest[key] = response.get(key, value)
            else:
                raise KeyError(f"Observed field {key} not found in manifest")
