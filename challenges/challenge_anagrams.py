def dict_letters(word):
    letter = dict()
    for char in word:
        if char in letter:
            letter[char] += 1
        else:
            letter[char] = 1
    return letter

def is_anagram(first_string, second_string):
    if len(second_string) == 0 or len(first_string) == 0:
        return False
    try:
        word = dict_letters(first_string.casefold())
        for c in second_string.casefold():
            if c not in word or word[c] == 0:
                return False
            word[c] -= 1
        return True
    except KeyError:
        return False
