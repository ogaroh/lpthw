#  write functions you can import / export as modules


def break_words(stuff):
    """This function will break words up for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words its given"""
    return sorted(words)


def print_first_word(words):
    """Returns the first words"""
    first_word = words.pop(0)
    print(first_word)


def print_last_word(words):
    """Returns the last word"""
    last_word = words.pop(-1)
    print(last_word)


def sort_sentence(sentence):
    """Sorts a combination of words it's given"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and the last word in a sentence """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Prints the first and last words in a sorted sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
