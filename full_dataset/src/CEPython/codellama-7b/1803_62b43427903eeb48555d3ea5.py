

def format(
		self,
		sql: AnyStr,
		params: Union[Dict[Union[str, int], Any], Sequence[Any]],
	) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    # Check if the SQL query is a string or bytes
    if not isinstance(sql, (str, bytes)):
        raise ValueError("SQL query must be a string or bytes")

    # Check if the parameters are a dictionary or a sequence
    if not isinstance(params, (dict, list)):
        raise ValueError("Parameters must be a dictionary or a sequence")

    # Check if the parameters are in the correct format
    if isinstance(params, dict):
        if not all(isinstance(key, (str, int)) and isinstance(value, Any) for key, value in params.items()):
            raise ValueError("Parameters must be a dictionary with string or integer keys and any values")
    elif isinstance(params, list):
        if not all(isinstance(value, Any) for value in params):
            raise ValueError("Parameters must be a list with any values")

    # Convert the SQL query to use out-style parameters
    formatted_sql = sql.replace("?", ":param{}".format(len(params) + 1))

    # Convert the parameters to out-style parameters
    out_params = {}
    if isinstance(params, dict):
        for key, value in params.items():
            out_params[":param{}".format(key)] = value
    elif isinstance(params, list):
        for i, value in enumerate(params):
            out_params[":param{}".format(i + 1)] = value

    return formatted_sql, out_params
