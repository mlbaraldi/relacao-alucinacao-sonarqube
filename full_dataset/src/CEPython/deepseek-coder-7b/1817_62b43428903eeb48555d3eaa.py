from typing import Any, AnyStr, Dict, Iterable, List, Sequence, Tuple, Union


def formatmany(
		self,
		sql: AnyStr,
		many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
	) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    formatted_sql = sql
    formatted_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Convert in-style parameters to out-style
            out_style_params = {k: '?' for k in params.keys()}
            formatted_sql = formatted_sql.replace('%s', '?')
            formatted_params.append(out_style_params)
        elif isinstance(params, Sequence):
            # Convert in-style parameters to out-style
            out_style_params = ['?' for _ in params]
            formatted_sql = formatted_sql.replace('%s', '?')
            formatted_params.append(out_style_params)

    return formatted_sql, formatted_params
