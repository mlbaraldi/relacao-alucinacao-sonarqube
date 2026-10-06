from typing import AnyStr, Dict, Union, Sequence, Tuple


def format(
		self,
		sql: AnyStr,
		params: Union[Dict[Union[str, int], Any], Sequence[Any]],
	) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convert the SQL query to use the out-style parameters instead of
    the in-style parameters.
    """
    if isinstance(params, dict):
        # Named parameter style
        out_params = {}
        for key, value in params.items():
            sql = sql.replace(':' + str(key), '%s')
            out_params[key] = value
        return sql, out_params
    else:
        # Ordinal parameter style
        out_params = list(params)
        sql = sql.replace(':', '%s', len(out_params))
        return sql, out_params
