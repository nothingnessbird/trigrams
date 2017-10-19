"""Tests for trigrams, a program that generates text based on a source text."""

DICT_KEYS = {
    'there blazed': ['forth', 'the'],
    'kept down': ['by', 'in'],
    'now got': ['up', 'some'],
    'A singular': ['change,'],
    'at first': ['had']
}


def test_create_dict(path='testpoe.txt'):
    """Test that trigrammer outputs actual trigram text."""
    from trigram import create_dict
    trigram_dict = create_dict('testpoe.txt')
    for key in DICT_KEYS:
        assert key in trigram_dict and trigram_dict[key] == DICT_KEYS[key]
