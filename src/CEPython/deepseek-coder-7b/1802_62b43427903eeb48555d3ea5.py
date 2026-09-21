from typing import Any, AnyStr, Dict, Sequence, Tuple, Union


def format(
		self,
		sql: AnyStr,
		params: Union[Dict[Union[str, int], Any], Sequence[Any]],
	) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Convert the SQL query to use the out-style parameters instead of
    the in-style parameters.

    *sql* (:class:`str` or :class:`bytes`) is the SQL query.

    *params* (:class:`~collections.abc.Mapping` or :class:`~collections.abc.Sequence`)
    contains the set of in-style parameters. It maps each parameter
    (:class:`str` or :class:`int`) to value. If :attr:`.SQLParams.in_style`
    is a named parameter style. then *params* must be a :class:`~collections.abc.Mapping`.
    If :attr:`.SQLParams.in_style` is an ordinal parameter style, then
    *params* must be a :class:`~collections.abc.Sequence`.

    Returns a :class:`tuple` containing:

    -       The formatted SQL query (:class:`str` or :class:`bytes`).

    -       The set of converted out-style parameters (:class:`dict` or
             :class:`list`).
    """
    if isinstance(params, dict):
        out_style_params = params
    else:
        out_style_params = {i: params[i] for i in range(len(params))}

    formatted_sql = sql
    if isinstance(sql, str):
        for param, value in out_style_params.items():
            placeholder = f':{param}'
            if placeholder in sql:
                formatted_sql = sql.replace(placeholder, str(value))
            else:
                placeholder = '?'
