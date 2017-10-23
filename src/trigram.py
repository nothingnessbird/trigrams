"""Function to produce text based on trigrams from input string."""


import random
import sys


def create_dict(path):
    """Create a dictionary of trigrams from a source book."""
    file = open(path)
    book = file.read().replace('\n', ' ')
    file.close()
    split_book = book.split()

    trigram_dict = {}

    coupled_book = iter(split_book)
    next(coupled_book)
    coupled_book_output = [' '.join((first_word, second_word))
                           for first_word, second_word
                           in zip(split_book, coupled_book)]

    for word_set_index in range(len(coupled_book_output)):
        try:
            key_pair = trigram_dict.setdefault(coupled_book_output[word_set_index], [])
            key_pair.append(split_book[word_set_index + 2])
        except IndexError:
            word_set_index = trigram_dict.setdefault(coupled_book_output[word_set_index], [])
    last_two_words = '{} {}'.format(split_book[-2], split_book[-1])
    del trigram_dict[last_two_words]
    return trigram_dict


def get_first_key_words(path, created_dict):
    """Generate random first words from dictionary of trigrams."""
    first_words = random.choice(list(created_dict))
    return first_words


def trigrammer(n, path):
    """Produce a dictionary of trigrams from text, use to build new string."""
    book_dictionary = create_dict(path)
    key_words = get_first_key_words(path, book_dictionary)
    generated_text = ''
    for reps in range(n):
        try:
            added_text = book_dictionary[key_words][random.randint(0, len(book_dictionary[key_words]) - 1)]
            generated_text += added_text + ' '
            key_words = key_words.split(' ')[1] + ' ' + added_text
        except KeyError:
            continue
    print(generated_text)
    return generated_text


if __name__ == '__main__':
    