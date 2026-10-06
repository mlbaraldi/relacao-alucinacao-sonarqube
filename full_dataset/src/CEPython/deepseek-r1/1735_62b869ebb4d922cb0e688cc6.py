def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for i in range(len(observer_schema)):
        if i >= len(response):
            continue  # Skip if response doesn't have this index
        resp_item = response[i]
        schema_item = observer_schema[i]

        if i >= len(last_applied_manifest):
            # Initialize new item based on schema_item and resp_item
            if isinstance(schema_item, dict):
                new_item = {}
                for key in schema_item:
                    if key in resp_item:
                        new_item[key] = resp_item[key]
                last_applied_manifest.append(new_item)
                # Recursively update the new_item
                update_last_applied_manifest_dict_from_resp(new_item, schema_item, resp_item)
            elif isinstance(schema_item, list):
                new_item = []
                last_applied_manifest.append(new_item)
                update_last_applied_manifest_list_from_resp(new_item, schema_item, resp_item)
            else:
                # For other schema types, append the response item directly
                last_applied_manifest.append(resp_item)
        else:
            manifest_item = last_applied_manifest[i]
            if isinstance(schema_item, dict) and isinstance(manifest_item, dict):
                update_last_applied_manifest_dict_from_resp(manifest_item, schema_item, resp_item)
            elif isinstance(schema_item, list) and isinstance(manifest_item, list):
                update_last_applied_manifest_list_from_resp(manifest_item, schema_item, resp_item)
            # Else, type mismatch, do nothing
