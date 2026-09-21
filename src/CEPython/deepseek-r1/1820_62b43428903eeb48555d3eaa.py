def formatmany(
		self,
		sql: AnyStr,
		many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
	) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    import re
    from itertools import count
    from typing import AnyStr, Union, Iterable, Dict, Sequence, Tuple, List

    param_list = list(many_params)
    if not param_list:
        return (sql, [])

    first_param = param_list[0]
    converted_sql = sql
    converted_params = []

    if self.in_style in ('pyformat', 'named'):
        if isinstance(first_param, dict):
            param_names = self._extract_named_params(sql)
            converted_sql = self._convert_sql_named_to_outstyle(sql, param_names)
            if self.out_style in ('qmark', 'format', 'numeric'):
                converted_params = [[p[name] for name in param_names] for p in param_list]
            else:
                converted_params = param_list
        else:
            raise TypeError("Named in_style requires parameters to be mappings.")
    else:
        num_params = self._count_ordinal_params(sql)
        if isinstance(first_param, (list, tuple)):
            if self.out_style in ('qmark', 'format', 'numeric'):
                converted_sql = self._convert_sql_ordinal_to_outstyle(sql)
                converted_params = param_list
            else:
                converted_sql = self._convert_sql_ordinal_to_named(sql)
                if self.out_style == 'named':
                    converted_params = [{str(i+1): val for i, val in enumerate(p)} for p in param_list]
                elif self.out_style == 'pyformat':
                    converted_params = [{i: val for i, val in enumerate(p)} for p in param_list]
                else:
                    converted_params = param_list
        else:
            raise TypeError("Ordinal in_style requires parameters to be sequences.")

    return (converted_sql, converted_params)
