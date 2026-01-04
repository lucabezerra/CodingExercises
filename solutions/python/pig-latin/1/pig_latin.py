VOWELS = ["a", "e", "i", "o", "u"]

def translate(text: str):
    return_values = []
    for word in text.split():
        first_letter_is_vowel = word[0] in VOWELS
        new_word = ""
        if word.startswith("xr") or word.startswith("yt") or first_letter_is_vowel:
            new_word = word
        elif not first_letter_is_vowel:
            consonants = ""
            for i, letter in enumerate(word):
                if letter not in VOWELS:
                    if letter == "y" and len(consonants) >= 1:
                        new_word = word[i:] + consonants
                        break
                    consonants += letter
                else:
                    new_word = word[i:] + consonants
                    if new_word[-1] == "q" and letter == "u":
                        new_word = new_word[1:] + "u"
                    break

        new_word += "ay"
        return_values.append(new_word)
    return " ".join(return_values)