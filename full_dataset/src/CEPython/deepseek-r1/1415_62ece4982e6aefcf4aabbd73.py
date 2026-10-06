def split(s, platform='this'):
    import re
    import sys
    """
    Multi-platform variant of shlex.split() for command-line splitting.
    Uses regular expressions to handle POSIX and Windows/CMD splitting rules.
    """
    if platform == 'this':
        platform = 0 if sys.platform.startswith('win') else 1
    elif platform not in (0, 1):
        raise ValueError("Invalid platform value")

    if platform == 1:
        # POSIX mode: handle single quotes, double quotes, and backslash escapes
        tokens = []
        pos = 0
        length = len(s)
        while pos < length:
            # Skip whitespace
            while pos < length and s[pos].isspace():
                pos += 1
            if pos >= length:
                break
            # Check for quoted token
            if s[pos] == "'":
                # Single-quoted token, find closing quote
                start = pos + 1
                pos = start
                while pos < length and s[pos] != "'":
                    pos += 1
                tokens.append(s[start:pos])
                if pos < length:
                    pos += 1  # skip closing quote
            elif s[pos] == '"':
                # Double-quoted token, handle escaped characters
                start = pos + 1
                pos = start
                escaped = False
                while pos < length:
                    if escaped:
                        escaped = False
                        pos += 1
                    elif s[pos] == '\\':
                        escaped = True
                        pos += 1
                    elif s[pos] == '"':
                        break
                    else:
                        pos += 1
                tokens.append(re.sub(r'\\(.)', r'\1', s[start:pos]))
                pos += 1  # skip closing quote
            else:
                # Unquoted token, handle backslash escapes and concatenate until whitespace
                start = pos
                while pos < length:
                    if s[pos] == '\\' and pos + 1 < length:
                        # Escape next character, skip over backslash and the character
                        pos += 2
                    elif s[pos].isspace():
                        break
                    else:
                        pos += 1
                # Process the unquoted token
                token = re.sub(r'\\(.)', r'\1', s[start:pos])
                tokens.append(token)
        return tokens
    else:
        # Windows mode: handle double quotes and backslashes before quotes
        tokens = []
        for match in re.finditer(r'(")((?:(?:\\"|[^"])*?)(?<!\\)(?:\\\\)*")|([^"]+?)(?=\s|$)|(")', s):
            quoted, content, unquoted, lone_quote = match.groups()
            if content is not None:
                # Quoted content, strip quotes and replace escaped quotes
                tokens.append(content.replace('\\"', '"'))
            elif unquoted is not None:
                # Split unquoted parts on whitespace and extend tokens
                parts = re.split(r'\s+', unquoted.strip())
                tokens.extend(part for part in parts if part)
            elif lone_quote:
                # Handle lone quote as part of unquoted (though this case is more complex)
                tokens.append(lone_quote)
        # Additional step to handle splitting unquoted parts that contain spaces
        # and joining tokens correctly (simplified approach)
        refined = []
        for token in tokens:
            if not refined or (token.startswith('"') and len(token) > 1 and token.endswith('"')):
                refined.append(token)
            else:
                # Split any remaining unquoted spaces (possible due to regex split)
                parts = re.split(r'\s+', token)
                refined.extend(part for part in parts if part)
        # Finally, process each token to handle Windows backslash rules
        final_tokens = []
        for token in refined:
            if token.startswith('"') and token.endswith('"'):
                # Remove surrounding quotes and replace escaped quotes
                stripped = token[1:-1].replace('\\"', '"')
                final_tokens.append(stripped)
            else:
                # No processing needed for unquoted tokens except splitting (already done)
                final_tokens.append(token)
        return [t for t in final_tokens if t]
