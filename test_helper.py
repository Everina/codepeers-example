from typing import Any, Callable, List
import json

def deep_equals(got: Any, expected: Any) -> bool:
    return json.dumps(got) == json.dumps(expected)
    
def general_test(fn, test_cases):
    for i, case in enumerate(test_cases):
        *params, expected = case
        ret = fn(*params)
        if not deep_equals(ret, expected):
            raise RuntimeError(f"wrong answer on test case {i + 1}, got {ret}")
    
def test_two_sum(fn: Callable[[List[int], int], List[int]]):
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2])
    ]
    general_test(fn, test_cases)

def test_length_of_longest_substring(fn: Callable[[str], int]):
    test_cases = [
        ("abcabcbb", 3),
        ("pwwkew", 6)
    ]
    general_test(fn, test_cases)