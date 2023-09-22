

def calculate_word_strength(word):
    ascii_sum = sum(ord(char) for char in word)
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        strength = ascii_sum * len(word)
    else:
        strength = ascii_sum // len(word)
    return strength


best_word = ""
max_strength = float('-inf')

while True:
    word = input()
    if word == "End of words":
        break

    word_strength = calculate_word_strength(word)

    if word_strength > max_strength:
        max_strength = word_strength
        best_word = word

print(f"The most powerful word is {best_word} - {max_strength}")
