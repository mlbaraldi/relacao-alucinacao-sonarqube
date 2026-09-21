

def formatmany(
		self,
		sql: AnyStr,
		many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
	) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    # Check if the SQL query is a string or bytes
    if not isinstance(sql, (str, bytes)):
        raise TypeError("sql must be a string or bytes")

    # Check if the many_params is an iterable
    if not isinstance(many_params, Iterable):
        raise TypeError("many_params must be an iterable")

    # Check if the many_params is a list or tuple
    if not isinstance(many_params, (list, tuple)):
        raise TypeError("many_params must be a list or tuple")

    # Check if the many_params is a list of dicts or a list of sequences
    if not all(isinstance(p, (dict, list, tuple)) for p in many_params):
        raise TypeError("many_params must be a list of dicts or a list of sequences")

    # Check if the many_params is a list of dicts and all the dicts have the same keys
    if isinstance(many_params, list) and not all(set(p.keys()) == set(many_params[0].keys()) for p in many_params):
        raise ValueError("many_params must be a list of dicts with the same keys")

    # Check if the many_params is a list of sequences and all the sequences have the same length
    if isinstance(many_params, list) and not all(len(p) == len(many_params[0]) for p in many_params):
        raise ValueError("many_params must be a list of sequences with the same length")

    # Check if the many_params is a list of dicts and all the dicts have the same values
    if isinstance(many_params, list) and not all(p.values() == many_params[0].values() for p in many_params):
        raise Value
