from typing import Any, Dict, Sequence, Tuple, Union
from collections.abc import Mapping, Sequence as SequenceABC


def format(
		self,
		sql: AnyStr,
		params: Union[Dict[Union[str, int], Any], Sequence[Any]],
	) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    template = string.Template(sql)
    if isinstance(params, Mapping):
        params = params.items()
    elif not isinstance(params, SequenceABC):
        raise TypeError('params must be a Mapping or Sequence')

    formatted_sql = template.safe_substitute(params)
    return formatted_sql, params
