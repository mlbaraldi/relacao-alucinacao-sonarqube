def format(
		self,
		sql: AnyStr,
		params: Union[Dict[Union[str, int], Any], Sequence[Any]],
	) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    import re
    from collections.abc import Mapping, Sequence
    from typing import AnyStr, Dict, Any, Sequence as Seq, Tuple, Union
    in_named = self.in_style in {'pyformat', 'named', 'numeric'}
    out_named = self.out_style in {'pyformat', 'named', 'numeric'}

    # Extract parameter keys and validate params
    if in_named:
        if not isinstance(params, Mapping):
            raise TypeError("params must be a Mapping for named in_style")
        if self.in_style == 'pyformat':
            pattern = re.compile(r'%\((\w+)\)s')
        elif self.in_style == 'named':
            pattern = re.compile(r':(\w+)')
        elif self.in_style == 'numeric':
            pattern = re.compile(r':(\d+)')
        else:
            raise ValueError(f"Unsupported in_style: {self.in_style}")
        param_keys = pattern.findall(sql)
        for key in param_keys:
            if key not in params:
                raise KeyError(f"Parameter '{key}' not found in params")
        param_values = [params[key] for key in param_keys]
    else:
        if not isinstance(params, Sequence):
            raise TypeError("params must be a Sequence for ordinal in_style")
        if self.in_style == 'qmark':
            pattern = re.compile(r'\?')
        elif self.in_style == 'format':
            pattern = re.compile(r'%s')
        else:
            raise ValueError(f"Unsupported in_style: {self.in_style}")
        matches = pattern.findall(sql)
        param_count = len(matches)
        if len(params) != param_count:
            raise ValueError(f"Expected {param_count} parameters, got {len(params)}")
        param_keys = list(range(param_count))
        param_values = list(params)

    # Generate new SQL and out_params
    if out_named:
        if in_named:
            out_params = {}
            used_keys = set()
            for key in param_keys:
                out_params[key] = params[key]
            if self.out_style == 'pyformat':
                new_sql = re.sub(pattern, r'%(\1)s', sql)
            elif self.out_style == 'named':
                new_sql = re.sub(pattern, r':\1', sql)
            elif self.out_style == 'numeric':
                new_sql = re.sub(pattern, r':\1', sql)
            else:
                raise ValueError(f"Unsupported out_style: {self.out_style}")
        else:
            out_keys = [str(i + 1) for i in range(len(param_values))]
            out_params = {k: v for k, v in zip(out_keys, param_values)}
            replacements = []
            if self.out_style == 'pyformat':
                replacements = [f'%({k})s' for k in out_keys]
            elif self.out_style == 'named':
                replacements = [f':{k}' for k in out_keys]
            elif self.out_style == 'numeric':
                replacements = [f':{i + 1}' for i in range(len(param_values))]
            else:
                raise ValueError(f"Unsupported out_style: {self.out_style}")
            parts = []
            last_end = 0
            if self.in_style == 'qmark':
                matches = list(re.finditer(r'\?', sql))
            else:
                matches = list(re.finditer(r'%s', sql))
            if len(matches) != len(replacements):
                raise ValueError("Mismatch in placeholder count during replacement")
            for i, match in enumerate(matches):
                start, end = match.start(), match.end()
                parts.append(sql[last_end:start])
                parts.append(replacements[i])
                last_end = end
            parts.append(sql[last_end:])
            new_sql = ''.join(parts)
    else:
        out_params = param_values
        if self.out_style == 'qmark':
            replacement = '?'
        elif self.out_style == 'format':
            replacement = '%s'
        else:
            raise ValueError(f"Unsupported ordinal out_style: {self.out_style}")
        if in_named:
            if self.in_style == 'pyformat':
                pattern = re.compile(r'%\(\w+\)s')
            elif self.in_style == 'named':
                pattern = re.compile(r':\w+')
            elif self.in_style == 'numeric':
                pattern = re.compile(r':\d+')
            new_sql = pattern.sub(replacement, sql)
        else:
            if self.in_style == 'qmark' and self.out_style == 'format':
                new_sql = sql.replace('?', '%s')
            elif self.in_style == 'format' and self.out_style == 'qmark':
                new_sql = sql.replace('%s', '?')
            else:
                new_sql = sql

    return (new_sql, out_params)
