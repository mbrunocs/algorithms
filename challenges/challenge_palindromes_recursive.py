def is_palindrome_recursive(word, low_index, high_index):
    if len(word) >= 100: raise(RecursionError)
    mirror = ''
    index = high_index
    while index >= low_index:
        mirror += word[index]
        index -= 1
    return False if mirror != word or word == '' else True
