from typing import List


def parse_music(music_string: str) -> List[int]:
    beats = []
    for char in music_string:
        if char == 'o':
            beats.append(4)
        elif char == 'o|':
            beats.append(2)
        elif char == '.|':
            beats.append(1)
        else:
            raise ValueError(f"Invalid character: {char}")
    return beats
