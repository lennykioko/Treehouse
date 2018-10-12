def sillycase(word):
    new_word = ""
    half_length = len(word) // 2
    new_word += word[:half_length].lower()
    new_word += word[half_length:].upper()
    return new_word

print(sillycase("Treehouse"))
