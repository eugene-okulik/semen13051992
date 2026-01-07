words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def new_words():
    for name, value in words.items():
        print(name * value)


new_words()
