def is_anagram(first_string, second_string):
    word = dict()
    if len(second_string) == 0 or len(first_string) == 0:
        return False
    try:
        for c in first_string.casefold():
            if c in word:
                word[c] += 1
            else:
                word[c] = 1
        for c in second_string.casefold():
            if not c in word or word[c] == 0:
                return False
            word[c] -= 1
        return True
    except KeyError:
        return False
