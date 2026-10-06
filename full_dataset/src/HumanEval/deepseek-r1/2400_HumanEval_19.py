from typing import List


def sort_numbers(numbers: str) -> str:
    from typing import List
    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word_to_num = {word: idx for idx, word in enumerate(num_words)}
    words = numbers.split()
    nums = [word_to_num[word] for word in words]
    sorted_nums = sorted(nums)
    sorted_words = [num_words[num] for num in sorted_nums]
    return ' '.join(sorted_words)
