"""Tests for trigrams, a program that generates text based on a source text."""

import pytest

BOOKS = [
    (100, 'communist_manifesto.txt', True),
    (500, 'victorian_sexy_fic.txt', True),
    (1000, 'communist_manifesto.txt', True),
    (-1, 'communist_manifesto.txt', False),
    (0, 'communist_manifesto.txt', False),
    ('hello', 'communist_manifesto', False),
]


@pytest.mark.parametrize('n, path, result', BOOKS)
def test_trigrammer(n, path, result):
    from trigram import trigrammer
    result = trigrammer(n, path)
    result_tester = result.split()
    for word in result_tester[2:]:
        if result_tester[word] in trigram_dict[result_tester[word - 2] + ' ' + result_tester[word - 1]]:
            assert True
        else:
            assert False

