"""Tests for trigrams, a program that generates text based on a source text."""

DICT_KEYS = {
    'there blazed': ['forth', 'the'],
    'kept down': ['by', 'in'],
    'now got': ['up', 'some'],
    'A singular': ['change,'],
    'at first': ['had']
}


def test_create_dict(path='testpoe.txt'):
    """Test that main outputs actual trigram text."""
    from trigram import create_dict
    trigram_dict = create_dict('testpoe.txt')
    for key in DICT_KEYS:
        assert key in trigram_dict and trigram_dict[key] == DICT_KEYS[key]


def test_get_first_key_words(path='testpoe.txt'):
    """Test if keyword generator produces keywords from dictionary."""
    from trigram import get_first_key_words
    from trigram import create_dict
    created_dict = create_dict(path)
    first_key = get_first_key_words(path, created_dict)
    assert first_key in created_dict


def test_main(path='testpoe.txt', n=50):
    """Test if main produces valid text."""
    from trigram import main
    from trigram import create_dict
    test_dict = create_dict(path)
    text = main(n, path)
    text = text.split()
    for word_idx in range(len(text) - 2):
        test_key = '{} {}'.format(text[word_idx], text[word_idx + 1])
        test_val = text[word_idx + 2]
        assert test_val in test_dict[test_key]
