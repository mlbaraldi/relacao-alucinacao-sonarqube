from typing import AnyStr, Union, Iterable, Dict, Sequence, Tuple, List


def formatmany(
		self,
		sql: AnyStr,
		many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
	) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            for key, value in params.items():
                formatted_sql = formatted_sql.replace(':' + str(key), str(value))
                params[key] = value
            formatted_params.append(params)
        elif isinstance(params, Sequence):
            for i, value in enumerate(params):
                formatted_sql = formatted_sql.replace('?' + str(i+1), str(value))
                params[i] = value
            formatted_params.append(params)

    return formatted_sql, formatted_params
